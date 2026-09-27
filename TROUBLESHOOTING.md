# Troubleshooting Guide

## Häufige Probleme und Lösungen

---

## Backend (alpha-backend)

### Problem: Port 58133 ist bereits in Benutzung

**Symptom:**
```
Error: listen EADDRINUSE: address already in use :::58133
```

**Lösung:**

1. **Finde den Prozess, der den Port nutzt:**
```bash
lsof -i :58133
```

2. **Beende den Prozess:**
```bash
kill -9 <PID>
```

3. **Oder ändere den Port in `server.js`:**
```javascript
const PORT = 58134; // Neuer Port
```

---

### Problem: npm install schlägt fehl

**Symptom:**
```
npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
```

**Lösung:**

```bash
# Verwende --legacy-peer-deps
npm install --legacy-peer-deps

# Oder nutze npm 7+
npm install --force
```

---

### Problem: Backend startet nicht

**Symptom:**
```
TypeError: Cannot find module 'express'
```

**Lösung:**

```bash
# Stelle sicher, dass dependencies installiert sind
cd alpha-backend
npm install

# Prüfe ob node_modules existiert
ls -la node_modules/

# Starte Backend neu
npm start
```

---

## Frontend (flowstate-next)

### Problem: Vite Server startet nicht

**Symptom:**
```
Error: ENOSPC: no space left on device
```

**Lösung:**

```bash
# Lösche node_modules und package-lock.json
rm -rf node_modules package-lock.json

# Installiere neu
npm install

# Starte dev server
npm run dev
```

---

### Problem: API Connection Error

**Symptom:**
```
Error: Failed to fetch http://localhost:58133/api/engine/status
```

**Lösungen:**

1. **Prüfe ob Backend läuft:**
```bash
curl -u admin:password http://localhost:58133/health
```

2. **Prüfe API Base URL in Settings:**
- Öffne http://localhost:5173/settings
- Stelle sicher, dass API Base URL korrekt ist
- Standard: `http://localhost:58133`

3. **Prüfe CORS:**
```bash
# Backend sollte CORS aktiviert haben
curl -H "Origin: http://localhost:5173" \
     -H "Access-Control-Request-Method: GET" \
     -H "Access-Control-Request-Headers: authorization" \
     -X OPTIONS http://localhost:58133/api/engine/status
```

---

### Problem: Authentifizierung fehlgeschlagen

**Symptom:**
```
401 Unauthorized
```

**Lösungen:**

1. **Prüfe Credentials:**
   - Username: `admin`
   - Password: `password`

2. **Prüfe Base64 Encoding:**
```bash
echo -n "admin:password" | base64
# Output: YWRtaW46cGFzc3dvcmQ=
```

3. **Teste mit cURL:**
```bash
curl -u admin:password http://localhost:58133/api/engine/status
```

---

### Problem: Local Storage wird nicht gespeichert

**Symptom:**
- State wird nach Refresh nicht wiederhergestellt
- Daten sind weg

**Lösungen:**

1. **Prüfe Browser Local Storage:**
```javascript
// Öffne Browser Console (F12)
localStorage.getItem('flowstate-next-state')
```

2. **Lösche Local Storage:**
```javascript
localStorage.clear()
// Refresh die Seite
```

3. **Prüfe ob Private Browsing aktiv ist:**
- Private Browsing deaktivieren
- Local Storage funktioniert nicht im Private Mode

---

## Mobile (project-alpha-mobile)

### Problem: Expo CLI nicht gefunden

**Symptom:**
```
command not found: expo
```

**Lösung:**

```bash
# Installiere Expo CLI global
npm install -g expo-cli

# Oder nutze npx
npx expo start
```

---

### Problem: QR Code scannen funktioniert nicht

**Symptom:**
- QR Code wird nicht erkannt
- Expo Go startet nicht

**Lösungen:**

1. **Stelle sicher, dass Expo Go installiert ist:**
   - iOS: App Store
   - Android: Google Play Store

2. **Prüfe Netzwerkverbindung:**
```bash
# Stelle sicher, dass Handy und Computer im gleichen Netzwerk sind
ping <computer-ip>
```

