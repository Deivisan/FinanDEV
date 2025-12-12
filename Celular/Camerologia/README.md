# 📦 Camerologia movida para Ambiente-Dev/Celular/Camerologia/

Este conteúdo foi consolidado em `Ambiente-Dev/Celular/Camerologia/README.md` para centralizar recursos técnicos e metodologias práticas. A versão antiga está arquivada como `Celular/Camerologia/README_legacy.md`.

**Por favor, edite a versão consolidada no caminho acima (Ambiente-Dev/Celular/Camerologia/README.md).**
---

## 🎯 Objetivo

Criar **galeria fotográfica estruturada** do físico, moda e ambiente dev para:
- Tracking progresso corpo (60kg → 70kg meta maio/2026)
- Documentar evolução setup (Ryzen 7, monitores, periféricos)
- Backup visual 360° ambiente completo
- **"Relic Mode"**: Ver como era tudo daqui 10 anos

---

## 📱 Especificações Técnicas Poco X5

### Sensores Câmera
- **Principal:** 48MP (f/1.8) - Samsung ISOCELL GM2
- **Ultra-wide:** 8MP (118°)
- **Macro:** 2MP
- **Frontal:** 13MP

### Sensores Auxiliares (Fotografia)
- **Luz ambiente:** Ajuste ISO automático
- **Giroscópio:** Estabilização digital
- **Acelerômetro:** Detecção orientação
- **Magnetômetro:** Geo-tagging (bússola)

---

## 🛠️ Apps Google Camera Recomendados (2025)

### MGC 9.4 BSG (Modo Panorama 360°)
**Uso:** Captura setup dev completo, ambiente 360°

**Features:**
- Stitching automático (costura fotos em esfera)
- Estabilização superior Snapdragon 695
- Export interativo (scroll panorâmico)

