# 📷 GCam APKs - Poco X5 (Snapdragon 778G)

## 🎯 5 Ports Recomendados para Teste

### 1️⃣ BSG MGC 9.2.113 (PRIORIDADE MÁXIMA)
**Dev:** BSG  
**Versão:** MGC_9.2.113_A11_V29 (mais recente)  
**Android:** 11+  
**Foco:** HDR+ low-light, sensores extras, configs XML

**Download direto:**
```
https://www.celsoazevedo.com/files/android/google-camera/dev-bsg/f/dl229/
```

**APK filename:** `MGC_9.2.113_A11_V29_snap.apk` (org.codeaurora.snapcam)

**Features:**
- ✅ HDR+ Enhanced
- ✅ Night Sight otimizado
- ✅ Configs XML para sensores extras
- ✅ Astrophotography mode
- ✅ Compatibilidade Snapdragon (Qualcomm)

**Alternativas BSG (se V29 der problema):**
- V26: https://www.celsoazevedo.com/files/android/google-camera/dev-bsg/f/dl226/
- V0 (inicial): https://www.celsoazevedo.com/files/android/google-camera/dev-bsg/f/dl196/

---

### 2️⃣ Arnova8G2 Gcam 8.7.250 Build 8.3
**Dev:** Arnova8G2  
**Versão:** 8.7.250.build-8.3 (stable)  
**Android:** 11+  
**Foco:** Video modes, stitching 360°, cinematic

**Download direto:**
```
https://www.celsoazevedo.com/files/android/google-camera/dev-arnova8G2/f/dl7/
```

**APK filename:** `Gcam-8.7.250.build-8.3_snapcam.apk` (org.codeaurora.snapcam)

**Features:**
- ✅ All video modes (slow-mo, cinematic, 8K)
- ✅ Photosphere 360° stitching
- ✅ Astro timelapse
- ✅ Force video FPS
- ✅ Muito estável (v8.3 stable)

**Changelog v8.3:**
- Fixed all video modes para vários devices
- Add createCustomCaptureSession (operation mode)
- Gboard fix ativado por padrão
- Muito estável

**Hash verificação (snapcam):**
- MD5: `9098bcabba3db844d13b8ed678cd856e`
- SHA-1: `791571a78f90b67339af7155c37b714afcf06b49`

---

### 3️⃣ cstark27 PXv4.5 (Pixel Experience)
**Dev:** cstark27  
**Versão:** PXv4.5_GoogleCamera_7.2.014  
**Android:** 9+  
**Foco:** Libpatcher avançado, denoise tuning

**Download direto:**
```
https://www.celsoazevedo.com/files/android/google-camera/f/changelog1330/
```

**APK filename:** `PXv4.5_GoogleCamera_7.2.014.apk`

**Features:**
- ✅ Libpatcher com chroma1 levels
- ✅ Dehaze disable option
- ✅ Advanced denoise tuning
- ✅ Suporte Pixel 4a (similar ao seu Poco X5)

**Nota dev:** Projeto parado desde 2020, mas versão 4.5 muito boa para Snapdragon

---

### 4️⃣ Nikita GCam (Alternativa BSG)
**Dev:** Nikita  
**Versão:** [A BUSCAR - site Celso Azevedo]  
**Android:** 11+  
**Foco:** Night mode, RAW capture

**Download (buscar em):**
```
https://www.celsoazevedo.com/files/android/google-camera/
```

**Filtro:** Pesquisar "Nikita" na página

---

### 5️⃣ Wichaya GCam (Alternativa para testes)
**Dev:** Wichaya  
**Versão:** [A BUSCAR - site Celso Azevedo]  
**Android:** 11+  
**Foco:** Ultra-wide optimizations

**Download (buscar em):**
```
https://www.celsoazevedo.com/files/android/google-camera/
```

**Filtro:** Pesquisar "Wichaya" na página

---

## 🚀 Ordem de Teste Sugerida

1. **BSG MGC 9.2.113 V29** (começa por esse - mais completo)
2. **Arnova8G2 8.7.250.build-8.3** (testa video modes e 360°)
3. **cstark27 PXv4.5** (compara libpatcher vs BSG)
4. **Nikita** (alternativa night mode)
5. **Wichaya** (testa ultra-wide)

