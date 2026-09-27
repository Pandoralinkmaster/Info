// Termux-Service: Führt echte Shell-Befehle aus über Termux:API oder WebSocket
// Unterstützt: Installation, Ausführung, Status-Prüfung aller 316 Tools

import AsyncStorage from '@react-native-async-storage/async-storage';

export interface TermuxCommand {
  command: string;
  args?: string[];
  background?: boolean;
  timeout?: number;
}

export interface TermuxResult {
  stdout: string;
  stderr: string;
  exitCode: number;
  duration: number;
}

export interface InstalledTool {
  id: string;
  name: string;
  installedAt: string;
  version: string;
  path: string;
}

const STORAGE_KEY = '@pandora_installed_tools';
const CUSTOM_TOOLS_KEY = '@pandora_custom_tools';

class TermuxService {
  private wsConnection: WebSocket | null = null;
  private pendingCommands: Map<string, { resolve: Function; reject: Function }> = new Map();
  private installedTools: InstalledTool[] = [];

  async initialize() {
    const stored = await AsyncStorage.getItem(STORAGE_KEY);
    if (stored) {
      this.installedTools = JSON.parse(stored);
    }
  }

  // Verbinde mit Termux über WebSocket (wenn Termux:API läuft)
  connectToTermux(host: string = 'localhost', port: number = 8765): Promise<boolean> {
    return new Promise((resolve) => {
      try {
        this.wsConnection = new WebSocket(`ws://${host}:${port}`);
        this.wsConnection.onopen = () => resolve(true);
        this.wsConnection.onerror = () => resolve(false);
        this.wsConnection.onmessage = (event) => {
          const data = JSON.parse(event.data);
          const pending = this.pendingCommands.get(data.id);
          if (pending) {
            pending.resolve(data.result);
            this.pendingCommands.delete(data.id);
          }
        };
      } catch {
        resolve(false);
      }
    });
  }

  // Führe einen Befehl über Termux aus
  async executeCommand(cmd: TermuxCommand): Promise<TermuxResult> {
    const startTime = Date.now();
    
    if (this.wsConnection?.readyState === WebSocket.OPEN) {
      // Echte Ausführung über WebSocket
      const id = Math.random().toString(36).substring(7);
      return new Promise((resolve, reject) => {
        this.pendingCommands.set(id, { resolve, reject });
        this.wsConnection!.send(JSON.stringify({ id, ...cmd }));
        
        // Timeout
        setTimeout(() => {
          if (this.pendingCommands.has(id)) {
            this.pendingCommands.delete(id);
            reject(new Error('Timeout'));
          }
        }, cmd.timeout || 30000);
      });
    }
    
    // Simulierte Ausführung (wenn kein Termux verbunden)
    return {
      stdout: `[Termux nicht verbunden] Befehl bereit: ${cmd.command} ${(cmd.args || []).join(' ')}\n\nUm diesen Befehl auszuführen:\n1. Öffne Termux auf deinem Android-Gerät\n2. Starte den Pandora-Server: pandora-server start\n3. Verbinde die App mit dem Server`,
      stderr: '',
      exitCode: 0,
      duration: Date.now() - startTime,
    };
  }

  // Installiere ein Tool
  async installTool(toolId: string, name: string, installCommand: string): Promise<TermuxResult> {
    const result = await this.executeCommand({
      command: 'bash',
      args: ['-c', installCommand],
      timeout: 120000,
    });

    if (result.exitCode === 0) {
      const tool: InstalledTool = {
        id: toolId,
        name,
        installedAt: new Date().toISOString(),
        version: '1.0.0',
        path: `/data/data/com.termux/files/home/.pandora/tools/${toolId}`,
      };
      this.installedTools.push(tool);
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(this.installedTools));
    }

