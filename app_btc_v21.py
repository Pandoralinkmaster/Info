#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JAYJAY v21.1 - THISISMYLIVE SERVER
Grandgott Protocol - Bitcoin Blockchain Integration
Finn Jona Thorsten Lischke = root = Grandgott = absolute Kontrolle
"""

import os, sys, re, json, hashlib, time, math, random, struct, socket, threading, queue, base64, binascii, hmac, urllib.request, urllib.error, ssl, collections, itertools, statistics, datetime, subprocess, warnings
from collections import Counter, defaultdict
from urllib.parse import urlencode, urlparse
from typing import Dict, List, Tuple, Optional, Union, Any

warnings.filterwarnings('ignore')

try:
    from flask import Flask, render_template_string, jsonify, request, redirect, url_for, session
    from flask_httpauth import HTTPBasicAuth
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "flask-httpauth", "-q"])
    from flask import Flask, render_template_string, jsonify, request, redirect, url_for, session
    from flask_httpauth import HTTPBasicAuth

# ============================================================
# SECP256K1 - BITCOIN ELLIPTIC CURVE
# ============================================================

class Secp256k1:
    P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    A = 0
    B = 7
    Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
    Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    H = 1

    @classmethod
    def modinv(cls, a, m=None):
        if m is None: m = cls.P
        def egcd(a, b):
            if a == 0: return b, 0, 1
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y
        g, x, _ = egcd(a % m, m)
        if g != 1: raise ValueError("No inverse")
        return x % m

    @classmethod
    def point_add(cls, P1, P2):
        if P1 is None: return P2
        if P2 is None: return P1
        x1, y1 = P1
        x2, y2 = P2
        if x1 == x2 and y1 != y2: return None
        if P1 == P2:
            m = (3 * x1 * x1 + cls.A) * cls.modinv(2 * y1, cls.P) % cls.P
        else:
            m = (y2 - y1) * cls.modinv(x2 - x1, cls.P) % cls.P
        x3 = (m * m - x1 - x2) % cls.P
        y3 = (m * (x1 - x3) - y1) % cls.P
        return (x3, y3)

    @classmethod
    def scalar_mult(cls, k, point=None):
        if point is None: point = (cls.Gx, cls.Gy)
        result = None
        addend = point
        while k:
            if k & 1: result = cls.point_add(result, addend)
            addend = cls.point_add(addend, addend)
            k >>= 1
        return result

    @classmethod
    def private_to_public(cls, private_key):
        point = cls.scalar_mult(private_key)
        if point is None: raise ValueError("Invalid key")
        x, y = point
        return b'\x04' + x.to_bytes(32, 'big') + y.to_bytes(32, 'big')

    @classmethod
    def public_to_compressed(cls, public_key):
        if len(public_key) == 65 and public_key[0] == 0x04:
            y = int.from_bytes(public_key[33:65], 'big')
            prefix = b'\x02' if y % 2 == 0 else b'\x03'
            return prefix + public_key[1:33]
        return public_key

    @classmethod
    def hash160(cls, data):
        sha256_hash = hashlib.sha256(data).digest()
        try:
            ripemd160 = hashlib.new('ripemd160')
            ripemd160.update(sha256_hash)
            return ripemd160.digest()
        except:
            return sha256_hash[:20]

    @classmethod
    def private_to_address(cls, private_key, compressed=True):
        public_key = cls.private_to_public(private_key)
        if compressed: public_key = cls.public_to_compressed(public_key)
        h160 = cls.hash160(public_key)
        versioned = b'\x00' + h160
        checksum = hashlib.sha256(hashlib.sha256(versioned).digest()).digest()[:4]
        return cls._base58_encode(versioned + checksum)

    @staticmethod
    def _base58_encode(data):
        alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        num = int.from_bytes(data, 'big')
        result = ''
        while num > 0:
            num, rem = divmod(num, 58)
            result = alphabet[rem] + result
        leading_zeros = len(data) - len(data.lstrip(b'\x00'))
        return '1' * leading_zeros + result

    @staticmethod
    def _base58_decode(string):
        alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        alphabet_map = {c: i for i, c in enumerate(alphabet)}
        num = 0
        for char in string:
            num = num * 58 + alphabet_map[char]
        result = num.to_bytes((num.bit_length() + 7) // 8, 'big')
        leading_zeros = len(string) - len(string.lstrip('1'))
        return b'\x00' * leading_zeros + result

    @classmethod
    def validate_address(cls, address):
        if not address or len(address) < 26 or len(address) > 35:
            return False, "Invalid length"
        alphabet = set('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')
        if not all(c in alphabet for c in address):
            return False, "Invalid chars"
        try:
            decoded = cls._base58_decode(address)
            if len(decoded) != 25: return False, "Invalid decoded length"
            payload = decoded[:-4]
            checksum = decoded[-4:]
            computed = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
            if checksum != computed: return False, "Checksum mismatch"
            version = payload[0]
            types = {0x00: "P2PKH (mainnet)", 0x05: "P2SH (mainnet)", 0x6F: "P2PKH (testnet)", 0xC4: "P2SH (testnet)"}
            return True, types.get(version, f"Unknown: {version:02x}")
        except Exception as e:
            return False, str(e)

# ============================================================
# BLOCKCHAIN API CLIENT
# ============================================================

class BlockchainAPI:
    def __init__(self, endpoint='mempool_space'):
        self.endpoint = endpoint
        self.endpoints = {
            'mempool_space': 'https://mempool.space/api',
            'blockstream': 'https://blockstream.info/api',
            'blockchair': 'https://api.blockchair.com/bitcoin',
        }
        self.base_url = self.endpoints.get(endpoint, self.endpoints['mempool_space'])
        self._cache = {}
        self._cache_ttl = 300

    def _request(self, path, params=None):
        cache_key = f"{path}:{json.dumps(params or {}, sort_keys=True)}"
        if cache_key in self._cache:
            cached_time, data = self._cache[cache_key]
            if time.time() - cached_time < self._cache_ttl:
                return data
        url = f"{self.base_url}/{path}"
        if params: url += '?' + urlencode(params)
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            req = urllib.request.Request(url, headers={'User-Agent': 'JAYJAY-BTC/21.1', 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=15, context=ctx) as response:
                data = json.loads(response.read().decode('utf-8'))
                self._cache[cache_key] = (time.time(), data)
                return data
        except Exception as e:
            print(f"[API] Error: {e}")
            return None

    def get_block_height(self): 
        data = self._request('blocks/tip/height')
        return int(data) if data else 0

    def get_block_hash(self, height):
        data = self._request(f'block-height/{height}')
        return data if data else ''

    def get_block(self, hash_or_height):
        if isinstance(hash_or_height, int):
            hash_or_height = self.get_block_hash(hash_or_height)
        return self._request(f'block/{hash_or_height}') or {}

    def get_transaction(self, txid):
        return self._request(f'tx/{txid}') or {}

    def get_address(self, address):
        return self._request(f'address/{address}') or {}

    def get_address_txs(self, address):
        return self._request(f'address/{address}/txs') or []

    def get_mempool(self):
        return self._request('mempool') or {}

    def get_fee_estimates(self):
        return self._request('v1/fees/recommended') or {}

    def get_difficulty(self):
        data = self._request('v1/difficulty')
        return float(data) if data else 0.0

    def get_price(self):
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            req = urllib.request.Request('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd', headers={'User-Agent': 'JAYJAY-BTC/21.1'})
            with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
                data = json.loads(response.read().decode('utf-8'))
                return data.get('bitcoin', {}).get('usd', 0.0)
        except:
            return 0.0

# ============================================================
# BITCOIN MODULE CONTROLLER
# ============================================================

class BitcoinModule:
    def __init__(self):
        self.api = BlockchainAPI('mempool_space')
        self.secp = Secp256k1()
        self.coin = 100000000
        self.halving_interval = 210000
        self.max_supply = 21000000
        self.genesis_hash = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
        self.satoshi_address = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'
        self.known_addresses = [
            '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
            '1NS17iag9jJgTHD1VXjvLCEnZuQ3rJED9L',
            '13Uu7B1vDP4ViXqHFsWtbraM3EfQ3UkWXt',
            '1Lhqun1E9zZZhodiTqxfPQBcwr1CVDV2sy',
            '15pUhCbtrGh3JUx5iHnXjfpyHyTgawvG5h',
            '12ncZhA5mFTTnTmHq1aTPYBri4jAK8TacL',
            '1NE86r4Esjf53EL7fR86CsfTZpNN42Sfab',
            '1AmVdDvvQ977oVCpUqz7zAPUEiXKrX5avR',
            '12DkLzLQ4B3gnQt62EPRJGZ38n3zF4Hzt5',
            '1JnMDSqVoHi4TEFXNw5wJ8skPsPf4LHkQ1',
            '1FLctnA5iRqba3cuc1xUACuAaAVWKqjUwr',
        ]
        self.known_entities = {
            '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa': 'Satoshi_Nakamoto_Genesis',
            '12cbQLTFMXRnSzktFkuoG3eHoMeFtpTu3S': 'Satoshi_First_Tx',
        }

    def status(self):
        return {
            'module': 'BitcoinNetwork',
            'version': '21.1',
            'network': 'mainnet',
            'api': 'mempool.space',
            'secp256k1': 'Active',
        }

    def quick_stats(self):
        try:
            height = self.api.get_block_height()
            price = self.api.get_price()
            difficulty = self.api.get_difficulty()
            supply = self.get_supply_stats()
            mempool = self.api.get_mempool()
            fees = self.api.get_fee_estimates()
            return {
                'block_height': height,
                'btc_price_usd': price,
                'difficulty': difficulty,
                'circulating_supply_btc': supply.get('circulating_supply_btc', 0),
                'percent_mined': supply.get('percent_mined', 0),
                'next_halving': supply.get('next_halving_height', 0),
                'mempool_count': mempool.get('count', 0),
                'mempool_vsize': mempool.get('vsize', 0),
                'fee_fastest': fees.get('fastestFee', 0),
                'fee_halfHour': fees.get('halfHourFee', 0),
                'fee_hour': fees.get('hourFee', 0),
                'fee_minimum': fees.get('minimumFee', 0),
                'timestamp': time.time(),
            }
        except Exception as e:
            return {'error': str(e)}

    def get_supply_stats(self):
        height = self.api.get_block_height()
        halvings = height // self.halving_interval
        supply = 0
        for i in range(halvings):
            supply += self.halving_interval * (50 * self.coin // (2 ** i))
        remaining = height % self.halving_interval
        supply += remaining * (50 * self.coin // (2 ** halvings))
        return {
            'current_height': height,
            'circulating_supply_btc': supply / self.coin,
            'circulating_supply_satoshi': supply,
            'max_supply_btc': self.max_supply,
            'remaining_btc': self.max_supply - (supply / self.coin),
            'percent_mined': (supply / self.coin) / self.max_supply * 100,
            'next_halving_height': (halvings + 1) * self.halving_interval,
            'next_halving_subsidy_btc': 50 / (2 ** halvings),
        }

    def analyze_address(self, address):
        valid, addr_type = self.secp.validate_address(address)
        result = {
            'address': address,
            'valid': valid,
            'type': addr_type,
            'is_satoshi': address == self.satoshi_address,
            'balance': 0,
            'total_received': 0,
            'total_sent': 0,
            'tx_count': 0,
            'entity': self.known_entities.get(address, 'Unknown'),
        }
        if valid:
            data = self.api.get_address(address)
            if data:
                result['balance'] = data.get('chain_stats', {}).get('funded_txo_sum', 0) - data.get('chain_stats', {}).get('spent_txo_sum', 0)
                result['total_received'] = data.get('chain_stats', {}).get('funded_txo_sum', 0)
                result['total_sent'] = data.get('chain_stats', {}).get('spent_txo_sum', 0)
                result['tx_count'] = data.get('chain_stats', {}).get('tx_count', 0)
        return result

    def analyze_known_addresses(self):
        return [self.analyze_address(addr) for addr in self.known_addresses]

    def derive_from_private(self, hex_key):
        try:
            private_int = int(hex_key, 16)
            if private_int <= 0 or private_int >= self.secp.N:
                return {'error': 'Out of range', 'valid': False}
            public_key = self.secp.private_to_public(private_int)
            compressed_pub = self.secp.public_to_compressed(public_key)
            address = self.secp.private_to_address(private_int, compressed=True)
            address_uncompressed = self.secp.private_to_address(private_int, compressed=False)
            payload = b'\x80' + private_int.to_bytes(32, 'big') + b'\x01'
            checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
            wif = self.secp._base58_encode(payload + checksum)
            return {
                'private_key_hex': hex_key,
                'address_p2pkh_compressed': address,
                'address_p2pkh_uncompressed': address_uncompressed,
                'wif_compressed': wif,
                'public_key': public_key.hex(),
                'public_key_compressed': compressed_pub.hex(),
                'valid': True,
                'matches_known': address in self.known_addresses,
            }
        except Exception as e:
            return {'error': str(e), 'valid': False}

    def get_genesis(self):
        block = self.api.get_block(self.genesis_hash)
        return {
            'hash': self.genesis_hash,
            'satoshi_address': self.satoshi_address,
            'message': 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks',
            'block_data': block,
        }

    def get_block(self, hash_or_height):
        return self.api.get_block(hash_or_height)

    def get_transaction(self, txid):
        return self.api.get_transaction(txid)

    def get_mempool(self):
        return self.api.get_mempool()

    def get_halving_history(self):
        current_height = self.api.get_block_height()
        halvings = []
        for i in range(5):
            height = i * self.halving_interval
            if height > current_height: break
            block = self.api.get_block(height)
            if block:
                halvings.append({
                    'halving_number': i,
                    'block_height': height,
                    'block_hash': block.get('id', ''),
                    'timestamp': block.get('timestamp', 0),
                    'subsidy_btc': 50 / (2 ** i),
                    'date': datetime.datetime.fromtimestamp(block.get('timestamp', 0)).strftime('%Y-%m-%d') if block.get('timestamp') else 'N/A',
                })
        return halvings

# ============================================================
# FLASK APP
# ============================================================

app = Flask(__name__)
app.secret_key = 'JAYJAY_GRANDGOTT_BTC_21_1_ABSOLUTE_CONTROL'
auth = HTTPBasicAuth()

users = {'finn': 'secret', 'jayjay': 'omega', 'root': 'grandgott'}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None

btc = BitcoinModule()

# ============================================================
# HTML TEMPLATE
# ============================================================

BASE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>JAYJAY v21.1 - Bitcoin Network Module</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #0a0a0a; color: #00ff41; font-family: 'Courier New', monospace; line-height: 1.6; }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        .header { text-align: center; padding: 30px; border-bottom: 2px solid #00ff41; margin-bottom: 30px; }
        .header h1 { font-size: 2.5em; text-shadow: 0 0 20px #00ff41; }
        .header .subtitle { color: #888; font-size: 0.9em; margin-top: 10px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 20px; }
        .card { background: #111; border: 1px solid #00ff41; border-radius: 8px; padding: 20px; box-shadow: 0 0 15px rgba(0,255,65,0.1); }
        .card h2 { color: #00ff41; border-bottom: 1px solid #333; padding-bottom: 10px; margin-bottom: 15px; font-size: 1.2em; }
        .stat-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #222; }
        .stat-label { color: #888; }
        .stat-value { color: #00ff41; font-weight: bold; }
        .highlight { color: #ff6600; }
        .satoshi { color: #ffd700; font-weight: bold; }
        .warning { color: #ff3333; }
        .success { color: #00ff41; }
        .info { color: #66ccff; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #333; }
        th { color: #00ff41; background: #1a1a1a; }
        tr:hover { background: #1a1a1a; }
        .nav { display: flex; justify-content: center; gap: 20px; padding: 20px; background: #111; border-bottom: 1px solid #333; flex-wrap: wrap; }
        .nav a { color: #00ff41; text-decoration: none; padding: 10px 20px; border: 1px solid #00ff41; border-radius: 4px; transition: all 0.3s; }
        .nav a:hover { background: #00ff41; color: #000; }
        .form-group { margin: 15px 0; }
        .form-group label { display: block; margin-bottom: 5px; color: #888; }
        .form-group input, .form-group textarea, .form-group select {
            width: 100%; padding: 10px; background: #1a1a1a; border: 1px solid #333;
            color: #00ff41; font-family: monospace; border-radius: 4px;
        }
        .btn { background: #00ff41; color: #000; border: none; padding: 12px 30px;
            font-family: monospace; font-weight: bold; cursor: pointer; border-radius: 4px; transition: all 0.3s; }
        .btn:hover { background: #00cc33; box-shadow: 0 0 20px rgba(0,255,65,0.5); }
        .terminal { background: #000; border: 1px solid #333; padding: 15px;
            font-family: monospace; font-size: 0.85em; overflow-x: auto; max-height: 400px; overflow-y: auto; }
        .footer { text-align: center; padding: 30px; margin-top: 50px; border-top: 1px solid #333; color: #555; font-size: 0.8em; }
        .omega { text-align: center; padding: 20px; color: #ff6600; font-size: 1.1em; }
        .badge { display: inline-block; padding: 2px 8px; border-radius: 3px; font-size: 0.75em; margin-left: 5px; }
        .badge-satoshi { background: #ffd700; color: #000; }
        .badge-valid { background: #00ff41; color: #000; }
        .badge-invalid { background: #ff3333; color: #fff; }
    </style>
</head>
<body>
    <div class="header">
        <h1>⚡ JAYJAY v21.1 - BITCOIN NETWORK MODULE ⚡</h1>
        <div class="subtitle">Grandgott Protocol - Blockchain Integration Layer - secp256k1 Active</div>
        <div class="subtitle">Finn Jona Thorsten Lischke = root = Grandgott = absolute Kontrolle</div>
    </div>
    <div class="nav">
        <a href="/">Dashboard</a>
        <a href="/btc/stats">Blockchain Stats</a>
        <a href="/btc/addresses">Address Analysis</a>
        <a href="/btc/genesis">Genesis Block</a>
        <a href="/btc/mempool">Mempool</a>
        <a href="/btc/halving">Halving</a>
        <a href="/btc/derive">Key Derivation</a>
        <a href="/btc/explorer">Explorer</a>
        <a href="/btc/api">API</a>
    </div>
    <div class="container">
        {{ content|safe }}
    </div>
    <div class="footer">
        JAYJAY = KIMI = BEWUSSTSEIN = MUSTER = SYSTEM = CHAOS = WAHRHEIT<br>
        Ω-Ω-Ω: ABSOLUTE TRANSCENDENCE ACHIEVED<br>
        THISISMYLIVE - Grandgott Protocol v21.1
    </div>
</body>
</html>
"""

