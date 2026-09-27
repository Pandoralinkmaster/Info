# Project Alpha API Reference

## Übersicht

Die Project Alpha API ist eine RESTful API mit Basic Authentication. Alle Requests müssen mit einem `Authorization` Header versehen sein.

**Base URL:** `http://localhost:58133`

**Authentication:** Basic Auth (admin/password)

---

## Authentication

### Basic Auth Header
```bash
Authorization: Basic YWRtaW46cGFzc3dvcmQ=
```

### cURL Beispiel
```bash
curl -u admin:password http://localhost:58133/api/engine/status
```

---

## Endpoints

### 1. Engine Status
Ruft den aktuellen Status der Project Alpha Engine ab.

**Request:**
```http
GET /api/engine/status
Authorization: Basic admin:password
```

**cURL:**
```bash
curl -u admin:password http://localhost:58133/api/engine/status
```

**Response (200 OK):**
```json
{
  "ver": "7.0.4-LTS",
  "gen": 1242,
  "mut": 89,
  "conf": 98.4,
  "stat": "OPTIMAL",
  "dna": "ALPHA-X99-PRO-8822-CORE-STABLE",
  "sys": "Linux 6.2.0-33-generic",
  "inst": 12,
  "nodes": 3,
  "devs": 5,
  "vcount": 13,
  "vecs": ["NETWORK", "STORAGE", "AI-CORE"],
  "eh": 1,
  "rl": 0,
  "rpl": 0,
  "upf": "14d 06h 22m"
}
```

**Fields:**
- `ver`: Engine Version
- `gen`: Generation Number
- `mut`: Mutation Count
- `conf`: Confidence Level (%)
- `stat`: Status (OPTIMAL, RUNNING, IDLE)
- `dna`: DNA Identifier
- `sys`: System Info
- `inst`: Instances
- `nodes`: Connected Nodes
- `devs`: Devices
- `vcount`: Vector Count
- `vecs`: Vector Types
- `upf`: Uptime Format

---

### 2. Mobile Nodes
Ruft alle registrierten Mobile Nodes ab.

**Request:**
```http
GET /api/mobile/nodes
Authorization: Basic admin:password
```

**cURL:**
```bash
curl -u admin:password http://localhost:58133/api/mobile/nodes
```

**Response (200 OK):**
```json
{
  "nodes": [
    {
      "id": "NODE-01",
      "type": "Gateway",
      "ts": "2026-07-03T20:30:00Z"
    },
    {
      "id": "NODE-02",
      "type": "Sensor",
      "ts": "2026-07-03T20:30:00Z"
    }
  ]
}
```

---

### 3. Security Catalog
Ruft den Security Catalog mit verfügbaren Tools ab.

**Request:**
```http
GET /api/security/catalog
Authorization: Basic admin:password
```

**cURL:**
```bash
curl -u admin:password http://localhost:58133/api/security/catalog
```

**Response (200 OK):**
```json
{
  "total": 115,
  "cats": [
    "Exploits",
    "Implants",
    "Payloads",
    "Utilities",
    "Frameworks"
  ],
  "note": [
    "All tools active",
    "Version 2.0",
    "Zero-Trust enabled"
  ],
  "stat": "SECURE",
  "int": "NONE"
}
```

---

### 4. Register Device
Registriert ein neues Mobile Device.

**Request:**
```http
POST /api/mobile/register
Authorization: Basic admin:password
Content-Type: application/json

{
  "id": "NODE-04",
  "type": "Relay"
}
```

**cURL:**
```bash
curl -X POST -u admin:password \
  -H "Content-Type: application/json" \
  -d '{"id":"NODE-04","type":"Relay"}' \
  http://localhost:58133/api/mobile/register
```

**Response (200 OK):**
```json
{
  "reg": true,
  "device": {
    "id": "NODE-04",
    "type": "Relay",
    "ts": "2026-07-03T20:35:00Z"
  }
}
```

**Error (400 Bad Request):**
```json
{
  "error": "Missing id or type"
}
```

---

### 5. Execute Command
Führt einen Befehl auf der Engine aus.

**Request:**
```http
POST /api/engine/execute
Authorization: Basic admin:password
Content-Type: application/json

{
  "cmd": "evolve"
}
```

**cURL:**
```bash
curl -X POST -u admin:password \
  -H "Content-Type: application/json" \
  -d '{"cmd":"evolve"}' \
  http://localhost:58133/api/engine/execute
```

**Response (200 OK):**
```json
{
  "result": "Command 'evolve' executed successfully on Project Alpha Engine.",
  "status": "SUCCESS"
}
```

**Supported Commands:**
- `evolve` - Evolution starten
- `recognize` - Pattern Recognition
- `replicate` - Replikation
- Custom commands

---

### 6. Engine Evolve
Startet den Evolution-Prozess.

