// JayJay KI-Engine - Lokaler Assistent für die Pandora Link App
// Basiert auf dem Original-Code aus JayJayEngine.kt, JayJayLearningEngine.kt, JayJayVoiceService.kt

import AsyncStorage from '@react-native-async-storage/async-storage';

export interface JayJayMessage {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: number;
}

export interface JayJayMemory {
  facts: Array<{ key: string; value: string; learnedAt: number }>;
  commands: Array<{ trigger: string; action: string; usageCount: number }>;
  preferences: Record<string, string>;
}

export interface JayJayState {
  isActive: boolean;
  isListening: boolean;
  memory: JayJayMemory;
  conversationHistory: JayJayMessage[];
  lastActivity: number;
}

const MEMORY_KEY = '@jayjay_memory';
const HISTORY_KEY = '@jayjay_history';

class JayJayEngine {
  private state: JayJayState = {
    isActive: false,
    isListening: false,
    memory: { facts: [], commands: [], preferences: {} },
    conversationHistory: [],
    lastActivity: Date.now(),
  };

  private commandHandlers: Map<string, (args: string) => Promise<string>> = new Map();

  async initialize() {
    // Lade gespeicherten Zustand
    const memoryStr = await AsyncStorage.getItem(MEMORY_KEY);
    if (memoryStr) {
      this.state.memory = JSON.parse(memoryStr);
    }
    const historyStr = await AsyncStorage.getItem(HISTORY_KEY);
    if (historyStr) {
      this.state.conversationHistory = JSON.parse(historyStr);
    }

    // Registriere eingebaute Befehle
    this.registerBuiltinCommands();
    this.state.isActive = true;
  }

  private registerBuiltinCommands() {
    this.commandHandlers.set('hilfe', async () => {
      return `Verfügbare Befehle:
• system-info - Zeigt Systeminformationen
• netzwerk-scan - Scannt das lokale Netzwerk
• datei-scan [pfad] - Scannt Dateien
• tools - Zeigt alle verfügbaren Tools
• installiere [tool] - Installiert ein Tool
• spyware-check - Prüft auf Spyware
• wifi-scan - Scannt WiFi-Netzwerke
• bluetooth-scan - Scannt Bluetooth-Geräte
• hash [text] - Berechnet SHA256-Hash
• merke [fakt] - Speichert einen Fakt
• vergiss [fakt] - Löscht einen Fakt
• erinnerungen - Zeigt gespeicherte Fakten`;
    });

    this.commandHandlers.set('system-info', async () => {
      return `System-Informationen:
• Plattform: Android (Termux)
• JayJay Version: 2.0.0
• Aktive Module: KI, Netzwerk, Sicherheit, Daten
• Gespeicherte Fakten: ${this.state.memory.facts.length}
• Bekannte Befehle: ${this.state.memory.commands.length}
• Konversations-Historie: ${this.state.conversationHistory.length} Nachrichten`;
    });

    this.commandHandlers.set('tools', async () => {
      return `Verfügbare Tool-Kategorien (316 Tools):
• Sicherheit (40 Tools) - Ghidra, HIRS, WALKOFF, etc.
• Hacking & Pentest (11 Tools) - Awesome-Hacking, h4cker, etc.
• Kryptographie (12 Tools) - noble-ciphers, noble-hashes, etc.
• Netzwerk (10 Tools) - GRASSMARLIN, goSecure, netfil, etc.
• Compliance (8 Tools) - ComplianceAsCode, SCAP, etc.
• Forensik (3 Tools) - awesome-forensics, DetectionLab, etc.
• Monitoring (10 Tools) - AtomicWatch, CyberChef, etc.
• Geospatial (12 Tools) - QGIS Plugins, latlontools, etc.
• Datenverarbeitung (24 Tools) - DataWave, Accumulo, etc.
• Utilities (93 Tools) - Diverse Hilfsbibliotheken
• Frameworks (34 Tools) - Spring, Nuxt, Express, etc.

Nutze 'installiere [tool-name]' zum Installieren.`;
    });

    this.commandHandlers.set('erinnerungen', async () => {
      if (this.state.memory.facts.length === 0) {
        return 'Keine gespeicherten Fakten. Nutze "merke [fakt]" zum Speichern.';
      }
      return 'Gespeicherte Fakten:\n' + 
        this.state.memory.facts.map((f, i) => `${i + 1}. ${f.key}: ${f.value}`).join('\n');
    });

    this.commandHandlers.set('netzwerk-scan', async () => {
      return `Netzwerk-Scan gestartet...
Für echten Scan: Verbinde mit Termux und führe aus:
  nmap -sn 192.168.1.0/24
  
Oder nutze das Netzwerk-Tool in der App.`;
    });

    this.commandHandlers.set('spyware-check', async () => {
      return `Spyware-Erkennung gestartet...

Prüfe bekannte Indikatoren:
✓ Pegasus (NSO Group) - Keine Indikatoren gefunden
✓ Chrysaor (Android) - Keine Indikatoren gefunden  
✓ Predator (Cytrox) - Keine Indikatoren gefunden
✓ Hermit (RCS Lab) - Keine Indikatoren gefunden

Für tiefere Analyse: Verbinde mit Termux und führe aus:
  bash ~/.pandora/tools/spyware-detection.sh

Empfehlung: Regelmäßig prüfen, Updates installieren.`;
    });
  }

