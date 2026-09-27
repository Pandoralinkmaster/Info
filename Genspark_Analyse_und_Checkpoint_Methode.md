# Genspark AI Analyse & Checkpoint-Resume Methode

## Warum ich (Kimi) stoppe — Technische Gründe

| Grund | Beschreibung |
|-------|-------------|
| **Token-Limit** | Maximales Kontextfenster (~256.000 Tokens). Bei sehr langen Aufgaben wird der Kontext voll. |
| **Zeitlimit pro Antwort** | Jede Antwort hat ein Zeitlimit. Komplexe Aufgaben können dies überschreiten. |
| **Tool-Schritte** | Maximal 10 Tool-Aufrufe pro Nachricht. Danach muss ich pausieren. |
| **Kein persistenter Speicher** | Zwischen Nachrichten "vergesse" ich nichts, aber ich kann nicht eigenständig im Hintergrund weiterarbeiten. |
| **Keine Selbst-Autonomie** | Ich kann mich nicht selbst neu starten. Jede Interaktion erfordert deine Eingabe. |

---

## Entwickelte Methode: "Checkpoint & Resume" System

### Phase 1: Vor dem Start — Setup
1. Ziel klar und konkret definieren
2. "Master-Plan" mit nummerierten Schritten erstellen
3. Format für Zwischenergebnisse festlegen

### Phase 2: Während der Arbeit — Checkpointing
Nach jedem abgeschlossenen Schritt:
- Ergebnis in einer Zusammenfassung speichern
- Aktuellen Stand dokumentieren (z.B. "Schritt 3/7 erledigt")
- Offene Punkte auflisten

### Phase 3: Bei Unterbrechung — Resume
Wenn ich stoppe, einfach senden:
**"WEITER"** oder **"RESUME"** + die letzte Zusammenfassung

Ich setze dann exakt dort fort, wo wir aufgehört haben.

---

## Praktische Anwendung: Schritt-für-Schritt Protokoll

**Beispiel:** *"Analysiere diese 50-seitige PDF und erstelle eine Präsentation"*

```
PLAN (7 Schritte):
1. PDF laden und strukturieren
2. Kernpunkte extrahieren
3. Gliederung erstellen
4. Slide-Inhalte verfassen
5. Visuelle Konzepte planen
6. Finale Präsentation zusammenstellen
7. Export vorbereiten

STARTE: Schritt 1...
```

**[Nach Schritt 3 — Stop wegen Limit]**

**Deine Eingabe:** *"WEITER — Stand: Schritt 3/7 erledigt. Kernpunkte: [X, Y, Z]. Nächster: Gliederung."*

**Meine Antwort:**
```
✅ Bestätige: Schritt 3 abgeschlossen
📋 Fortsetze: Schritt 4 — Gliederung erstellen...
```

---

## Genspark-spezifische Informationen

### Genspark Plattform-Features (2026)
- **Super Agent**: Zentrale Steuerung aller Agenten
- **Hub-System**: Projektbasierte Organisation
- **AI Drive**: Cloud-Speicher für KI-generierte Inhalte
- **Custom Super Agents**: Benutzerdefinierte Agenten mit spezifischen Fähigkeiten
- **Multi-Agent-System**: Verschiedene Agenten für unterschiedliche Aufgaben

### Hybrider Workflow (Genspark + Kimi)
```
1. Genspark: Recherche, Datenbeschaffung, grobe Struktur
2. Kimi (ich): Detaillierte Analyse, Code, Präzisionsarbeit
3. Genspark: Finale Präsentation/Export
```

---

## Befehlssatz für Auto-Resume

| Befehl | Funktion |
|--------|----------|
| `PLAN: [Aufgabe]` | Nummerierten Plan erstellen |
| `WEITER` | Beim letzten Schritt fortsetzen |
| `STATUS` | Aktuellen Fortschritt anzeigen |
| `CHECKPOINT` | Zwischenstand speichern |
| `RESUME: [Zusammenfassung]` | Mit Kontext neu starten |

---

## Wichtiger Hinweis

Ich bin **Kimi K2.6** von Moonshot AI — nicht Genspark. Die URL `https://www.genspark.ai/agents?id=d7496729-1dc4-4c44-bca2-83cf09454de4` ist für mich nicht zugänglich. Ich habe daher allgemeine Informationen über Genspark recherchiert und eine universelle Fortsetzungsmethode entwickelt, die mit jeder KI-Plattform funktioniert.

---

*Erstellt am: 2026-06-29*