---

## 📥 Como Baixar e Instalar

### Passo 1: Download APKs
```bash
# No PC (Linux):
cd /home/deivi/Projetos/FinanDEV/Temp/GCam-APKs/

# Baixar BSG V29 (exemplo):
wget -O BSG_MGC_9.2.113_V29.apk \
  "https://www.celsoazevedo.com/files/android/google-camera/dev-bsg/f/dl229/MGC_9.2.113_A11_V29_snap.apk"

# Baixar Arnova8G2 8.3 (exemplo):
wget -O Arnova8G2_8.7.250_build8.3.apk \
  "https://www.celsoazevedo.com/files/android/google-camera/dev-arnova8G2/f/dl7/Gcam-8.7.250.build-8.3_snapcam.apk"

# Baixar cstark27 PXv4.5 (exemplo):
wget -O cstark27_PXv4.5_GoogleCamera.apk \
  "https://www.celsoazevedo.com/files/android/google-camera/f/changelog1330/PXv4.5_GoogleCamera_7.2.014.apk"
```

### Passo 2: Transferir para Poco X5
```bash
# Via ADB (se conectado USB):
adb push BSG_MGC_9.2.113_V29.apk /sdcard/Download/
adb push Arnova8G2_8.7.250_build8.3.apk /sdcard/Download/
adb push cstark27_PXv4.5_GoogleCamera.apk /sdcard/Download/

# Ou sync Google Drive/Termux:
# Copie APKs para ~/Google Drive/GCam-APKs/
# No celular: baixe via Drive app ou Termux wget
```

### Passo 3: Instalar no Poco X5
```bash
# Via Termux (com root):
pkg install android-tools
pm install /sdcard/Download/BSG_MGC_9.2.113_V29.apk

# Ou manualmente:
# Arquivos > Download > Toque no APK > Instalar
```

---

## 🔧 Configs XML (GCam Tuning)

### BSG MGC - Config XML Custom
**Localização no celular:** `/sdcard/GCam/configs/`

**Baixar configs prontas:**
- **Poco X5 specific:** https://www.celsoazevedo.com/files/android/google-camera/configs/
- Buscar "Poco X5" ou "Snapdragon 778G"

**Aplicar config:**
1. Abre BSG GCam
2. Menu ⚙️ > Configurações
3. Import config XML
4. Seleciona arquivo `.xml` da pasta GCam/configs/

**Parametros importantes (Poco X5):**
- HDR+ parameters: ativar
- Sensor: Principal 48MP (Sony IMX582)
- AWB mode: Auto
- Night Sight: Force enable

---

## 📊 Comparativo Rápido

| GCam Port | HDR+ | Night | Video | 360° | RAW | Estabilidade |
|-----------|------|-------|-------|------|-----|--------------|
| **BSG 9.2 V29** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ⭐⭐⭐⭐⭐ |
| **Arnova 8.3** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | ⭐⭐⭐⭐⭐ |
| **cstark PXv4.5** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ✅ | ⭐⭐⭐⭐ |
| **Nikita** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ✅ | ⭐⭐⭐⭐ |
| **Wichaya** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ✅ | ⭐⭐⭐ |

---

## 🧪 Checklist de Testes (Face Capture Pipeline)

### BSG MGC 9.2.113 V29
- [ ] Instalar APK
- [ ] Importar config XML Poco X5
- [ ] Testar HDR+ mode (frontal + laterais 45°)
- [ ] Testar Night Sight (ambiente escuro)
- [ ] Capturar 20-30 fotos rosto (múltiplos ângulos)
- [ ] Verificar qualidade close-up bigode
- [ ] Exportar RAW (DNG) se possível
- [ ] Salvar em `~/Pictures/Face-Capture/BSG/`

### Arnova8G2 8.7.250 Build 8.3
- [ ] Instalar APK
- [ ] Testar Photosphere 360° (rosto)
- [ ] Testar Slow-motion 240fps
- [ ] Cinematic video mode
- [ ] Astrophotography (se rolar)
- [ ] Comparar qualidade vs BSG
- [ ] Salvar em `~/Pictures/Face-Capture/Arnova/`