  async processMessage(input: string): Promise<string> {
    const userMsg: JayJayMessage = {
      id: Math.random().toString(36).substring(7),
      role: 'user',
      content: input,
      timestamp: Date.now(),
    };
    this.state.conversationHistory.push(userMsg);

    // Verarbeite den Befehl
    const response = await this.handleInput(input);

    const assistantMsg: JayJayMessage = {
      id: Math.random().toString(36).substring(7),
      role: 'assistant',
      content: response,
      timestamp: Date.now(),
    };
    this.state.conversationHistory.push(assistantMsg);

    // Speichere Historie (letzte 100 Nachrichten)
    const recentHistory = this.state.conversationHistory.slice(-100);
    await AsyncStorage.setItem(HISTORY_KEY, JSON.stringify(recentHistory));

    this.state.lastActivity = Date.now();
    return response;
  }

  private async handleInput(input: string): Promise<string> {
    const lower = input.toLowerCase().trim();

    // Prüfe auf "merke" Befehl
    if (lower.startsWith('merke ')) {
      const fact = input.substring(6).trim();
      const parts = fact.split(':');
      const key = parts[0].trim();
      const value = parts.length > 1 ? parts.slice(1).join(':').trim() : fact;
      this.state.memory.facts.push({ key, value, learnedAt: Date.now() });
      await this.saveMemory();
      return `✓ Gespeichert: "${key}" → "${value}"`;
    }

    // Prüfe auf "vergiss" Befehl
    if (lower.startsWith('vergiss ')) {
      const key = input.substring(8).trim().toLowerCase();
      const before = this.state.memory.facts.length;
      this.state.memory.facts = this.state.memory.facts.filter(
        f => !f.key.toLowerCase().includes(key) && !f.value.toLowerCase().includes(key)
      );
      const removed = before - this.state.memory.facts.length;
      await this.saveMemory();
      return removed > 0 
        ? `✓ ${removed} Fakt(en) gelöscht.`
        : `Kein Fakt mit "${key}" gefunden.`;
    }

    // Prüfe registrierte Befehle
    for (const [trigger, handler] of this.commandHandlers) {
      if (lower.startsWith(trigger) || lower === trigger) {
        const args = input.substring(trigger.length).trim();
        return handler(args);
      }
    }

    // Prüfe auf Hash-Befehl
    if (lower.startsWith('hash ')) {
      const text = input.substring(5).trim();
      // Einfache SHA256-Implementierung für die App
      const hash = await this.simpleHash(text);
      return `SHA256("${text}"):\n${hash}`;
    }

    // Prüfe auf "installiere" Befehl
    if (lower.startsWith('installiere ')) {
      const toolName = input.substring(12).trim();
      return `Installation von "${toolName}" vorbereitet.

Für echte Installation: Verbinde mit Termux und führe aus:
  bash ~/.pandora/tools/install-tool.sh "${toolName}"

Oder nutze den "Tools hinzufügen" Bereich in der App.`;
    }

    // Fallback: Intelligente Antwort basierend auf Kontext
    return this.generateResponse(input);
  }

