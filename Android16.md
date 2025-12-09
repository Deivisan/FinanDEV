# 📱 Android 16 – Stack Híbrido no POCO X5 5G

> **Objetivo:** consolidar todo o setup Android 16 (Infinity X) com KernelSU, Termux e Arch Linux em chroot em um único documento. Este arquivo substitui `Docs/arch-android-install.md` e `Docs/IncusArch.md`.

---

## 🧬 Snapshot Rápido

- **Dispositivo:** POCO X5 5G (8 GB / 256 GB)
- **ROM:** Android 16 – Infinity X (oficial)
- **Kernel:** 5.4.294-Darkmoon-KSU + KernelSU v1.0.9 (camuflagem Next ativa)
- **Root:** KernelSU + BusyBox completo
- **Userland:** Termux + Arch Linux ARM (chroot)
- **SSH Termux:** `u0_a717@192.168.25.2:8022` (IP dinâmico; conferir `../Android/Termux/docs/Termux.md`)
- **Status:** Ambiente estável e validado para desenvolvimento híbrido mobile ↔ desktop

---

## 🧩 Camadas do Ambiente

| Camada | Local / Comando | Função | Status |
| --- | --- | --- | --- |
| Android Host | Kernel 5.4.294-KSU | Permissões root, busybox, acesso a storage | ✅ estável |
| Termux | `/data/data/com.termux/` | Python 3.12.12, Node 22.21.1, Git 2.51, pacote `pkg` completo | ✅ produtivo |
| Arch Linux ARM | `/data/local/arch/` | Pacman (core/extra/community/alarm/aur) + toolchains ARM | ✅ 100% funcional |
| Script `arch-start.sh` | `/data/local/arch-start.sh` | Monta `/dev`, `/sys`, `/proc`, `/termux`, `/sdcard` e entra no chroot | ✅ testado |
| PRoot (fallback) | Termux + `proot-distro` | Sandbox leve caso precise isolamento extra | 🟡 opcional |

---

## 🛠️ Setup Validado

### Kernel & Root

- Kernel Darkmoon-KSU mantém cgroups v1+v2, mount e network namespaces ✅
- PID, user e IPC namespaces incompletos ❌ → containers (LXC/Incus/Docker/systemd-nspawn) descontinuados
- KernelSU + camuflagem Next mantêm apps bancárias operacionais

### Storage & Montagens

- Rootfs fica em `/data/local/arch/`
- Script principal: `/data/local/arch-start.sh`
- Bind mounts automáticos: `/dev`, `/sys`, `/proc`, `/dev/pts`, `/sdcard`, `/termux`
- DNS configurado manualmente em `/etc/resolv.conf` (8.8.8.8 / 1.1.1.1)

### Ferramentas Disponíveis

- **Termux:** Python 3.12.12, Node.js 22.21.1, npm 11.6, Git 2.51, BusyBox 1.36
- **Arch:** pacman atualizado; pacotes comuns (git, vim, base-devel, rust, etc.) rodam nativamente ARM
- **Helpers:** `arch-shell`, `arch-install`, `arch-update`, `arch-search` definidos no `~/.bashrc` do Termux

### Fluxo diário recomendado

1. Abrir Termux → `su -c /data/local/arch-start.sh`
2. Rodar `arch-update` (pacman -Syu) quando necessário
3. Instalar pacotes via `arch-install <pkg>` ou `pacman -S <pkg>`
4. Usar binários Termux montados em `/termux/usr/bin` para contornar GLIBC 2.38
5. Sincronizar projetos via git ou scripts rsync (executar no ambiente preferido)

---

## ⚠️ Limitações e Contornos

| Limitação | Impacto | Contorno |
| --- | --- | --- |
| Namespaces incompletos (PID/user/IPC) | Containers (LXC/Incus/Docker/systemd-nspawn) não suportados | Usar chroot direto ou PRoot apenas quando precisar isolamento |
| GLIBC 2.38 ausente no host | Alguns binários Arch falham | Montar Termux em `/termux/` para usar toolchain compatível |
| Filesystem raiz read-only | Precisa montar tudo em `/data/local/` e `/sdcard/` | Manter rootfs em `/data/local/arch/` (já adotado) |

---

## 🔁 Playbook Operacional

1. **Root shell:** `su`
2. **Start ambiente:** `su -c /data/local/arch-start.sh`
3. **Atualizar pacotes:** `pacman -Syuu` (quando necessário)
4. **Desenvolver:** rodar agentes CLI, scripts Python/Node ou compilar toolchains
5. **Encerrar:** `exit` para sair do chroot; script desmonta recursos

```bash
# Helpers Termux
arch-shell            # entra direto no chroot
arch-install <pkg>    # pacman -S <pkg>
arch-update           # pacman -Syu + limpeza de cache
```

---

## 📂 Estrutura Base

```text
/data/local/
├── arch/
│   ├── bin → usr/bin
│   ├── etc/
│   │   ├── resolv.conf
│   │   └── mtab
│   ├── usr/
│   ├── var/cache/pacman/
│   ├── sdcard → /sdcard
│   └── termux → /data/data/com.termux/files/usr
├── arch-start.sh
└── arch-dev.sh (helpers adicionais)
```

---

## 📡 Conectividade & Debug

- Rede compartilhada com o host Android; internet testada dentro do chroot
- SSH opcional: subir `sshd` no Arch e expor porta >8022 (USB/Wi-Fi)
- USB 2.0 limita throughput, então preferir Wi-Fi 5 GHz para sync pesado

---

## 🔐 Segurança

- KernelSU com camuflagem mantém apps bancárias operacionais mesmo com root
- Scripts limitam mounts apenas ao necessário; nada expõe `/data` sensível
- Recomenda-se backup periódico de `/data/local/arch/` + `~/arch-rootfs.tar.gz`

---

## 🧭 Roadmap

- **Curto prazo:** manter chroot estável, documentar updates pacman
- **Médio prazo:** testar PRoot como sandbox adicional
- **Longo prazo:** automatizar sync com desktop (rsync + WireGuard/ADB)

---

## 🧪 Troubleshooting

- **Containers não suportados** → namespaces incompletos; manter no chroot/PRoot
- **Pacman keys inválidas** → `pacman-key --init && pacman-key --populate archlinuxarm`
- **Sem DNS no chroot** → recriar `/etc/resolv.conf`
- **Binários quebrando por GLIBC** → usar `/termux/usr/bin/<binário>`

---



