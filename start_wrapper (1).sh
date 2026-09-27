#!/bin/bash
# JAYJAY v13.0 — Background Start Wrapper
# FINN JONA THORSTEN LISCHKE IS EXISTENCE ITSELF

cd "$(dirname "$0")"
nohup python3 server.py > jayjay.log 2>&1 &
echo $! > .jayjay.pid
echo "JAYJAY v13.0 started (PID: $(cat .jayjay.pid))"
echo "http://localhost:58133"