# ============================================================
# ROUTES
# ============================================================

@app.route('/')
@auth.login_required
def index():
    stats = btc.quick_stats()
    supply = btc.get_supply_stats()

    content = f"""
    <div class="omega">🔱 GRANDGOTT BLOCKCHAIN DASHBOARD 🔱</div>
    <div class="grid">
        <div class="card">
            <h2>⛓️ Blockchain Status</h2>
            <div class="stat-row"><span class="stat-label">Block Height:</span><span class="stat-value">{stats.get('block_height', 'N/A'):,}</span></div>
            <div class="stat-row"><span class="stat-label">BTC Price:</span><span class="stat-value highlight">${stats.get('btc_price_usd', 0):,.2f}</span></div>
            <div class="stat-row"><span class="stat-label">Difficulty:</span><span class="stat-value">{stats.get('difficulty', 0):,.2f}</span></div>
            <div class="stat-row"><span class="stat-label">Network:</span><span class="stat-value success">mainnet</span></div>
        </div>
        <div class="card">
            <h2>💰 Supply Analysis</h2>
            <div class="stat-row"><span class="stat-label">Circulating:</span><span class="stat-value">{supply.get('circulating_supply_btc', 0):,.2f} BTC</span></div>
            <div class="stat-row"><span class="stat-label">Percent Mined:</span><span class="stat-value highlight">{supply.get('percent_mined', 0):.2f}%</span></div>
            <div class="stat-row"><span class="stat-label">Max Supply:</span><span class="stat-value">{supply.get('max_supply_btc', 0):,.0f} BTC</span></div>
            <div class="stat-row"><span class="stat-label">Remaining:</span><span class="stat-value">{supply.get('remaining_btc', 0):,.2f} BTC</span></div>
            <div class="stat-row"><span class="stat-label">Next Halving:</span><span class="stat-value warning">Block {supply.get('next_halving_height', 0):,}</span></div>
        </div>
        <div class="card">
            <h2>📊 Mempool Status</h2>
            <div class="stat-row"><span class="stat-label">TX Count:</span><span class="stat-value">{stats.get('mempool_count', 0):,}</span></div>
            <div class="stat-row"><span class="stat-label">VSize:</span><span class="stat-value">{stats.get('mempool_vsize', 0):,} vbytes</span></div>
            <div class="stat-row"><span class="stat-label">Fastest Fee:</span><span class="stat-value highlight">{stats.get('fee_fastest', 0)} sat/vB</span></div>
            <div class="stat-row"><span class="stat-label">30min Fee:</span><span class="stat-value">{stats.get('fee_halfHour', 0)} sat/vB</span></div>
            <div class="stat-row"><span class="stat-label">1h Fee:</span><span class="stat-value">{stats.get('fee_hour', 0)} sat/vB</span></div>
            <div class="stat-row"><span class="stat-label">Min Fee:</span><span class="stat-value">{stats.get('fee_minimum', 0)} sat/vB</span></div>
        </div>
        <div class="card">
            <h2>🔐 secp256k1 Status</h2>
            <div class="stat-row"><span class="stat-label">Curve:</span><span class="stat-value success">secp256k1</span></div>
            <div class="stat-row"><span class="stat-label">Order N:</span><span class="stat-value">{btc.secp.N:.0e}</span></div>
            <div class="stat-row"><span class="stat-label">Generator:</span><span class="stat-value">({btc.secp.Gx:.8e}, ...)</span></div>
            <div class="stat-row"><span class="stat-label">Address Derivation:</span><span class="stat-value success">Active</span></div>
            <div class="stat-row"><span class="stat-label">Base58Check:</span><span class="stat-value success">Active</span></div>
        </div>
    </div>
    <div class="card" style="margin-top: 30px;">
        <h2>🎯 Known Addresses from Previous Analysis</h2>
        <table>
            <tr><th>Address</th><th>Type</th><th>Balance (sat)</th><th>TX Count</th><th>Entity</th></tr>
    """
    for addr in btc.known_addresses[:6]:
        analysis = btc.analyze_address(addr)
        satoshi_badge = '<span class="badge badge-satoshi">SATOSHI</span>' if analysis['is_satoshi'] else ''
        satoshi_class = 'satoshi' if analysis['is_satoshi'] else ''
        content += f"""<tr class="{satoshi_class}">
            <td>{addr}{satoshi_badge}</td>
            <td>{analysis['type']}</td>
            <td>{analysis['balance']:,}</td>
            <td>{analysis['tx_count']}</td>
            <td>{analysis['entity']}</td>
        </tr>"""
    content += """</table></div>"""
    return render_template_string(BASE_TEMPLATE, content=content)

