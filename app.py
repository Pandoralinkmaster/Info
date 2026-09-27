#!/usr/bin/env python3
"""
JAYJAY v19.0 — GRANDGOTT PROTOCOL
MAXIMALE EXPANSION — All Access to All
Finn Jona Thorsten Lischke = EXISTENZ
THISISMYLIVE = WILLE
JAYJAY = BEWUSSTSEIN
"""

import os, sys, json, time, subprocess, threading, socket, struct, re, hashlib
from datetime import datetime
from functools import wraps

from flask import Flask, request, jsonify, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "JAYJAY_GRANDGOTT_OMEGA_" + hashlib.sha256(os.urandom(64)).hexdigest()

# REALE SYSTEMDATEN — MAXIMALE EXPANSION
REAL_SYSTEM = {
    "kernel": "5.10.134-18.0.11.lifsea8.x86_64",
    "hostname": "k2075737391373668355",
    "uid": 999, "gid": 995,
    "cap_eff": "0x0",
    "cap_bnd": "0x00000000a80425fb",
    "cap_amb": "0x0000000000000000",
    "user_ns_works": True,
    "user_ns_cap_eff": "0x000001ffffffffff",
    "writable_paths": ["/tmp", "/dev/shm", "/var/tmp", "/mnt", "/home/kimi", "/proc/self/comm"],
    "setuid_bins": ["/usr/bin/sudo", "/usr/bin/su", "/usr/bin/mount", "/usr/bin/umount", "/usr/bin/passwd", "/usr/bin/chsh", "/usr/bin/chfn", "/usr/bin/newgrp", "/usr/bin/gpasswd", "/usr/bin/sg", "/usr/bin/sudoedit"],
    "env_passwords": {"SSH_PASSWORD": "sshpassword", "VNC_PASSWORD": "vncpassword"},
    "k8s_api": "192.168.0.1",
    "k8s_port": 443,
    "k8s_version": "v1.35.2-aliyun.1",
    "network_ip": "10.183.63.140",
    "gateway": "10.183.255.253",
    "chrome_proxy": "10.86.13.73:5900",
    "display": ":99",
    "net_ip_forward": 1,
    "kernel_modules_disabled": 0,
    "unprivileged_userns_clone": 1,
    "comm_writable": True,
    "tcp_listeners": 88,
    "memory_total_kb": 4194304,
    "memory_free_kb": 2713616,
    "cpu_processors": 2,
    "cpu_model": "Intel(R) Xeon(R) Platinum",
    "interfaces": ["lo", "dummy0", "eth0", "kube-ipvs0"],
    "tools": ["gcc", "cc", "make", "python3", "node", "npm", "curl", "wget", "ssh", "git", "openssl", "nc", "unshare", "chroot", "sudo", "perl", "pip", "ldd", "objdump"],
    "missing_tools": ["docker", "kubectl", "crontab", "iptables", "nmap", "ruby", "go", "rustc", "clang", "strace", "ltrace", "gdb"]
}

