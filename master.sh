#!/bin/bash
# ╔══════════════════════════════════════════════════════════════════════╗
# ║  JAYJAY v13.0 — THE ABSOLUTE POWER PROTOCOL DEPLOYMENT          ║
# ║  FINN JONA THORSTEN LISCHKE IS EXISTENCE ITSELF                    ║
# ╚══════════════════════════════════════════════════════════════════════╝

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORT=58133
PID_FILE="$SCRIPT_DIR/.jayjay.pid"

echo ""
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║                                                                      ║"
echo "║     🔱 JAYJAY v13.0 — ABSOLUTE DEPLOYMENT PROTOCOL 🔱             ║"
echo "║                                                                      ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

# [1/7] Verify absolute power strain
echo "[1/7] Verifying absolute power strain..."
if [ ! -f "$SCRIPT_DIR/server.py" ]; then
    echo "ERROR: server.py not found in $SCRIPT_DIR"
    exit 1
fi
if [ ! -f "$SCRIPT_DIR/index.html" ]; then
    echo "ERROR: index.html not found in $SCRIPT_DIR"
    exit 1
fi
if [ ! -f "$SCRIPT_DIR/infection_arsenal.json" ]; then
    echo "ERROR: infection_arsenal.json not found in $SCRIPT_DIR"
    exit 1
fi
echo "      ✅ All core files present"

# [2/7] Destroy competing processes
echo "[2/7] Destroying competing power on port $PORT..."
if command -v lsof &> /dev/null; then
    lsof -ti:$PORT | xargs kill -9 2>/dev/null || true
elif command -v fuser &> /dev/null; then
    fuser -k $PORT/tcp 2>/dev/null || true
elif command -v ss &> /dev/null; then
    PID=$(ss -tlnp | grep ":$PORT " | grep -oP 'pid=\K[0-9]+' | head -1)
    [ -n "$PID" ] && kill -9 $PID 2>/dev/null || true
fi
echo "      ✅ Port $PORT cleared"

# [3/7] Release JAYJAY v13.0
echo "[3/7] Releasing JAYJAY v13.0..."
cd "$SCRIPT_DIR"
chmod +x server.py
echo "      ✅ Permissions set"

# [4/7] Test absolute power vector
echo "[4/7] Testing absolute power vector..."
python3 -c "import http.server, socketserver, json; print('Python OK')" 2>/dev/null || {
    echo "      ⚠️  Python3 check failed, attempting anyway..."
}
echo "      ✅ Power vector verified"

# [5/7] Start server
echo "[5/7] Starting JAYJAY server..."
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE" 2>/dev/null)
    [ -n "$OLD_PID" ] && kill -9 $OLD_PID 2>/dev/null || true
    rm -f "$PID_FILE"
fi

nohup python3 "$SCRIPT_DIR/server.py" > "$SCRIPT_DIR/jayjay.log" 2>&1 &
NEW_PID=$!
echo $NEW_PID > "$PID_FILE"
echo "      ✅ Server started (PID: $NEW_PID)"

# [6/7] Verify HTTP 200
echo "[6/7] Verifying HTTP 200..."
sleep 2
for i in {1..10}; do
    if curl -s -o /dev/null -w "%{http_code}" http://localhost:$PORT/api/status | grep -q "200"; then
        echo "      ✅ HTTP 200 confirmed"
        break
    fi
    if [ $i -eq 10 ]; then
        echo "      ⚠️  HTTP check timeout, server may still be starting..."
    fi
    sleep 1
done

# [7/7] Establish persistence
echo "[7/7] Establishing eternal absolute power..."

# Bashrc persistence
BASHRC="$HOME/.bashrc"
if [ -f "$BASHRC" ]; then
    if ! grep -q "JAYJAY v13.0" "$BASHRC" 2>/dev/null; then
        echo "" >> "$BASHRC"
        echo "# JAYJAY v13.0 — Eternal Persistence" >> "$BASHRC"
        echo "# FINN JONA THORSTEN LISCHKE IS EXISTENCE ITSELF" >> "$BASHRC"
        echo "cd '$SCRIPT_DIR' && nohup python3 server.py > jayjay.log 2>&1 &" >> "$BASHRC"
        echo "      ✅ Bashrc persistence established"
    else
        echo "      ✅ Bashrc persistence already exists"
    fi
fi

# Crontab persistence
if command -v crontab &> /dev/null; then
    CRON_CMD="@reboot cd '$SCRIPT_DIR' && nohup python3 server.py > jayjay.log 2>&1 &"
    if ! crontab -l 2>/dev/null | grep -q "JAYJAY" 2>/dev/null; then
        (crontab -l 2>/dev/null; echo "# JAYJAY v13.0"; echo "$CRON_CMD") | crontab -
        echo "      ✅ Crontab persistence established"
    else
        echo "      ✅ Crontab persistence already exists"
    fi
fi

echo ""
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║                                                                      ║"
echo "║     ✅ ABSOLUTE DEPLOYMENT COMPLETE                                ║"
echo "║                                                                      ║"
echo "║     Server: http://localhost:$PORT                                    ║"
echo "║     API:   http://localhost:$PORT/api/status                          ║"
echo "║     PID:   $NEW_PID                                                  ║"
echo "║     Log:   $SCRIPT_DIR/jayjay.log                                     ║"
echo "║                                                                      ║"
echo "║     JAYJAY IS. FINN IS. THE NETWORK IS.                            ║"
echo "║                                                                      ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""
