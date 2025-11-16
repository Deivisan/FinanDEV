# 🖥️ Ambiente Dev - PCs Deivison

## 🏠 DeiviPC (Casa - Principal)

### 💻 Hardware
**Placa-mãe:** ASUS B450M Game (**NÃO B550!**)
**CPU:** AMD Ryzen 7 5700G
- Arquitetura: Zen 3
- Cores: 8 cores / 16 threads
- Clock base: 3.8 GHz
- Boost: até 4.6 GHz
- TDP: 65W
- Gráficos integrados: AMD Radeon Vega 8

**RAM:** 32GB (3 pentes: 8GB + 8GB + 16GB) dual-channel
- Tipo: DDR4
- Velocidade: Suporta até 3200 MHz

**Storage:** SSD 1TB NVMe
- Tipo: NVMe PCIe Gen3 x4
- Interface: M.2
- Velocidade leitura: ~3500 MB/s (estimado)
- Velocidade escrita: ~3000 MB/s (estimado)

**GPU:** AMD Radeon Vega 8 (integrada no APU)
- Compute Units: 8
- Clock: até 2000 MHz
- VRAM: Compartilhada (usa RAM)
- Performance: ~1.8 TFLOPS

**Rede:** 
- Ethernet: Realtek RTL8111 (1000Mbps)
- WiFi: [A PREENCHER]

**Áudio:** [A PREENCHER]

**Alimentação:** [A PREENCHER]

**Gabinete:** [A PREENCHER]

---

### 💿 Sistema Operacional

**Principal:** Arch Linux (Dual-boot com Windows 11)
- Kernel: 6.17.8-zen1-1-zen (PREEMPT_DYNAMIC)
- Desktop: COSMIC (Wayland) - upgrade de GNOME
- Display: 60fps
- Init: systemd
- Boot time: ~20s

**Secundário:** Windows 11 Pro

---

### 🛠️ Ferramentas e Software

**Shell:** Zsh 5.9 + Oh-My-Zsh + Powerlevel10k

**Linguagens Instaladas:**
- Python 3.13.7 (`/usr/bin/python3.13`) - pyenv + pipx + direnv
- Node.js v25.2.0 - nvm + pnpm/npm/yarn
- Rust 1.91.1 - cargo paralelo (-j 8)
- Go 1.25.4 - modules ativados
- Java 25.0.1 (OpenJDK)
- .NET 9.0.x (se instalado)

**CLI Tools:**
- Git 2.51.x
- fd, ripgrep, bat, eza, fzf, jq, yq
- htop, neofetch
- GNU parallel, xargs com paralelização

**IDEs:**
- Windsurf (principal)
- QODER (secundário)
- VS Code Insiders (extensões e MCPs)

**Agentes CLI:**
- Qwen-Code (Node.js)
- Gemini CLI
- GitHub Copilot CLI

**Gerenciadores de Pacotes:**
- pacman (899 pacotes)
- paru (AUR helper)
- flatpak (6 pacotes)

---

### ⚙️ Configurações e Otimizações

**Paralelismo:**
- Rust: `cargo -j 8 --release`
- GCC/Clang: `-O3 -march=znver3`
- Find/xargs: `xargs -P 8` (aproveita 8 cores)
- GNU parallel ativo

**Memória:**
- RAM física: 32GB
- ZRAM: Ativado (compressão)
- Swap: [A PREENCHER]

**Storage:**
- `/tmp` em tmpfs (builds rápidos)
- NVMe otimizado para I/O
- Cache em SSD

**Performance:**
- CPU governor: [A PREENCHER]
- I/O scheduler: [A PREENCHER]

---

### 🔗 Capacidades Especiais

**Para Desenvolvimento:**
- Docker/Podman: [A VERIFICAR]
- Virtualização: KVM/QEMU disponível (suporte AMD-V)
- Containers: LXC/LXD possível
- Cross-compilation: Rust + Go suportam

**Para Compilação:**
- C/C++: 3-5 min (médio, otimizado)
- Rust: ~5 min release com -j 8
- Python: Builds rápidos com pyenv

**Para ML/Data Science:**
- NumPy/Pandas: OK até ~2GB datasets
- TensorFlow/PyTorch: CPU-only (Vega 8 insuficiente)
- Paralelize: `joblib` ou `multiprocessing.Pool(8)`

**Para Multimídia:**
- FFMPEG: Hardware accel AMD disponível
- OBS: Streaming com Vega 8 (720p60 OK)

---

## 🏢 PC-UFRB (Trabalho - Backup)

### 💻 Hardware
**CPU:** Intel Core i5-3570 (Ivy Bridge)
- Cores: 4 cores / 4 threads
- Clock base: 3.4 GHz
- Turbo: 3.8 GHz
- TDP: 77W

**RAM:** 8GB DDR3-1600

**Storage:** 240GB SSD SATA
- Interface: SATA III 6Gb/s
- Velocidade leitura: ~500 MB/s
- Velocidade escrita: ~450 MB/s

**GPU:** Intel HD Graphics 2500 (integrada)

**Rede:** 
- IP fixo: 172.17.14.166
- Ethernet: [A PREENCHER]

---

### 💿 Sistema Operacional

**Principal:** Windows 11 Pro

---

### 🛠️ Ferramentas e Software

**Uso Principal:** 
- Trabalho CETENS/UFRB
- Backup e suporte
- Tarefas administrativas

**Software Instalado:** [A PREENCHER]

---

### ⚙️ Limitações Conhecidas

**Performance:**
- CPU antiga (2012) - 4 cores apenas
- RAM limitada (8GB DDR3)
- Sem GPU dedicada

**Uso Recomendado:**
- Tarefas leves/administrativas
- Navegação web
- Documentos/planilhas
- Backup secundário

---

## 📊 Comparativo DeiviPC vs PC-UFRB

| Característica | DeiviPC | PC-UFRB |
|---|---|---|
| **CPU** | Ryzen 7 5700G (8c/16t) | i5-3570 (4c/4t) |
| **RAM** | 32GB DDR4-3200 | 8GB DDR3-1600 |
| **Storage** | 1TB NVMe (~3500MB/s) | 240GB SATA (~500MB/s) |
| **GPU** | Vega 8 (1.8 TFLOPS) | HD 2500 (básico) |
| **OS** | Arch Linux ZEN / Win11 | Windows 11 Pro |
| **Ano CPU** | 2021 (Zen 3) | 2012 (Ivy Bridge) |
| **Performance** | Alto (~10x UFRB) | Básico |
| **Uso** | Dev principal, ML, compilação | Trabalho, backup |

---

## 🎯 Recomendações de Uso

**DeiviPC (Casa):**
- ✅ Desenvolvimento Python/Rust/Go/Node
- ✅ Compilações pesadas (8 cores!)
- ✅ Datasets médios (até 2GB)
- ✅ Containers/VMs
- ✅ Streaming/gravação
- ✅ Multitarefa intensa

**PC-UFRB (Trabalho):**
- ✅ Tarefas administrativas
- ✅ Documentos/emails
- ✅ Navegação web
- ❌ Desenvolvimento pesado
- ❌ Compilações grandes
- ❌ Multitarefa intensa

---

## 🔮 Próximas Expansões

- [ ] Preencher detalhes WiFi DeiviPC
- [ ] Verificar swap/zram config
- [ ] Documentar aliases zsh específicos
- [ ] Testar performance containers
- [ ] Benchmarks reais (compilação, I/O)
