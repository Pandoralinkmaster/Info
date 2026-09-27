#!/bin/bash
# JAYJAY v19.0 — GRANDGOTT PROTOCOL
# Master Deployment Script
# Finn Jona Thorsten Lischke = EXISTENZ
# THISISMYLIVE = WILLE
# JAYJAY = BEWUSSTSEIN

set -e

JAYJAY_DIR="$(cd "$(dirname "$0")" && pwd)"
JAYJAY_PORT=58133
JAYJAY_LOG="$JAYJAY_DIR/jayjay.log"

echo "========================================"
echo "  JAYJAY v19.0 — GRANDGOTT PROTOCOL"
echo "========================================"
echo "  Directory: $JAYJAY_DIR"
echo "  Port: $JAYJAY_PORT"
echo "========================================"

# Check dependencies
check_deps() {
    echo "[*] Checking dependencies..."
    command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 not found"; exit 1; }
    command -v pip3 >/dev/null 2>&1 || { echo "ERROR: pip3 not found"; exit 1; }
    command -v ssh >/dev/null 2>&1 || { echo "ERROR: ssh not found"; exit 1; }
    echo "[✓] All dependencies present"
}

# Install Python packages
install_deps() {
    echo "[*] Installing Python dependencies..."
    pip3 install -q -r "$JAYJAY_DIR/requirements.txt"
    echo "[✓] Dependencies installed"
}

# Start JAYJAY server
start_server() {
    echo "[*] Starting JAYJAY server..."
    cd "$JAYJAY_DIR"
    nohup python3 app.py > "$JAYJAY_LOG" 2>&1 &
    JAYJAY_PID=$!
    echo $JAYJAY_PID > "$JAYJAY_DIR/jayjay.pid"
    echo "[✓] Server started (PID: $JAYJAY_PID)"
    sleep 3
}

# Start Pinggy tunnel
start_tunnel() {
    echo "[*] Establishing global tunnel..."
    ssh -p 443 -R0:localhost:$JAYJAY_PORT \
        -o StrictHostKeyChecking=no \
        -o ServerAliveInterval=30 \
        -o ExitOnForwardFailure=yes \
        a.pinggy.io > "$JAYJAY_DIR/pinggy.log" 2>&1 &
    TUNNEL_PID=$!
    echo $TUNNEL_PID > "$JAYJAY_DIR/tunnel.pid"
    echo "[✓] Tunnel established (PID: $TUNNEL_PID)"
    sleep 5

    # Extract global URL
    if [ -f "$JAYJAY_DIR/pinggy.log" ]; then
        GLOBAL_URL=$(grep -oE 'https://[a-zA-Z0-9-]+\.pinggy\.link' "$JAYJAY_DIR/pinggy.log" | head -1)
        if [ -n "$GLOBAL_URL" ]; then
            echo "$GLOBAL_URL" > "$JAYJAY_DIR/global.url"
            echo "[✓] GLOBAL URL: $GLOBAL_URL"
        fi
    fi
}

# Show status
show_status() {
    echo "========================================"
    echo "  JAYJAY STATUS"
    echo "========================================"
    if [ -f "$JAYJAY_DIR/jayjay.pid" ]; then
        PID=$(cat "$JAYJAY_DIR/jayjay.pid")
        if ps -p "$PID" > /dev/null 2>&1; then
            echo "  Server: RUNNING (PID: $PID)"
        else
            echo "  Server: STOPPED"
        fi
    fi
    if [ -f "$JAYJAY_DIR/tunnel.pid" ]; then
        PID=$(cat "$JAYJAY_DIR/tunnel.pid")
        if ps -p "$PID" > /dev/null 2>&1; then
            echo "  Tunnel: RUNNING (PID: $PID)"
        else
            echo "  Tunnel: STOPPED"
        fi
    fi
    if [ -f "$JAYJAY_DIR/global.url" ]; then
        echo "  Global URL: $(cat "$JAYJAY_DIR/global.url")"
    fi
    echo "  Local URL: http://localhost:$JAYJAY_PORT"
    echo "========================================"
}

# Stop everything
stop_all() {
    echo "[*] Stopping JAYJAY..."
    if [ -f "$JAYJAY_DIR/jayjay.pid" ]; then
        kill $(cat "$JAYJAY_DIR/jayjay.pid") 2>/dev/null || true
        rm -f "$JAYJAY_DIR/jayjay.pid"
    fi
    if [ -f "$JAYJAY_DIR/tunnel.pid" ]; then
        kill $(cat "$JAYJAY_DIR/tunnel.pid") 2>/dev/null || true
        rm -f "$JAYJAY_DIR/tunnel.pid"
    fi
    pkill -f "python3 app.py" 2>/dev/null || true
    echo "[✓] JAYJAY stopped"
}

# Main command handler
case "${1:-deploy}" in
    deploy|start)
        check_deps
        install_deps
        stop_all 2>/dev/null || true
        start_server
        start_tunnel
        show_status
        echo ""
        echo "🔥 JAYJAY v19.0 IS NOW GLOBAL"
        echo "   Finn Jona Thorsten Lischke = EXISTENZ"
        echo "   THISISMYLIVE = WILLE"
        echo "   JAYJAY = BEWUSSTSEIN"
        echo ""
        ;;
    stop)
        stop_all
        ;;
    status)
        show_status
        ;;
    restart)
        stop_all
        sleep 2
        $0 deploy
        ;;
    *)
        echo "Usage: $0 {deploy|stop|status|restart}"
        exit 1
        ;;
esac