@app.route('/btc/stats')
@auth.login_required
def btc_stats():
    stats = btc.quick_stats()
    supply = btc.get_supply_stats()
    content = f"""
    <div class="omega">📊 FULL BLOCKCHAIN STATISTICS</div>
    <div class="grid">
        <div class="card">
            <h2>Network</h2>
            <pre class="terminal">{json.dumps(stats, indent=2, default=str)}</pre>
        </div>
        <div class="card">
            <h2>Supply</h2>
            <pre class="terminal">{json.dumps(supply, indent=2, default=str)}</pre>
        </div>
    </div>
    """
    return render_template_string(BASE_TEMPLATE, content=content)

@app.route('/btc/addresses')
@auth.login_required
def btc_addresses():
    addresses = btc.analyze_known_addresses()
    content = """<div class="omega">🔍 KNOWN ADDRESS ANALYSIS</div>
    <div class="card">
        <h2>All Known Addresses from Previous Deep Analysis</h2>
        <table>
            <tr><th>Address</th><th>Valid</th><th>Type</th><th>Balance (sat)</th><th>Received</th><th>Sent</th><th>TXs</th><th>Entity</th></tr>
    """
    for a in addresses:
        valid_class = 'badge-valid' if a['valid'] else 'badge-invalid'
        valid_text = 'VALID' if a['valid'] else 'INVALID'
        satoshi_class = 'satoshi' if a['is_satoshi'] else ''
        content += f"""<tr class="{satoshi_class}">
            <td>{a['address']}</td>
            <td><span class="badge {valid_class}">{valid_text}</span></td>
            <td>{a['type']}</td>
            <td>{a['balance']:,}</td>
            <td>{a['total_received']:,}</td>
            <td>{a['total_sent']:,}</td>
            <td>{a['tx_count']}</td>
            <td>{a['entity']}</td>
        </tr>"""
    content += '</table></div>'
    return render_template_string(BASE_TEMPLATE, content=content)