3. **Starte Expo neu:**
```bash
npx expo start --clear
```

---

### Problem: API Connection auf Mobile

**Symptom:**
- Mobile App kann nicht mit Backend verbinden
- "Connection refused"

**Lösungen:**

1. **Nutze die Computer-IP statt localhost:**
```bash
# Finde deine IP
ifconfig | grep "inet "

# Verwende diese IP in der Mobile App
http://192.168.1.100:58133
```

2. **Prüfe Firewall:**
```bash
# Öffne Port 58133
sudo ufw allow 58133
```

3. **Teste Verbindung:**
```bash
# Vom Handy
curl -u admin:password http://<computer-ip>:58133/health
```

---

## Docker

### Problem: Docker Container startet nicht

**Symptom:**
```
docker: Error response from daemon
```

**Lösung:**

```bash
# Prüfe Docker Status
docker ps

# Prüfe Logs
docker-compose logs

# Rebuild Images
docker-compose build --no-cache

# Starte neu
docker-compose up -d
```

---

### Problem: Port-Konflikt in Docker

**Symptom:**
```
Error: Bind for 0.0.0.0:58133 failed
```

**Lösung:**

1. **Ändere Port in docker-compose.yml:**
```yaml
ports:
  - "58134:58133"  # Neuer Port
```

2. **Oder stoppe andere Container:**
```bash
docker-compose down
```

---

## Performance

### Problem: Slow API Responses

**Symptom:**
- API Requests dauern lange
- Frontend friert ein

**Lösungen:**

1. **Prüfe Backend Performance:**
```bash
# Messe Response Zeit
time curl -u admin:password http://localhost:58133/api/engine/status
```

2. **Prüfe Netzwerk:**
```bash
ping localhost
```

3. **Erhöhe Timeout in Frontend:**
```typescript
// In apiIntegration.ts
const response = await fetch(url, {
  headers: { Authorization: this.getAuthHeader() },
  signal: AbortSignal.timeout(60000) // 60 Sekunden
});
```

---

## Debugging

### Browser DevTools

1. **Öffne Developer Tools:**
   - Chrome/Firefox: F12
   - Safari: Cmd+Option+I

2. **Prüfe Console für Errors:**
   - Tab: Console
   - Suche nach roten Errors

3. **Prüfe Network Requests:**
   - Tab: Network
   - Filtere nach "api"
   - Prüfe Request/Response

### Backend Debugging

```bash
# Starte mit Debug Logs
DEBUG=* npm start

# Oder nutze Node Inspector
node --inspect server.js
```

### Mobile Debugging

```bash
# Nutze Expo DevTools
npx expo start --dev-client

# Oder Remote Debugging
adb logcat | grep "ReactNative"
```

---

## Logs

### Backend Logs

```bash
# Tail Logs
tail -f alpha-backend/logs.txt

# Oder nutze PM2
pm2 logs alpha-backend
```

### Frontend Logs

```bash
# Browser Console
console.log()
console.error()
console.warn()
```

### Docker Logs

```bash
# Alle Container
docker-compose logs -f

# Spezifischer Container
docker-compose logs -f alpha-backend
```

---

## Reset & Clean

### Vollständiger Reset

```bash
# Backend
cd alpha-backend
rm -rf node_modules package-lock.json
npm install

# Frontend
cd flowstate-next
rm -rf node_modules package-lock.json dist
npm install

# Mobile
cd project-alpha-mobile
rm -rf node_modules package-lock.json
npm install

# Docker
docker-compose down -v
docker-compose up -d
```

### Local Storage löschen

```javascript
// Browser Console
localStorage.clear()
sessionStorage.clear()
```

---

## Support

Falls das Problem nicht gelöst ist:

1. **Prüfe die Logs:**
   - Browser Console (F12)
   - Backend Terminal
   - Docker Logs

2. **Teste mit cURL:**
```bash
curl -v -u admin:password http://localhost:58133/api/engine/status
```

3. **Prüfe Dokumentation:**
   - `INTEGRATION_GUIDE.md`
   - `API_REFERENCE.md`
   - `PROJECT_STRUCTURE.md`

---

Erstellt mit Manus AI