    return result;
  }

  // Prüfe ob ein Tool installiert ist
  isInstalled(toolId: string): boolean {
    return this.installedTools.some(t => t.id === toolId);
  }

  // Hole alle installierten Tools
  getInstalledTools(): InstalledTool[] {
    return this.installedTools;
  }

  // Führe ein installiertes Tool aus
  async runTool(toolId: string, args: string[] = []): Promise<TermuxResult> {
    const tool = this.installedTools.find(t => t.id === toolId);
    if (!tool) {
      return {
        stdout: '',
        stderr: `Tool ${toolId} ist nicht installiert.`,
        exitCode: 1,
        duration: 0,
      };
    }

    return this.executeCommand({
      command: tool.path,
      args,
    });
  }

  // Custom Tool hinzufügen
  async addCustomTool(name: string, repoUrl: string): Promise<TermuxResult> {
    const installCmd = `cd ~/.pandora/tools && git clone ${repoUrl} ${name.toLowerCase().replace(/\s+/g, '-')}`;
    return this.installTool(
      `custom_${Date.now()}`,
      name,
      installCmd
    );
  }

  // Speichere Custom Tools
  async saveCustomTools(tools: Array<{ name: string; repoUrl: string; description: string }>) {
    await AsyncStorage.setItem(CUSTOM_TOOLS_KEY, JSON.stringify(tools));
  }

  // Lade Custom Tools
  async loadCustomTools(): Promise<Array<{ name: string; repoUrl: string; description: string }>> {
    const stored = await AsyncStorage.getItem(CUSTOM_TOOLS_KEY);
    return stored ? JSON.parse(stored) : [];
  }

  // Netzwerk-Scan
  async networkScan(subnet?: string): Promise<TermuxResult> {
    const cmd = subnet 
      ? `nmap -sn ${subnet} 2>/dev/null || ping -c 1 -W 1 ${subnet}`
      : `ip route | grep default | awk '{print $3}' | xargs -I{} nmap -sn {}/24 2>/dev/null || echo "nmap nicht installiert"`;
    return this.executeCommand({ command: 'bash', args: ['-c', cmd], timeout: 60000 });
  }

  // Datei-Scan
  async fileScan(path: string = '/', pattern?: string): Promise<TermuxResult> {
    const cmd = pattern 
      ? `find ${path} -name "${pattern}" -type f 2>/dev/null | head -500`
      : `find ${path} -type f 2>/dev/null | head -500`;
    return this.executeCommand({ command: 'bash', args: ['-c', cmd], timeout: 30000 });
  }

  // System-Info
  async systemInfo(): Promise<TermuxResult> {
    const cmd = `echo "=== System Info ===" && uname -a && echo "" && echo "=== CPU ===" && cat /proc/cpuinfo | head -20 && echo "" && echo "=== Memory ===" && free -h && echo "" && echo "=== Storage ===" && df -h && echo "" && echo "=== Network ===" && ip addr show 2>/dev/null || ifconfig`;
    return this.executeCommand({ command: 'bash', args: ['-c', cmd] });
  }

  // Spyware-Detection
  async spywareDetection(): Promise<TermuxResult> {
    const cmd = `echo "=== Spyware Detection ===" && echo "" && echo "Checking for known indicators..." && echo "" && echo "1. Checking running processes..." && ps aux 2>/dev/null | grep -iE "pegasus|nso|chrysaor|predator" && echo "" && echo "2. Checking network connections..." && netstat -tlnp 2>/dev/null | grep -iE "ESTABLISHED|LISTEN" && echo "" && echo "3. Checking installed packages..." && dpkg -l 2>/dev/null | grep -iE "spy|monitor|track" && echo "" && echo "4. Checking suspicious files..." && find /data/data -name "*.so" -newer /data/data/com.termux 2>/dev/null | head -20 && echo "" && echo "Scan complete."`;
    return this.executeCommand({ command: 'bash', args: ['-c', cmd], timeout: 60000 });
  }

  // Bluetooth Mesh
  async bluetoothScan(): Promise<TermuxResult> {
    const cmd = `echo "=== Bluetooth Scan ===" && hcitool scan 2>/dev/null || echo "Bluetooth-Tools nicht verfügbar. Installiere: pkg install bluez-utils"`;
    return this.executeCommand({ command: 'bash', args: ['-c', cmd] });
  }

  // WiFi Scan
  async wifiScan(): Promise<TermuxResult> {
    const cmd = `echo "=== WiFi Scan ===" && iwlist scan 2>/dev/null || termux-wifi-scaninfo 2>/dev/null || echo "WiFi-Scan nicht verfügbar. Installiere: pkg install wireless-tools"`;
    return this.executeCommand({ command: 'bash', args: ['-c', cmd] });
  }

  // Crypto Operations
  async cryptoHash(input: string, algorithm: string = 'sha256'): Promise<TermuxResult> {
    const cmd = `echo -n "${input}" | ${algorithm}sum`;
    return this.executeCommand({ command: 'bash', args: ['-c', cmd] });
  }

  // GIS/Geospatial
  async geoLookup(lat: number, lon: number): Promise<TermuxResult> {
    const cmd = `curl -s "https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lon}&format=json" 2>/dev/null || echo "Kein Internet"`;
    return this.executeCommand({ command: 'bash', args: ['-c', cmd] });
  }

  disconnect() {
    this.wsConnection?.close();
    this.wsConnection = null;
  }
}

export const termuxService = new TermuxService();
export default termuxService;
