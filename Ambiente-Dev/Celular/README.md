# 📱 Ambiente Dev - Poco X5 (Deivison)

## 🔧 Hardware Completo

### 📲 Modelo
**Marca:** Xiaomi  
**Modelo:** Poco X5 (5G)  
**Chipset:** Qualcomm Snapdragon 778G (6nm)
- CPU: Octa-core (4x2.4 GHz Kryo 670 + 4x1.9 GHz Kryo 670)
- GPU: Adreno 642L
- NPU: Hexagon 770 (IA/ML)
- Fabricação: 6nm TSMC

---

### 📷 Câmeras

**Câmera Traseira (Triple):**
- Principal: 48MP (sensor Sony IMX582)
  - Abertura: f/1.8
  - Pixel: 0.8µm (binning → 1.6µm)
  - Autofoco: PDAF
  - Resolução max: 8000x6000
- Ultra-wide: 8MP
  - Abertura: f/2.2
  - FOV: 118°
  - Resolução: 3264x2448
- Macro: 2MP
  - Abertura: f/2.4
  - Foco: 4cm
  - Resolução: 1600x1200

**Recursos Câmera:**
- Vídeo: 4K@30fps, 1080p@60fps
- Slow-motion: 720p@120fps
- HDR: Sim (suporte GCam ports)
- Night Mode: Sim
- Panorama: Sim
- RAW: Sim (via GCam)

**Câmera Frontal:**
- Selfie: 13MP
- Abertura: f/2.5
- Vídeo: 1080p@30fps

---

### 🎯 Sensores Completos

| Sensor | Tipo | Função | Uso Estratégico |
|--------|------|--------|------------------|
| **Acelerômetro** | Bosch BMI160 | Detecta movimento/aceleração | Treino (contar reps), quedas, gestos |
| **Giroscópio** | Bosch BMI160 | Detecta rotação/orientação | AR, estabilização vídeo, 360° capture |
| **Magnetômetro** | AK09918C | Bússola digital | Orientação, mapas, AR, alinhamento fotos |
| **Proximidade** | STK3321 | Distância objetos (0-5cm) | Auto-lock tela, pausar logs, gestos hover |
| **Luz Ambiente** | STK3321 | Intensidade luminosa | Auto-brilho, tracking qualidade luz treino |
| **Passos** | Virtual (SoC) | Contador passos | Pedômetro, calorias, rotinas caminhada |
| **Impressão Digital** | Goodix (lateral) | Biometria | Unlock, autenticação apps |
| **GPS** | Multi-GNSS | Localização (GPS, GLONASS, Galileo, BDS) | Corrida, mapas, geotagging fotos |
| **NFC** | NXP PN81T | Pagamentos contactless | Pix NFC, transferências |
| **IR Blaster** | Sim | Controle remoto infravermelho | Automação casa (TV, AC) |

---

### 🧠 Memória e Storage

**RAM:** 8GB LPDDR4X (2133MHz)  
**Storage:** 256GB UFS 2.2  
**Expansível:** Não (sem slot microSD)

---

### 🔋 Bateria

**Capacidade:** 5000 mAh (Li-Po)  
**Carga:** 33W fast charge (0-50% em 25min)  
**Autonomia estimada:** 1.5-2 dias uso médio

---

### 📡 Conectividade

**5G:** Sim (SA/NSA, dual-SIM)  
**WiFi:** 802.11 a/b/g/n/ac (dual-band)  
**Bluetooth:** 5.2 (A2DP, LE, aptX HD)  
**USB:** Type-C 2.0 (OTG suportado)  
**Audio Jack:** Sim (3.5mm)

---

### 📐 Tela

**Tamanho:** 6.67" AMOLED  
**Resolução:** 2400x1080 (FHD+, ~395 ppi)  
**Taxa atualização:** 120Hz  
**Touch sampling:** 240Hz  
**Brilho:** 700 nits (típico), 1200 nits (pico HDR)  
**Proteção:** Corning Gorilla Glass 3

---

## 💿 Sistema Operacional

### 🔓 ROM Custom: Infinity-X

**Baseado em:** Android 16 (AOSP customizado)  
**Kernel:** Linux 5.4 (otimizado)  
**Root:** Sim (Magisk instalado)  
**Recovery:** TWRP ou OrangeFox  
**Mods instalados:**
- Magisk modules: [A LISTAR]
- Xposed/LSPosed: [A VERIFICAR]
- Kernel tweaks: [A DOCUMENTAR]

**Recursos Infinity-X:**
- Debloated (sem apps Xiaomi)
- Performance mode ativo
- Custom bootanimation
- Temas modificáveis
- Tweaks de bateria/performance

---

## 🛠️ Software e Apps Estratégicos