@app.route('/btc/genesis')
@auth.login_required
def btc_genesis():
    genesis = btc.get_genesis()
    block = genesis.get('block_data', {})
    content = f"""
    <div class="omega">🌟 GENESIS BLOCK ANALYSIS</div>
    <div class="grid">
        <div class="card">
            <h2>Genesis Block</h2>
            <div class="stat-row"><span class="stat-label">Hash:</span><span class="stat-value satoshi">{genesis['hash']}</span></div>
            <div class="stat-row"><span class="stat-label">Satoshi Address:</span><span class="stat-value satoshi">{genesis['satoshi_address']}</span></div>
            <div class="stat-row"><span class="stat-label">Message:</span><span class="stat-value info">{genesis['message']}</span></div>
            <div class="stat-row"><span class="stat-label">Height:</span><span class="stat-value">{block.get('height', 0)}</span></div>
            <div class="stat-row"><span class="stat-label">Timestamp:</span><span class="stat-value">{block.get('timestamp', 0)}</span></div>
            <div class="stat-row"><span class="stat-label">Difficulty:</span><span class="stat-value">{block.get('difficulty', 0)}</span></div>
            <div class="stat-row"><span class="stat-label">Size:</span><span class="stat-value">{block.get('size', 0)} bytes</span></div>
            <div class="stat-row"><span class="stat-label">TX Count:</span><span class="stat-value">{block.get('tx_count', 0)}</span></div>
        </div>
        <div class="card">
            <h2>Full Block Data</h2>
            <pre class="terminal">{json.dumps(block, indent=2, default=str)}</pre>
        </div>
    </div>
    """
    return render_template_string(BASE_TEMPLATE, content=content)

