#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  FlowState Next & Project Alpha Quick Start    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════╝${NC}\n"

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo -e "${RED}✗ Node.js is not installed${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Node.js found: $(node -v)${NC}\n"

# Function to start a service
start_service() {
    local service=$1
    local port=$2
    local command=$3
    
    echo -e "${YELLOW}Starting ${service}...${NC}"
    
    if [ ! -d "$service" ]; then
        echo -e "${RED}✗ Directory '$service' not found${NC}"
        return 1
    fi
    
    cd "$service"
    
    if [ ! -d "node_modules" ]; then
        echo -e "${YELLOW}Installing dependencies...${NC}"
        npm install
    fi
    
    echo -e "${GREEN}✓ ${service} ready on port ${port}${NC}"
    eval "$command" &
    
    cd ..
    sleep 2
}

# Start Backend
start_service "alpha-backend" "58133" "npm start"

# Start Frontend
start_service "flowstate-next" "5173" "npm run dev"

echo -e "\n${GREEN}╔════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  Services are running:                         ║${NC}"
echo -e "${GREEN}║  Backend:  http://localhost:58133              ║${NC}"
echo -e "${GREEN}║  Frontend: http://localhost:5173               ║${NC}"
echo -e "${GREEN}║  Credentials: admin / password                 ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════╝${NC}\n"

echo -e "${YELLOW}Press Ctrl+C to stop all services${NC}"

# Wait for all background processes
wait
