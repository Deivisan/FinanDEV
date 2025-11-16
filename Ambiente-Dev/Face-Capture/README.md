# 👤 Face Capture - Vetorização Rosto para Assets

> **Objetivo:** Capturar traços faciais precisos (landmarks 468 pontos 3D)  
> **Uso:** Criar animações personalizadas (ex: puxar cortina no site DeiviTech)  
> **Pipeline:** Fotos → Processamento → SVG/JSON vetorial → Animação

---

## 🎯 Visão Geral

**Por quê?**
- Ter assets visuais únicos (meu rosto em desenho vetorial)
- Animações disruptivas em sites/apps (abertura customizada)
- Deepfakes personalizados para vídeos futuros
- Backup visual: "como eu era em 2025"

**Output esperado:**
- Arquivo SVG escalável infinitamente (sem perder qualidade)
- JSON com 468 landmarks 3D (coordenadas x, y, z de cada ponto facial)
- Mesh 3D opcional para Blender/Unity

---

## 📸 Fase 1: Captura de Fotos

### Equipamento
- **Celular:** Poco X5 com GCam port (MGC 9.4 ou LMC 8.4 R18)
- **Resolução:** 12MP+ (sensor principal 48MP)
- **Iluminação:** Natural, difusa, sem sombras fortes
- **Fundo:** Neutro (parede lisa, sem padrões)

### Ângulos Necessários (20-30 fotos)
1. **Frontal:** Olhando direto (neutro, sorrindo, sério)
2. **Laterais:** Perfil esquerdo/direito completo
3. **45 graus:** Meio-perfil esquerdo/direito
4. **Close-ups:** Olhos, nariz, boca, bigode (fios individuais)
5. **Variações:** Diferentes expressões (raiva, alegria, surpresa)

### Protocolo de Captura
```markdown
- Mesma iluminação para todas (manhã, janela natural)
- Mesma distância focal (braço estendido ou tripé)
- RAW DNG se possível (mais dados para processar)
- Salvar em: ~/storage/shared/DCIM/Face-Capture/YYYY-MM-DD/
```

---

## 🧠 Fase 2: Processamento (MediaPipe)

### Tecnologia
- **MediaPipe Face Mesh** (Google, open-source, grátis)
- **468 landmarks 3D** detectados automaticamente
- **Edge detection** para detalhes finos (bigode, rugas)

### Script Python (Termux/Arch)
```python
# face-landmarks.py
import cv2
import mediapipe as mp
import json

mp_face = mp.solutions.face_mesh

# Processar cada foto
with mp_face.FaceMesh(static_image_mode=True, max_num_faces=1) as face_mesh:
    for foto in glob.glob('Face-Capture/2025-11-16/*.jpg'):
        img = cv2.imread(foto)
        results = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            
            # Exportar JSON
            data = {
                'foto': foto,
                'landmarks': [
                    {'id': i, 'x': lm.x, 'y': lm.y, 'z': lm.z}
                    for i, lm in enumerate(landmarks)
                ]
            }
            
            with open(f'{foto}.json', 'w') as f:
                json.dump(data, f, indent=2)
```

**Output:** `foto.jpg.json` com 468 pontos (x, y, z normalizados 0-1)

---

## 🎨 Fase 3: Vetorização (SVG)

### Ferramentas Online (Usuário Final, Clique a Clique)

#### 1. Vectorizer.AI
- **URL:** vectorizer.ai
- **Uso:** Upload foto → espera 10s → download SVG
- **Vantagens:** Grátis, detecta edges automático, incluindo bigode
- **Limitações:** Não tem controle fino de landmarks

#### 2. Recraft.ai
- **URL:** recraft.ai
- **Uso:** Upload foto → ajuste detalhes (fios cabelo, bigode) → export SVG
- **Vantagens:** Editor visual, full-color tracing
- **Limitações:** Freemium (limite 5 exports/dia grátis)