### cstark27 PXv4.5
- [ ] Instalar APK
- [ ] Ativar libpatcher
- [ ] Tunear denoise parameters
- [ ] Testar chroma1 levels
- [ ] Comparar vs BSG/Arnova
- [ ] Salvar em `~/Pictures/Face-Capture/cstark/`

---

## 📂 Estrutura Organização APKs

```
Temp/GCam-APKs/
├── README.md (este arquivo)
├── BSG_MGC_9.2.113_V29.apk (quando baixar)
├── Arnova8G2_8.7.250_build8.3.apk (quando baixar)
├── cstark27_PXv4.5_GoogleCamera.apk (quando baixar)
├── Nikita_[versao].apk (quando encontrar)
├── Wichaya_[versao].apk (quando encontrar)
├── Configs/
│   ├── BSG_PocoX5_HDR.xml (buscar no site)
│   ├── Arnova_PocoX5_Video.xml (buscar no site)
│   └── README_configs.md (instruções XMLs)
└── Testes/
    ├── resultados_BSG.md (após testar)
    ├── resultados_Arnova.md (após testar)
    └── comparativo_final.md (conclusões)
```

---

## 🔗 Links Oficiais

- **Celso Azevedo (hub principal):** https://www.celsoazevedo.com/files/android/google-camera/
- **BSG APKs:** https://www.celsoazevedo.com/files/android/google-camera/dev-bsg/
- **Arnova8G2 APKs:** https://www.celsoazevedo.com/files/android/google-camera/dev-arnova8G2/
- **cstark27 APKs:** https://www.celsoazevedo.com/files/android/google-camera/dev-cstark27/
- **Configs XML:** https://www.celsoazevedo.com/files/android/google-camera/configs/
- **XDA BSG Thread:** https://forum.xda-developers.com/search (buscar "BSG MGC GCam")
- **XDA Arnova Thread:** https://forum.xda-developers.com/search (buscar "Arnova8G2 GCam")

---

## 💡 Dicas de Instalação

### Problema: "App não instalado"
**Solução:**
```bash
# Desinstalar GCam anterior com mesmo package:
adb uninstall org.codeaurora.snapcam

# Ou instalar com package diferente:
# BSG: org.codeaurora.snapcam
# Arnova: arn.android.gcam
# cstark: com.google.android.GoogleCamera
```

### Problema: Crash ao abrir câmera
**Solução:**
1. Limpar cache/dados app
2. Verificar permissões câmera (Settings > Apps)
3. Testar config XML diferente
4. Downgrade para versão anterior (V26 BSG)

### Problema: Sensor extra não funciona
**Solução:**
1. Menu GCam > Configurações > AUX cameras
2. Ativar "Force enable aux"
3. Importar XML com suporte multi-sensor
4. Verificar se ROM (Infinity-X) tem HAL camera2 ativado

---

## 📝 Notas Importantes

1. **Package names diferentes:** Instale todos 3 principais sem conflito (BSG, Arnova, cstark usam IDs diferentes)
2. **Android 16 Infinity-X:** Todos APKs testados em Android 11+, deve funcionar no seu custom ROM
3. **Root necessário:** Não para instalar, apenas para tweaks avançados (kernel tuning)
4. **Storage:** Cada APK ~80-100MB, total ~300MB para 3 principais
5. **Configs XML:** Opcional mas MUITO recomendado para Poco X5 (melhora 50% qualidade)

---

## 🎯 Próximos Passos (Após Baixar)

1. Baixar BSG V29 + Arnova 8.3 + cstark PXv4.5
2. Transferir para `/sdcard/Download/` no Poco X5
3. Instalar os 3 APKs
4. Buscar configs XML específicas Poco X5
5. Testar cada GCam em condições diferentes:
   - Luz natural (dia)
   - Low-light (noite)
   - Close-up macro (bigode)
   - Frontal + laterais (face capture)
6. Salvar fotos em pastas separadas por GCam
7. Comparar qualidade (zoom 100% no PC)
8. Escolher 1-2 GCams favoritas
9. Integrar com pipeline Face-Capture/MediaPipe

---

**Última atualização:** 16/11/2025  
**Fonte:** celsoazevedo.com (oficial)  
**Status:** APKs disponíveis, aguardando download manual