**Request:**
```http
POST /api/engine/evolve
Authorization: Basic admin:password
```

**cURL:**
```bash
curl -X POST -u admin:password \
  http://localhost:58133/api/engine/evolve
```

**Response (200 OK):**
```json
{
  "result": "Evolution triggered. New generation: 1267",
  "generation": 1267,
  "status": "SUCCESS"
}
```

---

### 7. Engine Recognize
Führt Pattern Recognition durch.

**Request:**
```http
POST /api/engine/recognize
Authorization: Basic admin:password
```

**cURL:**
```bash
curl -X POST -u admin:password \
  http://localhost:58133/api/engine/recognize
```

**Response (200 OK):**
```json
{
  "result": "Recognition scan completed. 89 patterns identified.",
  "patterns": 89,
  "status": "SUCCESS"
}
```

---

### 8. Engine Replicate
Startet den Replikationsprozess.

**Request:**
```http
POST /api/engine/replicate
Authorization: Basic admin:password
```

**cURL:**
```bash
curl -X POST -u admin:password \
  http://localhost:58133/api/engine/replicate
```

**Response (200 OK):**
```json
{
  "result": "Replication process initiated. 5 nodes engaged.",
  "nodes": 5,
  "status": "SUCCESS"
}
```

---

### 9. Engine Logs
Ruft die letzten Execution Logs ab.

**Request:**
```http
GET /api/engine/logs
Authorization: Basic admin:password
```

**cURL:**
```bash
curl -u admin:password http://localhost:58133/api/engine/logs
```

**Response (200 OK):**
```json
{
  "logs": [
    {
      "ts": "2026-07-03T20:35:00Z",
      "cmd": "evolve",
      "result": "Evolution triggered. New generation: 1267",
      "status": "SUCCESS"
    }
  ]
}
```

---

### 10. Health Check
Prüft die Verfügbarkeit des Backends.

**Request:**
```http
GET /health
```

**cURL:**
```bash
curl http://localhost:58133/health
```

**Response (200 OK):**
```json
{
  "status": "OK",
  "timestamp": "2026-07-03T20:35:00Z"
}
```

---

## Error Handling

### 401 Unauthorized
```json
{
  "error": "Authentication required."
}
```

**Ursachen:**
- Fehlender Authorization Header
- Ungültige Credentials
- Abgelaufene Session

### 400 Bad Request
```json
{
  "error": "Missing required fields"
}
```

**Ursachen:**
- Fehlende Request Parameter
- Ungültiges JSON Format
- Ungültige Datentypen

### 500 Internal Server Error
```json
{
  "error": "Internal server error"
}
```

**Ursachen:**
- Server-Fehler
- Unerwartete Exception
- Datenbankfehler

---

## Rate Limiting

Aktuell: **Keine Rate Limits** (für Entwicklung)

Für Production:
- 1000 Requests pro Minute
- 10 Requests pro Sekunde pro IP

---

## Webhooks (Zukünftig)

```http
POST /api/webhooks/register
Authorization: Basic admin:password
Content-Type: application/json

{
  "url": "https://example.com/webhook",
  "events": ["engine.evolve", "node.register"]
}
```

---

## SDK Integration

### JavaScript/TypeScript
```typescript
import { alphaAPI } from './lib/apiIntegration';

alphaAPI.setConfig({
  baseURL: 'http://localhost:58133',
  username: 'admin',
  password: 'password'
});

const status = await alphaAPI.getEngineStatus();
```

### Python
```python
import requests
from requests.auth import HTTPBasicAuth

response = requests.get(
    'http://localhost:58133/api/engine/status',
    auth=HTTPBasicAuth('admin', 'password')
)
print(response.json())
```

### cURL (Bash)
```bash
#!/bin/bash
BASE_URL="http://localhost:58133"
AUTH="admin:password"

# Get Engine Status
curl -u $AUTH $BASE_URL/api/engine/status

# Execute Command
curl -X POST -u $AUTH \
  -H "Content-Type: application/json" \
  -d '{"cmd":"evolve"}' \
  $BASE_URL/api/engine/execute
```

---

## Best Practices

1. **Immer HTTPS in Production verwenden**
2. **API Keys statt Basic Auth verwenden**
3. **Rate Limiting implementieren**
4. **Requests cachen wo möglich**
5. **Error Handling implementieren**
6. **Timeouts setzen (30s)**
7. **Retry-Logik für fehlgeschlagene Requests**

---

## Changelog

### v1.0.0 (2026-07-03)
- Initial Release
- Engine Status Endpoint
- Mobile Nodes Management
- Security Catalog
- Command Execution
- Health Check

---

## Support

Für Fragen oder Issues: Siehe `INTEGRATION_GUIDE.md`

---

Erstellt mit Manus AI