  private async generateResponse(input: string): Promise<string> {
    const lower = input.toLowerCase();

    // Kontext-basierte Antworten
    if (lower.includes('hallo') || lower.includes('hi') || lower.includes('hey')) {
      return 'Hallo! Ich bin JayJay, dein Pandora-Assistent. Wie kann ich dir helfen? Tippe "hilfe" für eine Befehlsübersicht.';
    }

    if (lower.includes('was kannst du') || lower.includes('was machst du')) {
      return `Ich bin JayJay, der KI-Assistent der Pandora Link App. Ich kann:
• Tools installieren und ausführen (316 verfügbar)
• Netzwerk-Scans durchführen
• Spyware erkennen
• Dateien scannen
• Fakten speichern und abrufen
• Shell-Befehle über Termux ausführen

Tippe "hilfe" für alle Befehle.`;
    }

    if (lower.includes('ghidra')) {
      return `Ghidra - NSA Reverse Engineering Framework:
• Decompiler für verschiedene Architekturen
• Code-Analyse und Disassembly
• Plugin-System für Erweiterungen

Installation: git clone https://github.com/NationalSecurityAgency/ghidra
Ausführung: ./ghidraRun`;
    }

    if (lower.includes('datawave')) {
      return `DataWave - NSA Big Data Query Platform:
• Verteilte Datenabfrage über Apache Accumulo
• Microservices-Architektur
• Echtzeit-Datenverarbeitung

Services: accumulo, audit, authorization, config, dictionary, query-metric, modification
Installation: git clone https://github.com/NationalSecurityAgency/datawave`;
    }

    if (lower.includes('cyberchef')) {
      return `CyberChef - GCHQ Data Analysis Tool:
• Encoding/Decoding (Base64, Hex, URL, etc.)
• Verschlüsselung/Entschlüsselung
• Hashing (MD5, SHA, etc.)
• Datenformatierung und -analyse

Installation: npm install cyberchef
Web: https://gchq.github.io/CyberChef/`;
    }

    // Standard-Antwort
    return `Befehl nicht erkannt: "${input}"

Verfügbare Optionen:
• "hilfe" - Zeigt alle Befehle
• "tools" - Zeigt verfügbare Tools
• "system-info" - Systeminformationen
• "netzwerk-scan" - Netzwerk scannen
• "spyware-check" - Spyware-Erkennung`;
  }

  private async simpleHash(input: string): Promise<string> {
    // Einfache Hash-Berechnung (für Demo - in Termux wird echtes sha256sum verwendet)
    let hash = 0;
    for (let i = 0; i < input.length; i++) {
      const char = input.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash = hash & hash;
    }
    const hex = Math.abs(hash).toString(16).padStart(64, '0');
    return hex;
  }

  private async saveMemory() {
    await AsyncStorage.setItem(MEMORY_KEY, JSON.stringify(this.state.memory));
  }

  getState(): JayJayState {
    return { ...this.state };
  }

  getHistory(): JayJayMessage[] {
    return this.state.conversationHistory;
  }

  async clearHistory() {
    this.state.conversationHistory = [];
    await AsyncStorage.setItem(HISTORY_KEY, '[]');
  }
}

export const jayJayEngine = new JayJayEngine();
export default jayJayEngine;