### 📷 Camerologia (Celso Azevedo Ports)

**GCam Ports Instalados:** [A TESTAR]
- BSG MGC 9.2: HDR+ low-light, configs XML sensores extras
- Arnova8G2: Night sight, stitching 360°
- cstark27: Compatibilidade Snapdragon otimizada
- Nikita MGC: [A TESTAR]
- Wichaya MGC: [A TESTAR]

**Configs/XMLs:** `Celular/Camerologia/configs/`

**Funcionalidades Testadas:**
- [ ] HDR+ Enhanced
- [ ] Night Sight
- [ ] Astrophotography
- [ ] Photosphere 360°
- [ ] Slow Motion 240fps
- [ ] RAW capture (DNG)
- [ ] Ultra-wide GCam

---

### 🔧 Termux + Alpine Linux

**Termux versão:** Latest (F-Droid)  
**Distro:** Alpine Linux (container)  
**Package manager:** apk (Alpine Package Keeper)

**Linguagens instaladas:**
- Python 3.x + pip
- Node.js + npm
- Rust (cargo)
- Go
- Java (OpenJDK)

**Tools CLI:**
- git, curl, wget, ssh
- ffmpeg, imagemagick
- pandas, numpy (Python)
- matplotlib (gráficos)

**Scripts desenvolvidos:**
- Sensor logger (acelerômetro/giroscópio → JSON)
- Face capture pipeline (MediaPipe)
- Treino tracker (reps counter)
- Sleep monitor (acelerômetro noturno)

---

### 📦 DriveDroid (USB Boot Injection)

**Versão:** [A PREENCHER]  
**Root:** Necessário ✅ (instalado)  
**Função:** Injetar ISOs como pendrive bootável via USB

**ISOs configurados:**
- Arch Linux: [A ADICIONAR]
- Ubuntu: [A ADICIONAR]
- Windows 11: [A ADICIONAR]
- Memtest86+: [A ADICIONAR]
- Rescue disks: [A ADICIONAR]

**Uso:** Formatação/instalação sistemas em PCs sem mídia física

---

### 🎯 Apps Sensores

**Sleep Tracking:**
- Sleep as Android (acelerômetro + microfone)
- Sleep Cycle (free version)
- Urbandroid apps

**Fitness:**
- SensorStream: Logs sensores tempo real
- Fitness Tracker custom (Termux script)
- Google Fit (contador passos)

**Automação:**
- Tasker + AutoInput (gestos, sensores)
- MacroDroid (automações simples)
- IFTTT (integração web)

---

## 🎯 Capacidades Estratégicas

### 📸 Captura Facial/Vetorial
- **Pipeline:** GCam port → MediaPipe → Landmarks 3D → SVG/JSON
- **Ângulos:** Frontal, laterais 45°, close-up bigode
- **Output:** 468 pontos faciais (olhos, nariz, contornos, pelos)
- **Uso:** Assets animações web, avatars 3D

**Alternativas cloud:**
- Polycam.io (web-based 3D scan)
- KIRI Engine (AR face mapping)
- Ready Player Me (avatar export)

---

### 🏋️ Tracking Treino

**Sensores usados:**
- Acelerômetro: Contar repetições (agachamento, flexões)
- Giroscópio: Detectar amplitude movimento
- Passos: Caminhada/corrida
- Luz ambiente: Qualidade ambiente treino

**Script Termux:**
```python
# sensor_logger.py
import android
droid = android.Android()
droid.startSensingTimed(1, 250)  # Accel, 250ms

while True:
    accel = droid.sensorsReadAccelerometer().result
    # Processa movimento, detecta rep
    # Salva JSON → FinanDEV/Logs/Treino/
```

**Output:** `YYYY-MM-DD_treino.json` → integra com Mini-Sistemas

---

### 🌙 Análise Sono

**Como usar:**
1. Deixar celular na cama/colchão (carga)
2. App Sleep as Android detecta movimentos via acelerômetro
3. Mapeia fases: REM, profundo, leve, acordado
4. Alarme inteligente: acorda fase leve (janela 30min)

**Integração FinanDEV:**
- Export JSON → `Rotinas/Sono/YYYY-MM-DD.json`
- Cruza com Mini-Sistemas/SAUDE-MENTAL.md (humor)
- Detecta padrões: sono ruim → humor baixo

---

### 🧭 Orientação e AR

**Magnetômetro + Giroscópio:**
- Bússola digital (mapas, trilhas)
- AR simples (alinhar objetos 3D)
- Geotagging fotos (direção cardeal)

**Apps:**
- Compass 360 Pro
- AR Core (Google)
- Cardboard (VR básico)

---

### 🔧 USB OTG Capabilities