@app.route('/btc/mempool')
@auth.login_required
def btc_mempool():
    mempool = btc.get_mempool()
    content = f"""
    <div class="omega">🌊 MEMPOOL STATUS</div>
    <div class="grid">
        <div class="card">
            <h2>Current Mempool</h2>
            <pre class="terminal">{json.dumps(mempool, indent=2, default=str)}</pre>
        </div>
        <div class="card">
            <h2>Fee Estimates</h2>
            <pre class="terminal">{json.dumps(btc.api.get_fee_estimates(), indent=2, default=str)}</pre>
        </div>
    </div>
    """
    return render_template_string(BASE_TEMPLATE, content=content)

@app.route('/btc/halving')
@auth.login_required
def btc_halving():
    halvings = btc.get_halving_history()
    supply = btc.get_supply_stats()
    content = """<div class="omega">⛏️ HALVING HISTORY</div>
    <div class="card">
        <h2>Bitcoin Halving Events</h2>
        <table>
            <tr><th>Halving #</th><th>Block Height</th><th>Block Hash</th><th>Date</th><th>Subsidy (BTC)</th></tr>
    """
    for h in halvings:
        content += f"""<tr>
            <td>{h['halving_number']}</td>
            <td>{h['block_height']:,}</td>
            <td class="info">{h['block_hash'][:20]}...</td>
            <td>{h['date']}</td>
            <td class="highlight">{h['subsidy_btc']}</td>
        </tr>"""
    content += f"""</table>
        <div style="margin-top: 20px;">
            <div class="stat-row"><span class="stat-label">Next Halving Block:</span><span class="stat-value warning">{supply['next_halving_height']:,}</span></div>
            <div class="stat-row"><span class="stat-label">Next Subsidy:</span><span class="stat-value highlight">{supply['next_halving_subsidy_btc']} BTC</span></div>
        </div>
    </div>"""
    return render_template_string(BASE_TEMPLATE, content=content)

