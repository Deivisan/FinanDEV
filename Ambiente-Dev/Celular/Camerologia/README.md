# 📸 Camerologia Poco X5 - Expansão Sensores & Configs

> **Objetivo:**

> **Criado:**

> **Status:**

> **Futuro:** Pode virar repositório standalone

---

## 🎯 Visão Geral

**Foco:** Não é fotografia artística, mas **o que a câmera pode fazer**

- Sensores disponíveis e limites reais

- Configurações avançadas (HDR+, Night Sight, 360°)

- Ports GCam otimizados para Poco X5 + Android 16 custom

- Hacks via Termux para automação de captura

**Meta final:** Assets vetoriais do rosto (SVG/landmarks) + fotos 360° do setup dev

---

## 📋 Checklist GCam Ports - Testes

### Legenda

- ✅ Funciona perfeitamente

- 🚧 Funciona com bugs/limitações

- ❌ Não funciona/crash

- ⚪ Não testado

---

### MGC 9.4.103_V22 (BSG - Setembro 2025)

| Feature | Status | Notas |
|---------|--------|-------|
| HDR+

| Night Sight | ⚪ | - |

| Panorama 360° | ⚪ | -

| Filmagem 4K 60fps | ⚪ | -

| Sensor Ultra-Wide | ⚪ | -

| Sensor Macro | ⚪ | -

| RAW Export | ⚪ | -

| Stitching Qualidade | ⚪ | - |

---

### MGC 9.6.113_V0.1_beta (BSG - Novembro 2025)

| Feature | Status | Notas |
|---------|--------|-------|
| HDR+

| Night Sight | ⚪ | - |

| Panorama 360° | ⚪ | Auto-stitching melhorado |
| Filmagem 4K 60fps | ⚪ | -

| Sensor Ultra-Wide | ⚪ | -

| Sensor Macro | ⚪ | -

| RAW Export | ⚪ | -

| Stitching Qualidade | ⚪ | - |

---

### LMC 8.4 R18 (Hasli/Arnova)

| Feature | Status | Notas |
|---------|--------|-------|
| HDR+

| Night Sight | ⚪ | - |

| Panorama 360° | ⚪ | -

| Filmagem 4K 60fps | ⚪ | -

| Sensor Ultra-Wide | ⚪ | -

| Sensor Macro | ⚪ | -

| RAW Export | ⚪ | Alta res para edição |
| Stitching Qualidade | ⚪ | - |

---

### AGC 9.4_V0.3 (Config XML Recomendada)

| Feature | Status | Notas |
|---------|--------|-------|
| Sensores Extras | ⚪ | Ativa 48MP completo |
| HDR+

| Night Sight | ⚪ | - |

| Panorama 360° | ⚪ | - |

---

### AGC 9.6.24_V0.X (Beta - A testar)

| Feature | Status | Notas |
|---------|--------|-------|
| IA Avançada | ⚪ | Recursos Pixel novos |
| HDR+

| Night Sight | ⚪ | - |

| Panorama 360° | ⚪ | - |

---

## 🛠️ Recursos do Celular

### Sensores Disponíveis

- **Principal:** 48MP (Samsung ISOCELL GM1)

- **Ultra-Wide:** 8MP 120°

- **Macro:** 2MP (distância mín. 4cm)

- **Giroscópio + Acelerômetro:** Para estabilização/360°

- **Magnetômetro:** Orientação espacial

### Capacidades Especiais

- **Panorama emulado 360°:** Via stitching automático (modo padrão GCam)

- **RAW DNG:** Export para edição vetorial posterior

- **Night Sight:** Low-light até 3 lux

- **HDR+ Enhanced:** Múltiplas exposições para detalhes

---

## 📊 Uso Estratégico Camerologia

### 1. Captura Rosto Vetorial (Face Assets)

**Objetivo:** Criar animações personalizadas (puxar cortina no site)

**Pipeline:**

1. Tirar 20-30 fotos rosto (frontal, laterais 45°, close bigode)

2. GCam com RAW ou alta res (MGC 9.4/LMC 8.4)

3. Processar com MediaPipe (Termux Python) → landmarks 468 pontos 3D

4. Exportar SVG vetorial + JSON coordenadas

5. Usar em Blender/Lottie para animação web

**Alternativas online:**

- Polycam (polycam.io) - Scan 3D via browser

- KIRI Engine (kiriengine.app) - AR mapping automático

- Ready Player Me (readyplayer.me) - Avatar 3D instant

---

### 2. Fotos 360° Setup Dev

**Objetivo:** Backup visual do ambiente de desenvolvimento

**Método:**

1. GCam modo Panorama (MGC 9.4 recomendado)

2. Girar devagar 360° completos

3. Stitching automático gera esférico interativo

4. Salvar em FinanDEV/Assets/Setup-360/YYYY-MM-DD.jpg

**Uso futuro:** Comparar setups ao longo dos anos, ver evolução workspace

---

### 3. Filmagens 4K para Treinos

**Testar:** Quais ports suportam 4K 60fps estável
**Uso:** Gravar séries de exercícios, analisar forma depois

---

## 🔬 Testes Pendentes

### Protocolo de Teste (Para cada GCam)

1. Instalar APK via ADB ou manual

2. Configurar XML (se aplicável)

3. Testar cada feature da checklist

4. Anotar bugs, crashes, limitações

5. Comparar qualidade output (HDR+, stitching)

6. Escolher top 3 para manter instaladas

> 📝 Preencher checklist acima conforme testes avançarem

---

## 🤖 Automação Termux (Futuro)

### Script Auto-Captura Rosto

```python

# auto-capture-face.py

# Termux + Tasker + GCam intent

# Tira 20 fotos automáticas em ângulos pré-definidos

# Salva em ~/storage/shared/DCIM/Face-Capture/

```text

### Debug Inteligente Câmera

```bash

# camera-debug.sh

# Conecta via USB, puxa logs kernel sensores

# Analisa qual sensor ativo, framerate, exposição

# Output JSON para FinanDEV/Ambiente-Dev/logs/

```text

---

## 📚 Referências

### Fontes GCam Ports

-

  -

  -

  - Dev Arnova8G2: Configs XML

### Tutoriais

- XDA Developers - Poco X5 GCam threads

- YouTube - Reviews de ports específicos

- Reddit r/PocoPhones - Feedback comunidade

---

## 🎯 Metas

- [ ] Testar todas as 5 GCams listadas

- [ ] Escolher top 3 (HDR geral, Night, 360°)

- [ ] Capturar rosto 20+ fotos para vetorização

- [ ] Fazer primeira foto 360° do setup

- [ ] Configurar auto-captura via Termux

- [ ] Exportar landmarks faciais (MediaPipe)

---

*Sistema experimental | Documentação em construção | Pode virar repo standalone futuro*