**Com root + DriveDroid:**
- Injetar ISOs bootáveis (formatar PCs)
- Pendrive virtual (storage externo)
- Teclado/mouse emulado (HID)
- Ethernet via adaptador USB

**Testes futuros:**
- [ ] Boot Arch Linux via celular
- [ ] Instalar Windows 11 remoto
- [ ] Recovery PC-UFRB sem mídia
- [ ] Ethernet USB adapter

---

## 📊 Sensores Detalhados (Specs Técnicas)

### Acelerômetro Bosch BMI160
- **Range:** ±2g, ±4g, ±8g, ±16g (configurável)
- **Resolution:** 16-bit
- **Taxa amostragem:** 12.5Hz a 1600Hz
- **Consumo:** 180 µA (normal mode)
- **Eixos:** X, Y, Z (3-axis)

### Giroscópio Bosch BMI160
- **Range:** ±125°/s, ±250°/s, ±500°/s, ±1000°/s, ±2000°/s
- **Resolution:** 16-bit
- **Taxa amostragem:** 25Hz a 3200Hz
- **Consumo:** 850 µA (normal mode)
- **Eixos:** Roll, Pitch, Yaw (3-axis)

### Magnetômetro AK09918C
- **Range:** ±4900 µT (microtesla)
- **Resolution:** 0.15 µT
- **Taxa amostragem:** 10Hz, 20Hz, 50Hz, 100Hz
- **Consumo:** 1.1 mA (continuous mode)
- **Precisão:** ±3° (orientação)

### Sensor Proximidade STK3321
- **Range:** 0-5 cm
- **Tecnologia:** Infravermelho
- **Consumo:** 3 mA (ativo)
- **Uso:** Detecção rosto (chamadas), hover gestos

### Sensor Luz Ambiente STK3321
- **Range:** 0.01 lux a 64000 lux
- **Resolution:** 16-bit
- **Consumo:** 0.5 mA
- **Uso:** Auto-brilho, condições fotografia

---

## 🔮 Próximas Expansões Camerologia

### Testes Prioritários
1. [ ] Testar 5 ports GCam (BSG, Arnova, cstark, Nikita, Wichaya)
2. [ ] Configurar XMLs custom por sensor (principal, ultra-wide, macro)
3. [ ] Capturar dataset 360° rosto (20-30 fotos)
4. [ ] Script Termux → MediaPipe → SVG export
5. [ ] Photosphere 360° com stitching

### Integrações FinanDEV
1. [ ] Pipeline Face-Capture automatizado
2. [ ] Logs sensores treino → Mini-Sistemas/ROTINA-FISICA.md
3. [ ] Sono tracker → Mini-Sistemas/SLEEP-TRACKING.md
4. [ ] DriveDroid ISOs → Ambiente-Dev/Estoque/

### Automações Tasker
1. [ ] Acelerômetro parado 2h → Lembrete treino
2. [ ] Luz ambiente < 100 lux → Batch cooking reminder
3. [ ] Proximidade bolso → Pausar logs sensores
4. [ ] GPS academia → Iniciar treino tracker

---

## 📝 Notas Importantes

**Root Warnings:**
- Banking apps: Podem detectar root (usar Magisk Hide)
- SafetyNet: Precisa passar (módulos específicos)
- OTA updates: Bloqueadas (usar TWRP manual updates)

**Performance Tips:**
- Kernel governor: `performance` (treino) ou `schedutil` (bateria)
- CPU boost: Ativar para compilações Termux
- GPU rendering: Force 120Hz em apps específicos
- Thermal throttling: Monitor com Franco Kernel Manager

**Backup Strategy:**
- TWRP nandroid: Semanal (recovery partition)
- Titanium Backup: Apps + dados
- Sync Termux: Git push scripts → GitHub
- Fotos: Google Photos unlimited (compressão) + local NAS

---

## 🎯 Sensores → Rotinas (Roadmap)

| Sensor | Rotina Atual | Rotina Futura |
|--------|--------------|---------------|
| Acelerômetro | Manual (apps) | Auto-log treino → JSON FinanDEV |
| Giroscópio | Estabilização vídeo | AR experiences, 360° fotos |
| Magnetômetro | Bússola maps | Alinhamento fotos, orientação automática |
| Proximidade | Auto-lock tela | Pausar sensores (bolso), gestos hover |
| Luz ambiente | Auto-brilho | Tracking luz treino, reminder batch cooking |
| Passos | Google Fit | Integrar Meta +10kg (calorias) |
| GPS | Maps básico | Geotagging rotinas, tracking corrida |
| NFC | Pagamentos | Automação casa (tags NFC) |
| IR Blaster | - | Controle TV/AC scripts Termux |

---

**Última atualização:** [AUTO - Git hook]  
**Próxima revisão:** Após testar 5 GCam ports