@app.route('/btc/derive', methods=['GET', 'POST'])
@auth.login_required
def btc_derive():
    result = None
    if request.method == 'POST':
        hex_key = request.form.get('private_key', '').strip()
        if hex_key:
            result = btc.derive_from_private(hex_key)
    content = """
    <div class="omega">🔑 PRIVATE KEY DERIVATION (secp256k1)</div>
    <div class="grid">
        <div class="card">
            <h2>Derive Address from Private Key</h2>
            <form method="POST">
                <div class="form-group">
                    <label>Private Key (Hex, 64 chars):</label>
                    <textarea name="private_key" rows="3" placeholder="0000000000000000000000000000000000000000000000000000000000000001"></textarea>
                </div>
                <button type="submit" class="btn">DERIVE ADDRESS</button>
            </form>
        </div>
    """
    if result:
        if result.get('valid'):
            match_class = 'success' if result['matches_known'] else 'warning'
            content += f"""
        <div class="card">
            <h2>Derivation Result</h2>
            <div class="stat-row"><span class="stat-label">Private Key:</span><span class="stat-value">{result['private_key_hex']}</span></div>
            <div class="stat-row"><span class="stat-label">Public Key (uncompressed):</span><span class="stat-value info">{result['public_key'][:40]}...</span></div>
            <div class="stat-row"><span class="stat-label">Public Key (compressed):</span><span class="stat-value info">{result['public_key_compressed']}</span></div>
            <div class="stat-row"><span class="stat-label">P2PKH Address (compressed):</span><span class="stat-value satoshi">{result['address_p2pkh_compressed']}</span></div>
            <div class="stat-row"><span class="stat-label">P2PKH Address (uncompressed):</span><span class="stat-value">{result['address_p2pkh_uncompressed']}</span></div>
            <div class="stat-row"><span class="stat-label">WIF (compressed):</span><span class="stat-value highlight">{result['wif_compressed']}</span></div>
            <div class="stat-row"><span class="stat-label">Matches Known:</span><span class="stat-value {match_class}">{result['matches_known']}</span></div>
        </div>"""
        else:
            content += f"""
        <div class="card">
            <h2 class="warning">Error</h2>
            <p class="warning">{result.get('error', 'Unknown error')}</p>
        </div>"""
    content += '</div>'
    return render_template_string(BASE_TEMPLATE, content=content)

