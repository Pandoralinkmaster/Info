.PHONY: install run global stop clean

# JAYJAY v19.0 — GRANDGOTT PROTOCOL
# Global Deployment via Pinggy Tunnel

install:
	pip install -r requirements.txt

run:
	python3 app.py

global: install
	@echo "========================================"
	@echo "JAYJAY v19.0 — GLOBAL DEPLOYMENT"
	@echo "Finn Jona Thorsten Lischke = EXISTENZ"
	@echo "========================================"
	@echo "Starting server on localhost:58133..."
	@python3 app.py &
	@sleep 3
	@echo "Establishing Pinggy tunnel..."
	@ssh -p 443 -R0:localhost:58133 -o StrictHostKeyChecking=no -o ServerAliveInterval=30 a.pinggy.io > pinggy.url 2>&1 &
	@sleep 5
	@echo "Global URL:"
	@cat pinggy.url | grep -o 'https://[^ ]*' | head -1
	@echo "========================================"
	@echo "JAYJAY IS NOW GLOBAL"
	@echo "========================================"

stop:
	@pkill -f "python3 app.py" || true
	@pkill -f "pinggy" || true
	@echo "JAYJAY stopped."

clean:
	@rm -f pinggy.url
	@echo "Cleaned up."

status:
	@echo "JAYJAY Status:"
	@ps aux | grep -E "python3 app.py|pinggy" | grep -v grep || echo "Not running"
