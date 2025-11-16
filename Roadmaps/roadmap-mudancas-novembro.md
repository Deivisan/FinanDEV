# 🗺️ Roadmap de Mudanças - Novembro 2025

> **Baseado em:** 2 conversas Grok (460 + 166 mensagens)  
> **Status:** 🚧 Em Implementação Agêntica  
> **Última Atualização:** 16/11/2025 09:00  
> **Conversas:**
> - 16/11 02:12-04:32 (460 msgs) - Refatoração FinanDEV + mini-sistemas
> - 16/11 07:00-09:00 (166 msgs) - Camerologia, Face-Capture, Finanças Auto, Emails

---

## 📋 Índice de Mudanças

- [Repositório Base (FinanDEV)](#repositório-base)
- [Mini-Sistemas Identificados](#mini-sistemas)
- [Novos Repositórios](#novos-repositórios)
- [Migrações de Formato](#migrações)
- [Metas de Trabalho (CETENS)](#metas-trabalho)
- [Sistemas Sociais](#sistemas-sociais)
- [Tecnologias e Ferramentas](#tecnologias)

---

## 🏗️ Repositório Base (FinanDEV)

### ✅ Mudanças Concluídas
- [x] Migração TXT → Markdown (transcrições estruturadas)
- [x] Criação pasta `Backup/` (README-ANTIGO, README-REFATORACAO)
- [x] Atualização specs hardware (B450M ASUS, 32GB 3 pentes, Cloud Sonnet 4.5)
- [x] PROMPT-MODO-VOZ.md criado (447 linhas)
- [x] Vida-Deivison.json v1.1.0 (setup_tecnico adicionado)
- [x] .gitignore configurado

### 🚧 Mudanças Pendentes

#### 1. Renomeação do Repositório
**De:** `FinanDEV` (finanças de desenvolvedor)  
**Para:** *A definir* - opções discutidas:
- `DevCore` (núcleo desenvolvedor)
- `VidaScript` (vida em código)
- `BackupMental` (literal)

**Razão:** Evoluiu de finanças para backup mental completo.

#### 2. Sistema de Última Atualização
- **Problema:** Timestamp geral não reflete edições individuais (DevTech.md foi 5 dias atrás, mas mostra mais antigo)
- **Solução:** Script automático no commit que atualiza campo de data em cada MD editado
- **Local:** Rodapé de cada Markdown principal

#### 3. Estrutura de Pastas
**Nova hierarquia:**
```
FinanDEV/
├── Base/           # Docs fundamentais (specs, stack, workspace)
├── Rotinas/        # Rotinas diárias e semanais
├── Transcricoes/   # Conversas capturadas (formato novo)
├── Temp/           # Rascunhos, questionários temporários
├── Backup/         # Versões antigas (já existe)
├── Roadmaps/       # Este arquivo e futuros (já existe)
└── Mini-Sistemas/  # Sistemas individualizados (criar)
```

**Mover para Temp/:**
- README-REFATORACAO.md
- QUESTIONARIO-LACUNAS.md
- Futuros questionários de agentes

---

## 🔧 Mini-Sistemas Identificados

### 1. Sistema de Moda e Corpo (ROTINA-FISICA.md)
**Objetivo:** Rastrear evolução visual e física  
**Componentes:**
- **Fotos periódicas:** Corpo (frontal, lateral, costas)
- **Vestimenta:** Peças do dia com descrição (ex: "camisa preta oversized, calça cargo")
- **Peso semanal:** Integrar meta 60kg → 70kg (maio 2026)
- **Notas estilo:** Transição de "roupas herdadas do irmão" → escolhas pessoais

**Formato:**
```markdown
## 2025-11-16
**Peso:** 62kg  
**Outfit:** Camisa preta básica, jeans rasgado, tênis branco  
**Foto:** /fotos/corpo/2025-11-16.jpg  
**Nota:** Primeira peça comprada por mim - camisa oversized preta
```

**Status:** 📝 A criar

---

### 2. Sistema de Saúde Mental (SAUDE-MENTAL.md)
**Objetivo:** Monitorar padrões de sono, energia, humor  
**Componentes:**
- **Sono:** Horas + qualidade (0-10)
- **Energia diária:** Escala 0-10
- **Humor pós-trabalho:** Neutro/Positivo/Negativo + nota
- **Padrões de estresse:** Relação com CETENS e finanças

**Formato:**
```markdown
## Semana 16-22/11/2025
| Dia | Sono | Energia | Humor | Notas |
|-----|------|---------|-------|-------|
| 16  | 5h   | 4/10    | Neutro | Madrugada coding, CETENS tedioso |
```

**Integração:** Cruzar com alimentação e rotina para detectar padrões

**Status:** 📝 A criar

---

### 3. Sistema de Aprendizados Semanais (LEARNINGS.md)
**Objetivo:** Extrair insights de transcrições semanais  
**Componentes:**
- **Input:** Transcrições da semana (Temp-Transcrições)
- **Processamento:** Agente extrai:
  - Confirmações/Decisões tomadas
  - Correções de specs/dados
  - Ideias novas (mini-sistemas, repos)
  - Padrões comportamentais
- **Output:** Resumo semanal com tags vetoriais

**Formato:**
```markdown
## Semana 10-16/11/2025
**Transcrições processadas:** 3 (conversa-scrape, CETENS-update, grupo-amigos)

### Decisões Finais
- ✅ Migrar transcrições TXT → MD estruturado
- ✅ Criar Temp-Transcrições universal

### Novas Inclinações Captadas
- Disruptividade profissional (não baixar ritmo para outros)
- Autossuficiência como barreira e liberdade

### Correções Técnicas
- Hardware: B450M ASUS (não B550)
- RAM: 32GB em 3 pentes (8+8+16)
```

**Status:** 📝 A criar

---

### 4. Sistema de Aliases Modo Voz (ALIASES-VOZ.md)
**Objetivo:** Atalhos de comando para interações rápidas com IA  
**Componentes:**
- **Aliases de repo:** `repo-finandev`, `repo-X`, `modo-refator`
- **Aliases de contexto:** `ctx-trabalho`, `ctx-casa`, `ctx-madrugada`
- **Aliases de ação:** `captura-agora`, `resume-hoje`, `commit-urgente`

**Exemplo de uso:**
```
Deivison (voz): "repo-finandev, modo-refator, captura-agora"
Grok: [Abre FinanDEV, ativa modo refatoração, inicia captura de voz]
```

**Status:** 💡 Planejado (não implementado)

---

### 5. Sistema Backbrowser (SLEEP-TRACKING.md)
**Objetivo:** Rastreamento automático de sono/energia  
**Componentes:**
- **Fonte:** Browser history + timestamps de atividade
- **Detecção:** Último comando terminal, último commit GitHub
- **Inferência:** "Dormiu às 04:30 (última atividade), acordou às 12:00 (primeiro commit)"
- **Output:** Gráficos semanais de sono

**Tecnologia:** Script Python + cron job + análise de logs

**Status:** 💡 Planejado (mencionado na conversa)

---

## 🆕 Novos Repositórios

### 1. Temp-Transcrições (UNIVERSAL)
**Nome:** `Temp-Transcricoes`  
**Descrição:** Backup universal de TODAS as transcrições, independente do repo de origem  
**Estrutura:**
```
Temp-Transcricoes/
├── 2025-11/
│   ├── 16-scrape-refatoracao-finandev.md
│   ├── 16-tedino-cetens-madrugada.md
│   └── 17-grupo-amigos-rifa.md
└── README.md (metodologia de captura)
```

**Características:**
- **Formato:** Markdown estruturado com emojis (👤 Deivison / 🤖 Grok)
- **Metadados:** Data, hora, duração, fonte (Grok/Gemini/Qwen)
- **Título:** Gerado automaticamente pelo agente (`data-topico-repo.md`)
- **Commit:** Automático após cada captura (script Node.js + Playwright)
- **Função:** Cofre infinito - se perder tudo, esse repo salva

**Status:** 🚧 Criar (prioridade alta)

---

### 2. Orquestração-Settings
**Nome:** `Orquestracao-Settings`  
**Descrição:** Meta-repositório de orquestrações diárias/semanais  
**Conteúdo:**
- Mini-tarefas diárias (CETENS, projetos pessoais)
- Tracking de progresso (antes de sair em dezembro)
- Configurações de bots e automações

**Status:** 📝 Mencionado (já existe?)

---

### 3. Grupo-Amigos (Sistema Social)
**Nome:** `Grupo-Amigos-Bot`  
**Descrição:** Banco vetorial de amigos para automação social  
**Componentes:**
- **Perfis:** OCR de fotos → rostos vetorizados
- **Dados:** Finanças, metas, interações passadas
- **Bot WhatsApp:** Vídeos personalizados, rifas coletivas, mini-sistemas sociais
- **IA Generativa:** Deepfakes personalizados (rostos + prompts)

**Exemplo de uso:**
```markdown
## João Silva
**Foto vetorial:** /rostos/joao-silva.vec
**Último contato:** 10/11/2025
**Meta compartilhada:** Juntar R$500 para almoço coletivo
**Próxima rifa:** 20/11/2025 (R$10/pessoa)
```

**Status:** 💡 Meta pequena (fazer quando tiver tempo)

---

### 4. Grupo-Ateus v4.0
**Nome:** `Ateus-Debates`  
**Descrição:** Revitalização do grupo de debates lógicos  
**Componentes:**
- **Bot de debates:** Argumentos vetorizados (lógica crua, sem dogma)
- **Expansão:** Facebook, outros grupos
- **Conteúdo:** Posts automáticos, respostas baseadas no repo

**Status:** 💡 Planejado mas nunca foi à frente (branch experimental)

---

## 🔄 Migrações de Formato

### 1. Transcrições: TXT → Markdown Estruturado
**Status:** ✅ Decidido | 🚧 Implementação pendente (agente aplicará)

**De:**
```
Texto cru sem formatação
Deivison falando
Grok respondendo
Sem separação visível
```

**Para:**
```markdown
# 🗣️ Transcrição - Tópico Descritivo

> **Data:** 16/11/2025 02:12-04:32  
> **Duração:** 2h20min  
> **Fonte:** Grok Modo Voz  
> **Capturado via:** Metodologia Script.md (Playwright)

---

### 👤 Deivison
Texto da fala dele aqui...

### 🤖 Grok
Resposta do Grok aqui...
```

**Vantagens:**
- **Humano-legível:** Fácil revisar conversas antigas
- **Agente-legível:** Tags estruturadas para indexação vetorial
- **Metadados preservados:** Data, duração, fonte
- **Navegação:** Headings facilitam busca

**Script atualizar:** `Docs/scrape.js` → adicionar formatação MD + emojis + metadados

---

### 2. JSON Vetorial → Markdowns Temáticos
**Status:** 📋 Planejado

**Vida-Deivison.json é denso demais.** Quebrar em:
- `PERFIL.md` (dados pessoais, psicológico)
- `FINANCAS.md` (salário, sobra, investimentos)
- `ALIMENTACAO.md` (2400 kcal/dia, despensa ativa)
- `ROTINAS-SEMANA.md` (segunda-domingo granular)
- `METAS.md` (peso, trabalho, 2026)
- `SETUP-TECNICO.md` (PC pessoal, trabalho, celular, agentes IA)

**JSON permanece como fonte de verdade,** MDs são humano-friendly.

**Agente sincroniza:** Mudanças em MD → atualiza JSON automaticamente.

---

## 💼 Metas de Trabalho (CETENS)

### Meta Principal: Sair em Paz (Dezembro 2025)
**Deadline:** 30/12/2025 (44 dias restantes a partir de 16/11)

#### Checklist de Saída
- [ ] **Upgrade Hardware:**
  - [x] Orçamento aprovado (8GB RAM para todos)
  - [ ] Instalar 8GB em TODOS os Dell OptiPlex 7010
  - [ ] Adicionar SSD nos setores mais movimentados
  - [ ] Formatar máquinas com Windows 7 → Windows 10

- [ ] **Sistema OK:**
  - [ ] Todos os setores com programas instalados e configurados
  - [ ] Drivers atualizados (rede, áudio, vídeo)
  - [ ] Zerar chamados pendentes
  - [ ] Documentar setup de cada setor (MD com specs + softwares)

- [ ] **Automação Silenciosa:**
  - [ ] Scripts de manutenção automatizados (limpeza, updates)
  - [ ] Manual de troubleshooting para próximo dev (se houver)

- [ ] **Estado Final:**
  - [ ] Sistema funciona 3-6 meses sem suporte externo
  - [ ] Chefe satisfeito (modo passivo dele facilita)
  - [ ] Legado deixado: "Extraí o máximo da geração passada"

**Tempo diário disponível:** 6-8h (trabalho ócio, sem chamados)  
**Estratégia:** Mini-tarefas diárias no Orquestração-Settings

---

### Meta Tecnológica 2026: Novo Ambiente
**Objetivo:** Encontrar trabalho com:
- Avanços tecnológicos reais (IA, ML, computação quântica)
- Time que acompanha ritmo disruptivo
- Liberdade para inovar sem barreiras burocráticas

**Ação atual:** Mapear empresas/startups em Feira de Santana/Salvador

---

## 👥 Sistemas Sociais

### 1. Grupo de Amigos - Reestruturação v2.0
**Componentes:**
- **Bot WhatsApp:** Vídeos personalizados (rostos via OCR + IA generativa)
- **Rifas coletivas:** Sistema de contribuição (R$10/pessoa para almoço mensal)
- **Prompts inteligentes:** Banco vetorial de personalidades
- **Mini-sistemas:**
  - Casa de alguém? → Post no grupo com contribuição
  - Aniversário? → Vídeo deepfake personalizado

**Lançamento:** Atualização surpresa em uma madrugada (grupo acorda diferente)

---

### 2. Grupo Ateus v4.0
**Componentes:**
- **Bot de debates:** Argumentos lógicos vetorizados
- **Expansão:** Posts automáticos Facebook
- **Conteúdo:** Ateísmo lógico, sem dogma

**Status:** Branch experimental (prometido mas nunca feito)

---

## 🛠️ Tecnologias e Ferramentas

### 1. Meta de Vídeo IA (2026)
**Objetivo:** Criar vídeos personalizados sem limitação  
**Requisitos:**
- **Modelo:** Stable Video Diffusion, Runway (open-source preferido)
- **Prompts vetoriais:** Descrição de traços, expressões, roupas
- **Rostos:** OCR + vetorização para deepfakes perfeitos

**Uso:** Grupos WhatsApp, conteúdo DeiviTech, experimentos pessoais

---

### 2. Scrape v3.0 → v4.0 (Playwright)
**Melhorias pendentes:**
- **Batch mode:** Capturar múltiplos links em paralelo
- **Diff comparison:** Detectar mudanças entre capturas
- **Validação web:** Checar se info está desatualizada
- **Double-run:** Capturar 2x, comparar, confirmar integridade

**Limitações conhecidas:**
- **Contexto cheio (>60%):** Busca web trava, chat congela
- **Solução:** Agente pausa, faz dump, limpa 20% buffer, retoma

**Max captura:** 2MB de Markdown (24h de conversa) = 15s de processamento

---

### 3. Aliases e Prompts Modo Voz
**Sistema de atalhos para Grok/Gemini/Qwen:**
- `repo-X` → Abre repositório X
- `modo-refator` → Ativa modo refatoração
- `captura-agora` → Inicia gravação de voz
- `resume-hoje` → Resumo do dia baseado em commits/transcrições

**Implementação:** PROMPT-MODO-VOZ.md expandido com seção de aliases

---

## 📊 Conversões Planejadas

### JSON → Markdown
**Vida-Deivison.json (286 linhas) quebrar em:**
1. `PERFIL.md` - Dados pessoais, psicológico
2. `FINANCAS.md` - Salário dinâmico (±100 reais/mês), sobra
3. `ALIMENTACAO.md` - 2400 kcal, despensa ativa
4. `ROTINAS-SEMANA.md` - Segunda-domingo
5. `METAS-2026.md` - Peso 70kg, novo trabalho
6. `SETUP-TECNICO.md` - PC, celular, agentes IA

**Sincronização:** Agente monitora MDs, atualiza JSON automaticamente

---

## 🔍 Traços Psicológicos Captados (para refinar Deivison.md)

### Novas Inclinações Identificadas
- **Disruptividade profissional:** Não reduz ritmo para caber em moldes alheios
- **Autossuficiência:** Barreira natural (desinteresse em quem não agrega valor único)
- **Frustração CETENS:** Ambiente "parado no tempo" vs. mente acelerada
- **Moda como autoexpressão:** Transição "roupas herdadas" → escolhas pessoais
- **Teste de limites:** Personalidade de "cutucar até quebrar" (sistemas, pessoas, IA)

### Atualizar Deivison.md
Adicionar seção **Visão de Mundo:**
- Crítica ao "jeitinho brasileiro" (amiguismo vs. mérito lógico)
- Mudança de mentalidade como root de transformação social
- Pensamento fora da curva (IDH, QI) sem garantia de estar certo

---

## 📅 Cronograma de Implementação

### Prioridade ALTA (Novembro 2025)
1. ✅ Criar Roadmaps/ + este arquivo
2. 🚧 Criar Temp-Transcrições (repo universal)
3. 🚧 Atualizar scrape.js para MD estruturado
4. 🚧 Migrar questionários para Temp/
5. 🚧 Sistema de última atualização (script auto)

### Prioridade MÉDIA (Novembro-Dezembro 2025)
6. Criar Mini-Sistemas/ (moda, saúde mental, learnings)
7. Quebrar Vida-Deivison.json em MDs temáticos
8. Meta CETENS: Upgrade completo até 30/12
9. Atualizar Deivison.md com traços psicológicos novos

### Prioridade BAIXA (2026)
10. Grupo-Amigos-Bot (vetorização rostos + rifas)
11. Grupo-Ateus v4.0 (debates lógicos)
12. Sistema de Aliases Voz
13. Backbrowser (sleep tracking automático)
14. Meta de Vídeo IA (deepfakes personalizados)

---

## 🤖 Para o Agente Aplicar

### Instruções de Execução Agêntica
1. **Ler este roadmap completamente** antes de agir
2. **Marcar tarefas como in-progress** no manage_todo_list
3. **Executar em ordem de prioridade** (ALTA → MÉDIA → BAIXA)
4. **Commitar incrementalmente** (não esperar tudo ficar pronto)
5. **Atualizar este roadmap** conforme progresso (checkboxes ✅)
6. **Criar MDs individuais** para cada mini-sistema
7. **Documentar decisões** em comentários de commit

### Arquivos a Criar
- [ ] `Mini-Sistemas/ROTINA-FISICA.md`
- [ ] `Mini-Sistemas/SAUDE-MENTAL.md`
- [ ] `Mini-Sistemas/LEARNINGS.md`
- [ ] `Mini-Sistemas/ALIASES-VOZ.md`
- [ ] `Mini-Sistemas/SLEEP-TRACKING.md`
- [ ] `PERFIL.md`, `FINANCAS.md`, `ALIMENTACAO.md`, etc. (conversão JSON)
- [ ] Repo externo: `Temp-Transcricoes`

### Arquivos a Mover
- [ ] `Contexto/README-REFATORACAO.md` → `Temp/`
- [ ] `Contexto/QUESTIONARIO-LACUNAS.md` → `Temp/`

### Scripts a Atualizar
- [ ] `Docs/scrape.js` → adicionar formatação MD + emojis + metadados
- [ ] Criar script de última atualização (auto-commit)

---

---

## 🚀 NOVA CAPTAÇÃO - Conversa 16/11 07:00-09:00 (166 mensagens)

### 📁 Ambiente-Dev - Documentação Completa Setup

**Criado:** `Ambiente-Dev/` (estrutura completa para contexto agentes)

**Objetivo:** Centralizar specs hardware/software (PC, Celular, Estoque) para agentes entenderem ambiente real

**Estrutura:**
```
Ambiente-Dev/
├── README.md (índice master)
├── PC/ (specs pessoal + trabalho - A PREENCHER)
├── Celular/ (Poco X5 + mods)
│   └── Camerologia/ (sistema testes GCam)
├── Estoque/ (inventário TI - A PREENCHER)
└── Face-Capture/ (pipeline vectorização rosto)
```

**Integração:** Referenciado em PROMPT-MODO-VOZ.md como contexto obrigatório

---

### 📷 Camerologia - Sistema Testes GCam (Poco X5)

**Arquivos:**
- `Ambiente-Dev/Celular/Camerologia/README.md` (285 linhas)
- `Ambiente-Dev/Celular/Camerologia/gcam-ports-lista.md` (92 linhas)

**5 Portes GCam para Testar:**
1. **MGC 9.4.103_V22** (Sept 2025) - Stable, HDR+ confiável
2. **MGC 9.6.113_V0.1_beta** (Nov 10) - IA auto-stitching panoramas
3. **LMC 8.4 R18** (Hasli) - HDR+ ultra para interiores + RAW
4. **AGC 9.4_V0.3** - XML ativa 3 sensores (48MP+8MP+2MP)
5. **AGC 9.6.24** - Beta experimental (features Pixel, instável)

**Features Checklist:**
- HDR+, Night Sight, Panorama 360°, 4K 60fps
- Ultra-Wide, Macro, RAW export, Stitching quality

**Usos Estratégicos:**
1. **Face Vectorial:** 20-30 fotos → MediaPipe → SVG
2. **Setup 360°:** Panoramas ambiente dev (backup visual)
3. **Treinos 4K:** Vídeos exercícios (análise form)

**Status:** ⚪ Todos checkboxes vazios (aguardando testes reais)

**Automação:** Scripts Termux (auto-capture, debug USB)

**Download:** celsoazevedo.com/files/android/google-camera/dev-bsg

---

### 🎭 Face-Capture - Pipeline Vectorização Rosto

**Arquivo:** `Ambiente-Dev/Face-Capture/README.md` (272 linhas)

**Pipeline 5 Fases:**

**1. Captura (GCam):**
- 20-30 fotos: frontal, laterais 45°, close-ups bigode
- RAW, iluminação neutra

**2. Processamento (MediaPipe):**
- Face Mesh → 468 landmarks 3D (x,y,z coords)
- Edge detection detalhes finos
- Output: `foto.jpg.json` com coordenadas normalizadas

**3. Vectorização:**
- **Online:** Vectorizer.AI, Recraft.ai, Vector Magic
- **Offline:** Potrace, Autotrace (CLI)
- Output: SVG escalável infinito

**4. Alternativa 3D Scan:**
- **Polycam** (melhor - 1-2min scan)
- **KIRI Engine** (web AR)
- **Ready Player Me** (avatar instant)
- Output: OBJ/STL para Blender

**5. Animação:**
- **Lottie JSON:** Bodymovin export After Effects
- **CSS+SVG:** Keyframes transform
- **Stable Diffusion+ControlNet:** Gerar vídeo animado

**Uso Final:** Asset "puxar cortina" no site DeiviTech (rosto Deivison custom)

**Script Exemplo:**
```python
import mediapipe as mp
mp_face_mesh = mp.solutions.face_mesh
# Processa foto.jpg → landmarks JSON
```

---

### 💰 Finanças-Automatizadas - Pix + Blockchain (BRAINSTORM)

**Arquivo:** `Ideias/Financas-Automatizadas.md` (198 linhas)

**Conceito:** Centralizar finanças (Pix Automático + USDC stablecoins + audit blockchain)

**Componentes:**

**Pix Automático (Junho 2025):**
- Autoriza 1x → auto-executa mensalmente
- Uso: Suplementos (R$300/mês), Google Drive (R$6.99), doações grupo

**Blockchain:**
- USDC/USDT (Ethereum, Solana, Polygon) - evita volatilidade
- Bridges: AEON Pay, Zypto (crypto → Pix QR)
- Audit transparente: blockchain explorer público

**Dashboard FinanDEV:**
- Frontend: Next.js
- Backend: Python Flask API
- Storage: JSON + blockchain

**Stack:**
- Stripe Pix API (2.9% fee)
- Volt.io (automação)
- Web3.py (wallet management)

**Roadmap:**
1. MVP: Stripe Pix only
2. Blockchain: USDC wallet integration
3. Dashboard: Full UI
4. Audit: Explorer público

**Limitações:**
- Google Cloud precisa cartão (mesmo free tier)
- Crypto fees 1-3%
- Regulação incerta

**Alternativa:** Playwright automation (zero custo, funciona hoje)

---

### 📧 Pendências - Email Cleanup Automation

**Arquivo:** `Pendencias/Emails-Organizacao.md` (362 linhas)

**Problema:** 1600+ emails spam bloqueando respostas vagas emprego

**Solução:** Playwright headless automation (sem API, custo zero)

**3 Scripts Python:**

**1. email-setup.py:**
- Login manual 1x
- Auto-clica "Aceitar cookies" (múltiplos seletores)
- Salva session JSON

**2. email-cleanup.py:**
- Headless deletion em lotes
- Random delays (0.5-1.5s anti-block)
- Progress tracking

**3. email-organize.py:**
- Filtra "vaga OR currículo"
- Aplica label "Vagas"
- Cria subpastas

**Features Anti-Blocking:**
- Cookie banner detection (Gmail, Outlook, genérico PT/EN)
- User-agent rotation
- Session restoration
- Rate limits: ~100 emails/min Gmail, ~80/min Outlook

**Uso:** Setup 1x → roda headless forever, sem re-login

---

### 📸 Pendências - Google Photos Organização

**Arquivo:** `Pendencias/Google-Photos-Organizacao.md` (280 linhas)

**Objetivo:** Organizar fotos em álbuns (Físico 2025, Ambiente Dev, Treinos)

**2 Abordagens:**

**API (Official):**
- Google Photos Library API
- OAuth, metadata access
- **Requer:** Google Cloud + cartão

**Playwright (Free):**
- Browser automation
- **Zero custo**, funciona hoje
- Mais lento

**Scripts:**

**google-photos-api.py:**
- Autentica 1x
- Lista fotos
- Cria álbuns
- Adiciona em lote (data/local/faces)

**google-photos-playwright.py:**
- Salva session
- Cria álbuns
- Busca por data
- Seleciona + adiciona

**Filtros:**
- **Data:** Últimos 30 dias, 2025-11
- **GPS:** Proximidade casa (lat/lon)
- **Faces:** Google auto-detect, filter personId

**Casos Uso:**
- "Físico 2025": Progresso corpo (quinzenal)
- "Ambiente Dev": Panoramas 360° setup (anual)
- "Treinos": Vídeos 4K exercícios

**Futuro:** IA categorização (Vision API), cron Domingos 20:00

---

### 📊 Resumo Nova Captação (166 mensagens)

**7 Sistemas Criados:**
1. ✅ Ambiente-Dev/ - Contexto setup completo
2. ✅ Camerologia/ - 5 GCam ports + checklists
3. ✅ Face-Capture/ - Pipeline 5 fases vectorização
4. ✅ Finanças-Automatizadas - Pix + blockchain brainstorm
5. ✅ Emails-Organizacao - Playwright cleanup 1600 spans
6. ✅ Google-Photos-Organizacao - API + Playwright albums
7. ✅ gcam-ports-lista.md - Specs detalhadas ports

**Arquivos Criados:** 7 MDs (1539+ linhas)

**Folders Criados:** 8 (Ambiente-Dev/, PC/, Celular/, Camerologia/, Face-Capture/, Estoque/, Ideias/, Pendencias/)

**Status Implementação:**
- Documentação: ✅ 100%
- Testes reais: ⚪ Aguardando (GCam, fotos, scripts)

**Prioridades:**
1. **ALTA:** Testar GCam ports → preencher checklists reais
2. **ALTA:** Capturar 20-30 fotos rosto → MediaPipe processing
3. **ALTA:** Implementar email-cleanup.py (testar 10 emails primeiro)
4. **MÉDIA:** Preencher Ambiente-Dev/PC/ + Estoque/
5. **BAIXA:** Protótipos (blockchain MVP, animações Lottie)

---

## 📝 Notas Finais

**Este roadmap é vivo.** Cada conversa com Grok/Gemini pode adicionar:
- Novos mini-sistemas
- Correções de specs
- Mudanças de prioridade

**Agente DevSan (Cloud Sonnet 4.5)** aplicará mudanças autonomamente com base neste mapa.

**Capturas:**
- **1ª conversa:** 16/11/2025 02:12-04:32 (460 msgs, 2h20min)
- **2ª conversa:** 16/11/2025 07:00-09:00 (166 msgs, 2h)

**Próxima revisão:** Após testes GCam + face capture reais

---

*Gerado por DevSan a partir de 2 conversas (626 msgs total) | Auto-aprovado | Poder máximo* 🚀
