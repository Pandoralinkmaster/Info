# Projektstruktur

## Verzeichnisbaum

```
flowstate-project-alpha-complete/
│
├── README.md                          # Hauptdokumentation
├── INTEGRATION_GUIDE.md                # Detaillierte Integrationsleitfaden
├── PROJECT_STRUCTURE.md               # Diese Datei
├── docker-compose.yml                 # Docker Compose für All-in-One Setup
├── quick-start.sh                     # Schnellstart-Script
│
├── alpha-backend/                     # Project Alpha Mock Backend
│   ├── server.js                      # Express Server mit API Endpoints
│   ├── package.json                   # Dependencies
│   ├── Dockerfile                     # Docker Image
│   └── README.md                      # Backend Dokumentation
│
├── flowstate-next/                    # FlowState Next Web App
│   ├── src/
│   │   ├── App.tsx                    # Hauptkomponente mit Routing
│   │   ├── main.tsx                   # Entry Point
│   │   ├── styles.css                 # Globale Styles
│   │   ├── types.ts                   # TypeScript Interfaces
│   │   ├── components/
│   │   │   └── AlphaIntegration.tsx   # Project Alpha Integration Component
│   │   └── lib/
│   │       ├── seed.ts                # Initiale Daten
│   │       ├── useLocalStorage.ts     # Local Storage Hook
│   │       └── apiIntegration.ts      # API Client für Project Alpha
│   ├── index.html                     # HTML Template
│   ├── package.json                   # Dependencies
│   ├── vite.config.ts                 # Vite Konfiguration
│   ├── tsconfig.json                  # TypeScript Konfiguration
│   ├── Dockerfile                     # Docker Image
│   └── dist/                          # Build Output
│
├── project-alpha-mobile/              # Project Alpha Mobile App
│   ├── app/
│   │   ├── screens/                   # Screen-Komponenten
│   │   ├── _layout.tsx                # Navigation Layout
│   │   └── index.tsx                  # Home Screen
│   ├── lib/
│   │   ├── api-client.ts              # API Client
│   │   ├── auth-context.tsx           # Authentication Context
│   │   ├── theme-provider.tsx         # Theme Provider
│   │   └── _core/                     # Core Utilities
│   ├── hooks/
│   │   ├── use-auth.ts                # Auth Hook
│   │   └── use-colors.ts              # Color Hook
│   ├── package.json                   # Dependencies
│   ├── app.json                       # Expo Konfiguration
│   ├── tsconfig.json                  # TypeScript Konfiguration
│   └── design.md                      # Design-Spezifikation
│
└── [weitere Dateien aus den Originalzips]
```

---

## Komponenten-Übersicht

### Backend (alpha-backend)
- **Express Server** auf Port 58133
- **REST API** mit Basic Auth
- **Endpoints:**
  - `GET /api/engine/status` - Engine Status
  - `GET /api/mobile/nodes` - Registrierte Nodes
  - `GET /api/security/catalog` - Security Tools
  - `POST /api/mobile/register` - Device registrieren
  - `POST /api/engine/execute` - Command ausführen
  - `POST /api/engine/evolve` - Evolution starten
  - `POST /api/engine/recognize` - Pattern Recognition
  - `POST /api/engine/replicate` - Replikation

### Frontend (flowstate-next)
- **React + Vite** Web Application
- **Pages:**
  - Dashboard - Hauptübersicht
  - Mesh - Netzwerkverwaltung
  - JayJay KI - Sprachassistent
  - Wallet - Bitcoin Management
  - Security - Sicherheitslogs
  - Storage - Dateimanagement
  - Engine - Project Alpha Integration
  - Settings - Konfiguration
  
- **Features:**
  - Dark Mode / Matrix Theme
  - Local Storage Persistenz
  - Real-time Charts (Recharts)
  - Responsive Design
  - Export/Import

### Mobile (project-alpha-mobile)
- **React Native + Expo**
- **Screens:**
  - Login
  - Dashboard
  - Engine Status
  - Mobile Nodes
  - Security Catalog
  - Logs
  - Settings
  
- **Features:**
  - Authentication
  - Offline Mode
  - Local Caching
  - Dark Mode
  - API Integration

---

## Datenfluss

```
┌──────────────────┐
│  User Interface  │
│  (Web/Mobile)    │
└────────┬─────────┘
         │
         │ HTTP/REST
         │
┌────────▼─────────┐
│  API Integration │
│  (apiIntegration │
│   .ts / .tsx)    │
└────────┬─────────┘
         │
         │ Basic Auth
         │
┌────────▼──────────────┐
│  Express Backend      │
│  (server.js)          │
└────────┬──────────────┘
         │
         │ In-Memory
         │ Storage
         │
┌────────▼──────────────┐
│  Data Store           │
│  (Devices, Logs, etc) │
└───────────────────────┘
```

---

## Authentifizierung

**Basic Auth:**
```
Username: admin
Password: password
```

**Header:**
```
Authorization: Basic YWRtaW46cGFzc3dvcmQ=
```

---

## Umgebungsvariablen

### Backend
```bash
NODE_ENV=production
PORT=58133
```

### Frontend
```bash
VITE_API_BASE_URL=http://localhost:58133
VITE_API_USERNAME=admin
VITE_API_PASSWORD=password
```

### Mobile
```bash
EXPO_PUBLIC_API_URL=http://localhost:58133
EXPO_PUBLIC_API_USERNAME=admin
EXPO_PUBLIC_API_PASSWORD=password
```

---

## Build & Deployment

### Lokal
```bash
# Backend
cd alpha-backend && npm install && npm start

# Frontend
cd flowstate-next && npm install && npm run dev

# Mobile
cd project-alpha-mobile && npm install && npx expo start
```

### Docker
```bash
docker-compose up -d
```

### Production
```bash
# Build Frontend
cd flowstate-next && npm run build

# Deploy Backend
pm2 start alpha-backend/server.js

# Deploy Mobile
eas build --platform ios
eas build --platform android
```

---

## Abhängigkeiten

### Backend
- express
- cors
- body-parser

### Frontend
- react
- react-router-dom
- recharts
- lucide-react
- typescript

### Mobile
- expo
- react-native
- @react-navigation
- typescript
- drizzle-orm
- @trpc/client

---

## Erweiterungspunkte

1. **Neue API Endpoints** - Backend erweitern
2. **Neue Pages** - Frontend Routing hinzufügen
3. **Neue Screens** - Mobile Komponenten
4. **Datenbank** - SQLite/PostgreSQL Integration
5. **Authentifizierung** - OAuth2/JWT
6. **Real-time Updates** - WebSocket Integration
7. **File Upload** - S3/Cloud Storage

---

## Support & Dokumentation

- **Integration Guide:** `INTEGRATION_GUIDE.md`
- **Backend README:** `alpha-backend/README.md`
- **Mobile Design:** `project-alpha-mobile/design.md`
- **API Docs:** Siehe INTEGRATION_GUIDE.md

---

Erstellt mit Manus AI - Vollständig lokal ausführbar!