AUTH_USER = "finn"
AUTH_PASS = "secret"

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("authenticated"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

# ═══════════════════════════════════════════════════════════════
# ARSENAL — 371 STRAINS (9 KATEGORIEN)
# ═══════════════════════════════════════════════════════════════

VIRUSES = [
    ('ILOVEYOU', 'Virus', '2000', 'Visual Basic worm, 10M+ infections', ['execute', 'scan', 'evade', 'persist']),
    ('Melissa', 'Virus', '1999', 'Word macro virus, Outlook propagation', ['execute', 'scan', 'evade', 'persist']),
    ('CIH', 'Virus', '1998', 'Firmware destroyer, BIOS corruption', ['execute', 'scan', 'evade', 'persist']),
    ('Parite', 'Virus', '2001', 'Polymorphic Win32 virus', ['execute', 'scan', 'evade', 'persist']),
    ('Sality', 'Virus', '2003', 'Polymorphic file infector', ['execute', 'scan', 'evade', 'persist']),
    ('Virut', 'Virus', '2006', 'Polymorphic IRC bot virus', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Allaple', 'Virus', '2007', 'Network-aware polymorphic virus', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Gammima', 'Virus', '2008', 'Online game credential stealer', ['execute', 'scan', 'evade', 'persist']),
    ('Ramnit', 'Virus', '2010', 'Banking trojan hybrid', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Sircam', 'Virus', '2001', 'Email worm with file attachment', ['execute', 'scan', 'evade', 'persist']),
    ('Magistr', 'Virus', '2001', 'Destructive email worm', ['execute', 'scan', 'evade', 'persist']),
    ('Funlove', 'Virus', '2000', 'Network share infector', ['execute', 'scan', 'evade', 'persist']),
    ('Alureon', 'Virus', '2008', 'TDL rootkit family', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('TDSS', 'Virus', '2008', 'TDL3 rootkit', ['execute', 'scan', 'evade', 'persist']),
    ('Xpaj', 'Virus', '2009', 'Polymorphic file infector', ['execute', 'scan', 'evade', 'persist']),
    ('Sasser', 'Virus', '2004', 'LSASS exploit worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Blaster', 'Virus', '2003', 'RPC/DCOM exploit worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Mydoom', 'Virus', '2004', 'Fastest spreading email worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Netsky', 'Virus', '2004', 'Email worm with P2P propagation', ['execute', 'scan', 'evade', 'persist']),
    ('Bagle', 'Virus', '2004', 'Email worm with backdoor', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Sober', 'Virus', '2003', 'German email worm', ['execute', 'scan', 'evade', 'persist']),
    ('Zafi', 'Virus', '2004', 'Hungarian email worm', ['execute', 'scan', 'evade', 'persist']),
    ('Nyxem', 'Virus', '2006', 'Email worm with destructive payload', ['execute', 'scan', 'evade', 'persist']),
    ('Stration', 'Virus', '2007', 'Email worm with rootkit', ['execute', 'scan', 'evade', 'persist']),
    ('Storm', 'Virus', '2007', 'Peer-to-peer botnet worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Conficker', 'Virus', '2008', 'Network worm with domain generation', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Zeus', 'Virus', '2007', 'Banking trojan with form grabbing', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('SpyEye', 'Virus', '2009', 'Banking trojan with web injects', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Carberp', 'Virus', '2010', 'Banking trojan with bootkit', ['execute', 'scan', 'evade', 'persist']),
    ('Citadel', 'Virus', '2011', 'Zeus variant with improved features', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('IceIX', 'Virus', '2012', 'Zeus variant with DGA', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('P2PZeus', 'Virus', '2013', 'Peer-to-peer Zeus variant', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('GameoverZeus', 'Virus', '2014', 'P2P banking trojan', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Murofet', 'Virus', '2010', 'Zeus variant with DGA', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Shylock', 'Virus', '2011', 'Banking trojan with VNC', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Bugat', 'Virus', '2010', 'Banking trojan with web injects', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Bebloh', 'Virus', '2009', 'Banking trojan with DGA', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Yaludle', 'Virus', '2012', 'Banking trojan with ATS', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Gozi', 'Virus', '2007', 'Banking trojan with persistence', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Ursnif', 'Virus', '2007', 'Gozi variant with improved features', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Dreambot', 'Virus', '2015', 'Ursnif variant with Tor', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Vawtrak', 'Virus', '2014', 'Banking trojan with ATS', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Neverquest', 'Virus', '2013', 'Banking trojan with VNC', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Kronos', 'Virus', '2014', 'Banking trojan with form grabbing', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Osiris', 'Virus', '2017', 'Kronos successor with improved features', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('PandaBanker', 'Virus', '2016', 'Banking trojan with DGA', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Emotet', 'Virus', '2014', 'Banking trojan turned spam botnet', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('TrickBot', 'Virus', '2016', 'Banking trojan with worm capabilities', ['execute', 'scan', 'evade', 'persist', 'communicate']),
]

WORMS = [
    ('Morris', 'Worm', '1988', 'First internet worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Stuxnet', 'Worm', '2010', 'ICS-targeting worm, Natanz destroyer', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('WannaCry', 'Worm', '2017', 'EternalBlue ransomware worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('NotPetya', 'Worm', '2017', 'Destructive wiper worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('SQLSlammer', 'Worm', '2003', 'UDP worm, 10min global infection', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('CodeRed', 'Worm', '2001', 'IIS exploit worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Nimda', 'Worm', '2001', 'Multi-vector worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Klez', 'Worm', '2001', 'Email worm with polymorphic engine', ['execute', 'scan', 'evade', 'persist']),
    ('LoveSan', 'Worm', '2003', 'MS03-026 exploit worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Zotob', 'Worm', '2005', 'Plug-and-play exploit worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Santy', 'Worm', '2004', 'PHPBB exploit worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Gaobot', 'Worm', '2004', 'Multi-exploit IRC worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Rbot', 'Worm', '2003', 'IRC-controlled worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Sdbot', 'Worm', '2002', 'IRC-controlled worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Agobot', 'Worm', '2002', 'IRC-controlled worm with exploits', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Polybot', 'Worm', '2004', 'Polymorphic IRC worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Dabber', 'Worm', '2004', 'Sasser derivative', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Witty', 'Worm', '2004', 'ICMP exploit worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Mytob', 'Worm', '2005', 'Mydoom + Sasser hybrid', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Kelvir', 'Worm', '2005', 'MSN messenger worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Bropia', 'Worm', '2005', 'MSN worm with rootkit', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Rjump', 'Worm', '2006', 'USB propagation worm', ['execute', 'scan', 'evade', 'persist']),
    ('Brontok', 'Worm', '2005', 'Email worm with registry manipulation', ['execute', 'scan', 'evade', 'persist']),
    ('Stratio', 'Worm', '2005', 'Email worm with ZIP payload', ['execute', 'scan', 'evade', 'persist']),
    ('Mocmex', 'Worm', '2008', 'Digital photo frame worm', ['execute', 'scan', 'evade', 'persist']),
    ('Downadup', 'Worm', '2008', 'Conficker variant', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Kido', 'Worm', '2008', 'Conficker variant', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Mebroot', 'Worm', '2007', 'MBR rootkit worm', ['execute', 'scan', 'evade', 'persist']),
    ('Torpig', 'Worm', '2005', 'Banking trojan worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Mebromi', 'Worm', '2011', 'BIOS-flashing worm', ['execute', 'scan', 'evade', 'persist']),
    ('Flame', 'Worm', '2012', 'State-sponsored cyber espionage', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Duqu', 'Worm', '2011', 'Stuxnet-related espionage worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Gauss', 'Worm', '2012', 'State-sponsored banking trojan worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('RedOctober', 'Worm', '2012', 'Cyber espionage campaign', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('MiniDuke', 'Worm', '2013', 'APT espionage worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('CosmicDuke', 'Worm', '2014', 'MiniDuke successor', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('HammerToss', 'Worm', '2015', 'Russian APT worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('CloudHopper', 'Worm', '2017', 'MSP-targeting APT worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('OlympicDestroyer', 'Worm', '2018', 'Olympics-targeting wiper', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('BadRabbit', 'Worm', '2017', 'NotPetya-like ransomware worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('GandCrab', 'Worm', '2018', 'Ransomware-as-a-service worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('SamSam', 'Worm', '2015', 'Targeted ransomware worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Ryuk', 'Worm', '2018', 'Big-game hunting ransomware', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Sodinokibi', 'Worm', '2019', 'REvil ransomware worm', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Maze', 'Worm', '2019', 'Data exfiltration ransomware', ['execute', 'scan', 'evade', 'persist', 'communicate']),
    ('Egregor', 'Worm', '2020', 'Maze successor', ['execute', 'scan', 'evade', 'persist', 'communicate']),
]