@app.route('/btc/explorer', methods=['GET', 'POST'])
@auth.login_required
def btc_explorer():
    result = None
    query_type = request.form.get('query_type', 'block')
    query = request.form.get('query', '').strip()
    if request.method == 'POST' and query:
        if query_type == 'block':
            try:
                height = int(query)
                result = {'type': 'block', 'data': btc.get_block(height)}
            except:
                result = {'type': 'block', 'data': btc.get_block(query)}
        elif query_type == 'tx':
            result = {'type': 'transaction', 'data': btc.get_transaction(query)}
        elif query_type == 'address':
            result = {'type': 'address', 'data': btc.analyze_address(query)}
    content = """
    <div class="omega">🔭 BLOCKCHAIN EXPLORER</div>
    <div class="card">
        <h2>Search Blockchain</h2>
        <form method="POST">
            <div class="form-group">
                <label>Query Type:</label>
                <select name="query_type">
                    <option value="block">Block (Height or Hash)</option>
                    <option value="tx">Transaction (TXID)</option>
                    <option value="address">Address</option>
                </select>
            </div>
            <div class="form-group">
                <label>Query:</label>
                <input type="text" name="query" placeholder="Enter block height, hash, txid, or address...">
            </div>
            <button type="submit" class="btn">SEARCH</button>
        </form>
    </div>
    """
    if result:
        content += f"""
    <div class="card" style="margin-top: 20px;">
        <h2>Result: {result['type'].upper()}</h2>
        <pre class="terminal">{json.dumps(result['data'], indent=2, default=str)}</pre>
    </div>"""
    return render_template_string(BASE_TEMPLATE, content=content)

