# 📱 GCam Ports - Lista Completa Testagem

> **Poco X5 +

> **Última atualização:** 16/11/2025

---

## 🎯 Ports Recomendados (Novembro 2025)

### 1. MGC 9.4.103_V22 (BSG)

- **Fonte:** celsoazevedo.com/files/android/google-camera/dev-bsg

- **Lançamento:** Setembro 2025

- **Foco:** HDR+ geral, Night Sight estável

- **Snapdragon 778G:** Otimizado ✅

- **Reviews:** Menos crashes, stitching panorama top

### 2. MGC 9.6.113_V0.1_beta (BSG)

- **Fonte:** celsoazevedo.com/files/android/google-camera/dev-bsg

- **Lançamento:** 10/11/2025

- **Foco:** IA nova (auto-stitching, denoising avançado)

- **Snapdragon 778G:** Beta maduro, poucos bugs

- **Reviews:** XDA/Reddit - suave no Poco X5

### 3. LMC 8.4 R18 (Hasli/Arnova)

- **Fonte:** celsoazevedo.com/files/android/google-camera/dev-hasli

- **Foco:** HDR+ ultra para interiores, RAW export

- **Uso:** Ideal para fotos setup dev (detalhes cabos, telas)

- **Reviews:** Queridinha para ambientes complexos

### 4. AGC 9.4_V0.3 (Config XML)

- **Tipo:** Arquivo de configuração (não APK)

- **Uso:** Carrega em MGC 9.4 para ativar sensores extras

- **Recurso:** 48MP completo + ultra-wide + macro simultâneos

### 5. AGC 9.6.24_V0.X (Beta experimental)

- **Foco:** Recursos IA Pixel novos (ainda instável no Poco X5)

- **Testar:** Quando sair versão estável

---

## Links Úteis

- [Celso Azevedo GCam Hub](https://celsoazevedo.com/files/android/google-camera)

- XDA Developers: <https://forum.xda-developers.com/t/gcam-google-camera-port.3910259/>

---

## 🛠️ Configs XML Recomendadas

### Para MGC 9.4

- AGC9.4_V0.3.xml

- Ativa: 48MP sensor principal

- Ativa: Ultra-wide 8MP

- Ativa: Macro 2MP

- HDR+ Enhanced padrão

### Para MGC 9.6

- AGC9.6_Beta_Config.xml (quando disponível)

---

## 🧪 Protocolo de Teste

1. Baixar APK

2. Instalar via ADB ou manual (root permite ambos)

3. Abrir GCam → Configurações → Carregar XML (se aplicável)

4. Testar checklist completa (ver README.md principal)

5. Anotar resultados: funciona/bugs/crash

6. Comparar qualidade output (mesma cena, diferentes ports)

---

## 📊 Sensores a Verificar em Cada Port

- [ ] Sensor principal 48MP ativo?

- [ ] Ultra-wide 8MP funciona?

- [ ] Macro 2MP captura close-up?

- [ ] Giroscópio para estabilização ativo?

- [ ] Night Sight captura até 3 lux?

- [ ] Panorama 360° stitching suave?

- [ ] Filmagem 4K 60fps estável?

- [ ] RAW DNG export funciona?

---

| ⏳ | Testando face capture integrado |

---

> 📝 Documentação viva - Atualizar conforme novos ports lançarem
