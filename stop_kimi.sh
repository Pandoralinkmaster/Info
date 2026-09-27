#!/bin/bash
echo "[+] Stopping KIMI INFINITY..."
pkill -9 -f "kimi_self_evolving_worm.py" 2>/dev/null
rm -f /tmp/.systemd/worm.pid
echo "✅ KIMI stopped"