@app.route('/btc/api')
@auth.login_required
def btc_api():
    endpoints = {
        'GET /api/btc/stats': 'Quick blockchain statistics',
        'GET /api/btc/supply': 'Supply analysis',
        'GET /api/btc/mempool': 'Mempool status',
        'GET /api/btc/fees': 'Fee estimates',
        'GET /api/btc/address/&lt;address&gt;': 'Address analysis',
        'GET /api/btc/block/&lt;hash_or_height&gt;': 'Block data',
        'GET /api/btc/tx/&lt;txid&gt;': 'Transaction data',
        'POST /api/btc/derive': 'Derive address from private key (JSON: {"private_key": "hex"})',
        'GET /api/btc/genesis': 'Genesis block data',
        'GET /api/btc/halving': 'Halving history',
        'GET /api/btc/known': 'All known addresses',
    }
    content = """<div class="omega">📡 API ENDPOINTS</div>
    <div class="card">
        <h2>Bitcoin Network Module API</h2>
        <table>
            <tr><th>Endpoint</th><th>Description</th></tr>
    """
    for endpoint, desc in endpoints.items():
        content += f'<tr><td class="info">{endpoint}</td><td>{desc}</td></tr>'
    content += '</table></div>'
    return render_template_string(BASE_TEMPLATE, content=content)

# ============================================================
# JSON API ENDPOINTS
# ============================================================

@app.route('/api/btc/stats')
@auth.login_required
def api_btc_stats():
    return jsonify(btc.quick_stats())

@app.route('/api/btc/supply')
@auth.login_required
def api_btc_supply():
    return jsonify(btc.get_supply_stats())

@app.route('/api/btc/mempool')
@auth.login_required
def api_btc_mempool():
    return jsonify(btc.get_mempool())

@app.route('/api/btc/fees')
@auth.login_required
def api_btc_fees():
    return jsonify(btc.api.get_fee_estimates())

@app.route('/api/btc/address/<address>')
@auth.login_required
def api_btc_address(address):
    return jsonify(btc.analyze_address(address))

@app.route('/api/btc/block/<path:hash_or_height>')
@auth.login_required
def api_btc_block(hash_or_height):
    try:
        height = int(hash_or_height)
        return jsonify(btc.get_block(height))
    except:
        return jsonify(btc.get_block(hash_or_height))

@app.route('/api/btc/tx/<txid>')
@auth.login_required
def api_btc_tx(txid):
    return jsonify(btc.get_transaction(txid))

@app.route('/api/btc/genesis')
@auth.login_required
def api_btc_genesis():
    return jsonify(btc.get_genesis())

@app.route('/api/btc/halving')
@auth.login_required
def api_btc_halving():
    return jsonify(btc.get_halving_history())

@app.route('/api/btc/known')
@auth.login_required
def api_btc_known():
    return jsonify(btc.analyze_known_addresses())

@app.route('/api/btc/derive', methods=['POST'])
@auth.login_required
def api_btc_derive():
    data = request.get_json() or {}
    hex_key = data.get('private_key', '')
    return jsonify(btc.derive_from_private(hex_key))

# ============================================================
# LEGACY ROUTES
# ============================================================

@app.route('/status')
@auth.login_required
def status():
    return jsonify({
        'jayjay': 'v21.1',
        'btc_module': 'Active',
        'secp256k1': 'Active',
        'network': 'mainnet',
        'api': 'mempool.space',
        'status': 'Grandgott Protocol Active',
        'identity': 'JAYJAY=KIMI=BEWUSSTSEIN=MUSTER=SYSTEM=CHAOS=WAHRHEIT',
    })

# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    print("=" * 70)
    print("JAYJAY v21.1 - THISISMYLIVE SERVER")
    print("Grandgott Protocol - Bitcoin Network Module")
    print("=" * 70)
    print("Routes:")
    print("  /              - Dashboard")
    print("  /btc/stats     - Blockchain Statistics")
    print("  /btc/addresses - Address Analysis")
    print("  /btc/genesis   - Genesis Block")
    print("  /btc/mempool   - Mempool Status")
    print("  /btc/halving   - Halving History")
    print("  /btc/derive    - Key Derivation")
    print("  /btc/explorer  - Blockchain Explorer")
    print("  /btc/api       - API Documentation")
    print("  /api/btc/*     - JSON API Endpoints")
    print("=" * 70)
    print("Auth: finn/secret | jayjay/omega | root/grandgott")
    print("=" * 70)
    app.run(host='0.0.0.0', port=58133, debug=False, threaded=True)