#### 3. Vector Magic
- **URL:** vectormagic.com
- **Uso:** Upload BMP/JPG → conversão automática → SVG download
- **Vantagens:** Preciso para detalhes faciais
- **Limitações:** Pago ($9.95/mês)

---

### Ferramentas Offline (Script Python)

#### Potrace (Open-Source)
```bash
# Converter foto para SVG vetorial
potrace -s foto.pbm -o rosto.svg
```

#### Autotrace
```bash
autotrace --output-file rosto.svg --output-format svg foto.jpg
```

---

## 🧊 Fase 4: Scan 3D (Alternativa Rápida)

### Apps que Geram Modelo 3D Direto

#### 1. Polycam (Melhor Opção)
- **URL:** polycam.io
- **Uso:** Web ou app mobile → girar rosto devagar → modelo 3D pronto
- **Output:** STL, OBJ, GLTF (importa Blender direto)
- **Tempo:** 1-2 minutos
- **Custo:** Grátis básico, Pro $10/mês para mais resolução

#### 2. KIRI Engine
- **URL:** kiriengine.app
- **Uso:** Web puro, AR mapping automático
- **Output:** JSON landmarks + mesh 3D
- **Vantagens:** Roda suave no Poco X5

#### 3. Ready Player Me
- **URL:** readyplayer.me
- **Uso:** Selfie upload ou vídeo curto → avatar 3D
- **Output:** Modelo pronto para Unity/web animations
- **Vantagens:** Disruptivo, exporta facilmente

---

## 🎬 Fase 5: Animação

### Para Web (Site DeiviTech)

#### Lottie (JSON Animations)
```javascript
// Importar landmarks como morph targets
import lottie from 'lottie-web';

lottie.loadAnimation({
  container: document.getElementById('deivi-face'),
  renderer: 'svg',
  loop: false,
  autoplay: true,
  path: 'assets/deivi-puxa-cortina.json'
});
```

#### CSS + SVG
```css
/* Animação puxar cortina com rosto */
.deivi-face {
  animation: puxa-cortina 2s ease-in-out;
}

@keyframes puxa-cortina {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(0); }
}
```

---

### Para Vídeo (Deepfakes Futuro)

#### Stable Diffusion + ControlNet
- Usar landmarks como guia
- Prompt: "Deivison puxando cortina, cartoon style"
- Output: Vídeo curto 5-10s

#### Runway Gen-2
- Upload foto rosto
- Descreve ação: "puxar cortina suavemente"
- IA gera vídeo realista

---

## 📊 Estrutura Arquivos

```
FinanDEV/
└── Ambiente-Dev/
    └── Face-Capture/
        ├── README.md (este arquivo)
        ├── Fotos/
        │   ├── 2025-11-16/
        │   │   ├── frontal-01.jpg
        │   │   ├── frontal-01.jpg.json (landmarks)
        │   │   ├── perfil-esq.jpg
        │   │   └── close-bigode.jpg
        ├── Vetoriais/
        │   ├── rosto-completo.svg
        │   ├── landmarks-468.json
        │   └── mesh-3d.obj
        └── Animacoes/
            ├── puxa-cortina.json (Lottie)
            └── abertura-site.mp4
```

---

## 🎯 Checklist de Execução

- [ ] Capturar 20-30 fotos (ângulos variados)
- [ ] Processar com MediaPipe → JSON landmarks
- [ ] Vetorizar com Vectorizer.AI ou Recraft → SVG
- [ ] (Opcional) Scan 3D com Polycam → modelo Blender
- [ ] Criar animação Lottie "puxar cortina"
- [ ] Testar no site DeiviTech local
- [ ] Salvar assets finais em Ambiente-Dev/Face-Capture/

---

## 🔗 Referências

- **MediaPipe Docs:** mediapipe.dev/solutions/face_mesh
- **Polycam Tutorial:** YouTube - "3D Face Scan with Phone"
- **Lottie Web:** airbnb.io/lottie/web/
- **SVG Animation:** CSS-Tricks guides

---

*Projeto experimental | Assets únicos personalizados | Disruptivo visuais*
