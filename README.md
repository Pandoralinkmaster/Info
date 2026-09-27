# FlowState Next & Project Alpha Ecosystem

Dieses Paket enthält das vollständige, erweiterte Ökosystem von **FlowState Next** und **Project Alpha Mobile**, inklusive eines Mock-Backends für die lokale Entwicklung.

## Struktur

- `/flowstate-next`: Die Haupt-Web-App (Vite + React + TypeScript).
- `/project-alpha-mobile`: Die mobile App-Komponente (Expo + React Native).
- `/alpha-backend`: Ein Node.js Express Mock-Backend zur Simulation der Project Alpha API.

## Installation & Start

### 1. Backend (Optional für lokale API-Tests)
```bash
cd alpha-backend
npm install
npm start
```
Das Backend läuft auf `http://localhost:58133`.

### 2. FlowState Next (Web)
```bash
cd flowstate-next
npm install
npm run dev
```

### 3. Project Alpha Mobile (Mobile)
```bash
cd project-alpha-mobile
npm install
npx expo start
```

## Features & Integration
- **Zero-Trust Mesh Network Dashboard**: Überwachung von Mesh-Geräten und Sicherheit.
- **JayJay KI**: Integrierter Sprachassistent (Mockup).
- **BTC Wallet**: Transaktionsübersicht und Management.
- **Project Alpha Integration**: Direkte Anbindung an das Alpha-Backend für Engine-Status, Nodes und Security Catalog.
- **Dark Mode / Matrix Theme**: Anpassbare Cyberpunk-Ästhetik.

---
Erstellt von Manus AI.