**Download:** [Celso Azevedo - BSG](https://www.celsoazevedo.com/files/android/google-camera/dev-bsg/)

**Config sugerida:**
```
HDR+: Enhanced
Resolução: 48MP (sem binning)
Stitching: Alta qualidade (processamento 30s)
```

**Como capturar setup:**
1. Posiciona phone centro ambiente
2. Rotação lenta 360° (15s total)
3. App costura automaticamente
4. Salva em `Celular/Camerologia/360-Setup/`

---

### LMC 8.4 R18 (Hasli) - Fotos Detalhadas
**Uso:** Progresso corpo, outfit diário, close-ups hardware

**Features:**
- HDR+ extremo (detalhes sombras/luz)
- Night Sight aprimorado
- RAW + JPEG simultâneo
- Astrofotografia (sensores longos)

**Download:** [Celso Azevedo - Hasli](https://www.celsoazevedo.com/files/android/google-camera/dev-hasli/)

**Config corpo/moda:**
```
Modo: Retrato (desfoque background)
HDR+: Enhanced
Grid: 3x3 (composição terços)
Timer: 3s (evita tremor)
```

---

## 📂 Estrutura Proposta

```
Celular/Camerologia/
  README.md (este arquivo)
  360-Setup/
    2025-11-16-setup-completo.jpg (panorama)
    2025-12-01-novo-monitor.jpg
  Tracking-Corpo/
    2025-11/
      16-frente-60kg.jpg
      16-lado-60kg.jpg
      16-costas-60kg.jpg
    2025-12/
      ...
  Outfit-Diario/
    2025-11-16-camisa-preta-oversized.jpg
  Configs-GCam/
    mgc-9.4-bsg-config.xml
    lmc-8.4-hasli-config.xml
  ANALISE-VISUAL.md (métricas + insights)
```

---

## 📋 Metodologia Fotos Consistentes

### Tracking Corpo (Baseado em apps fitness 2025)

**Frequência:** Semanal (mesma hora, mesmo dia)

**Setup:**
- **Local:** Parede branca/neutra
- **Luz:** Natural (janela) ou ring light
- **Hora:** 7h manhã (pré-café, pós-banheiro)
- **Roupa:** Sem camisa, bermuda preta

**Poses obrigatórias (9 pontos medição):**
1. Frente relaxado
2. Frente flexionado (bíceps)
3. Lado direito
4. Lado esquerdo
5. Costas relaxado
6. Costas lat spread
7. Pernas frente
8. Pernas lado
9. Close braço (circunferência)

**Timer GCam:** 3 segundos (posiciona antes)

**Metadata salvar:**
```markdown
# 2025-11-16
- Peso: 60kg
- Braço: 28cm
- Cintura: 76cm
- Observações: Início tracking
```

---

### Outfit Diário

**Frequência:** Diária (opcional fins de semana)

**Setup:**
- Espelho corpo inteiro
- Luz natural
- GCam modo retrato (desfoque fundo)

**Metadata:**
```markdown
# 2025-11-16
- Camisa: Preta oversized (Renner)
- Calça: Cargo jeans rasgado
- Tênis: All Star preto
- Contexto: Trabalho casual
```

---

### Setup Dev 360°

**Frequência:** Mensal (ou após upgrades)

**Setup MGC Panorama:**
1. Limpa setup (remove objetos temporários)
2. Liga todos monitores (screenshot desktop)
3. Iluminação ambiente completa
4. Phone centro sala, altura 1.5m
5. Rotação lenta 360° (app guia)

**Metadata:**
```markdown
# 2025-11-16 Setup
- PC: Ryzen 7 5700G, 32GB, B450M
- Monitor 1: LG 24" 1080p
- Monitor 2: Samsung 22" (vertical)
- Teclado: Redragon Kumara
- Mouse: Logitech G203
- Observações: Adicionado mousepad XL
```

---

## 🎨 Apps Complementares (Opcional)

### Metamorph (Líder 2025)
- **Função:** Comparação lado-a-lado fotos
- **Features:** Overlay transparente (vê progresso real)
- **Link:** Play Store (free trial 7 dias)

### Gym Body Tracker
- **Função:** 9 pontos circunferência automático
- **Features:** OCR extrai medidas de foto fita métrica
- **Link:** Play Store

### Me 360
- **Função:** Scan 3D corpo via câmera
- **Features:** Modelo 3D interativo, export OBJ
- **Nota:** Requer Android 12+ (Poco X5 OK)

---

## 🧪 Experimentos Futuros

### 1. Astrofotografia Setup
- Usar Night Sight para capturar céu noturno
- Salvar em `Camerologia/Astro/`
- Metadata: constelações visíveis, poluição luminosa

### 2. Timelapse Batch Cooking
- GCam modo timelapse (1 foto/10s)
- Documenta processo domingo 19-21h
- Export vídeo 30s (2h condensado)

### 3. Sensor Fusion Testing
- Combinar giroscópio + acelerômetro
- Hyperlapse estabilizado (caminhadas)
- Salvar dados sensor JSON paralelo

---

## 📊 Integração Backup Mental

### Atualização Automática `ANALISE-VISUAL.md`

```python
# update_visual_analysis.py
from PIL import Image
from PIL.ExifTags import TAGS
import os

def extract_metadata(foto_path):
    img = Image.open(foto_path)
    exif = img._getexif()
    
    return {
        'data': exif.get('DateTime'),
        'resolucao': f"{img.width}x{img.height}",
        'camera': exif.get('Model'),
        'iso': exif.get('ISOSpeedRatings'),
        'exposicao': exif.get('ExposureTime')
    }

def update_analysis_md():
    fotos = sorted(os.listdir('Tracking-Corpo/2025-11'))
    
    with open('ANALISE-VISUAL.md', 'a') as f:
        for foto in fotos:
            meta = extract_metadata(f'Tracking-Corpo/2025-11/{foto}')
            f.write(f"- {meta['data']}: {foto} ({meta['resolucao']})\n")
```

---

## 🔗 Referências Web (2025)

**Fitness Photography:**
- Trainero: Visual Progress Tracking (9-point measurements)
- Metamorph: Leading progress app 2025
- Exercise.com: Gym photo software best practices

**GCam Community:**
- Celso Azevedo: 200+ ports catalogados
- MGC BSG: Melhor Panorama Android 2025
- LMC Hasli: Top HDR+ Snapdragon 695

**Body Scanning:**
- Me 360: 3D scanning via phone camera
- Gym Body Tracker: OCR measurements
- Instagram Reel: Phone scan demo (DLQVyIiPyJ0)

---

## ✅ Checklist Inicial

- [ ] Baixar MGC 9.4 BSG (Celso Azevedo)
- [ ] Baixar LMC 8.4 R18 Hasli
- [ ] Configurar timer 3s GCam
- [ ] Tirar primeira foto 360° setup
- [ ] Criar subpastas (Tracking-Corpo, Outfit, 360-Setup)
- [ ] Primeira sessão tracking corpo (9 poses)
- [ ] Testar Metamorph comparação fotos
- [ ] Script Python metadata extraction

---

**Última atualização:** 16/11/2025  
**Próxima ação:** Captura inicial setup 360° + primeira foto corpo
