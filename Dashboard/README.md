# 📊 Dashboard FinanDEV - Painel Controle Centralizado

> **Objetivo:**

> **Stack:**

> **Status:**

> **Criado:** 16/11/2025

---

## 🎯 Visão Geral

Dashboard único que centraliza:

- 📈 **Métricas Vida:** Peso, calorias, proteínas, sono, humor

- 💰 **Finanças:** Saldo, gastos quinzenais, economia vs orçamento

- ✅ **Tarefas:** Pendências, mini-sistemas status, commits semana

- 📸 **Progresso Físico:** Timeline fotos corpo (quinzenal)

- 🎯 **Metas:** 70kg maio/2026, 100g proteína/dia, R$1086 sobra/mês

- 🔧 **Ações Rápidas:** Adicionar peso, registrar humor, commit automático

---

## 🏗️ Arquitetura

### Frontend (index.html + style.css + app.js)

- **Framework:** Vanilla JS (zero dependências, 100% offline)

- **Design:** Glassmorphism dark mode (inspirado DeiviTech)

- **Responsivo:** Desktop-first, mobile adaptado

-

  -

  -

  -

  -

  - Quick actions (botões ação rápida)

### Backend (dashboard.py - FastAPI)

-

  -

  -

  -

  -

  - Gerar resumo diário/semanal

### Automação (scripts/)

- **update-metrics.py:** Atualiza JSON com novas entradas

- **commit-auto.sh:** Git add + commit + push agendado

- **scrape-grok.js:** Captura nova conversa → transcrição MD

- **photo-timeline.py:** Organiza fotos progresso físico

---

## 📊 Widgets Dashboard (A Implementar)

### 1. Card Peso/Físico

```yaml
Título: "Progresso Físico 🏋️"
Dados:
  -

  -

  -

  -

  -

Ações:
  -

  -

  -

```text

### 2. Card Nutrição

```yaml
Título: "Nutrição Hoje 🍽️"
Dados:
  -

  -

  -

  -

Gráfico:
  -

Ações:
  -

  -

```text

### 3. Card Finanças

```yaml
Título: "Finanças 💰"
Dados:
  -

  -

  -

  -

  -

  -

Gráfico:
  -

Ações:
  -

  -

```text

### 4. Card Sono/Saúde Mental

```yaml
Título: "Sono & Humor 😴"
Dados:
  -

  -

  -

  -

Gráfico:
  -

Ações:
  -

  -

```text

### 5. Card Pendências

```yaml
Título: "Pendências ⚠️"
Lista:
  -

  -

  -

  -

  -

Ações:
  -

  -

```text

### 6. Card Git Activity

```yaml
Título: "Commits Semana 🚀"
Dados:
  -

  -

  -

  -

Gráfico:
  -

Ações:
  -

  -

```text

### 7. Timeline Fotos

```yaml
Título: "Evolução Física 📸"
Layout: Carrossel horizontal
Fotos:
  -

Metadata cada foto:
  -

  -

  -

Ações:
  -

  -

```text

---

## 🛠️ Stack Técnico

### Frontend

- **HTML5** + **CSS3** (Grid + Flexbox)

- **Vanilla JavaScript** (ES6+)

- **Chart.js** v4.4.0 (gráficos)

- **Font:** Inter (Google Fonts)

- **Ícones:** Emojis nativos (zero deps)

### Backend

- **Python 3.13.7** + **FastAPI** v0.115.0

- **Uvicorn** (ASGI server)

- **Pandas** (processar JSON → DataFrames)

- **Gitpython** (stats commits)

- **Playwright** (scrape Grok se precisar)

### Database

- **Vida-Deivison.json** (source of truth)

- **Dashboard/data/metrics.json** (cache métricas processadas)

- **Dashboard/data/timeline.json** (fotos progresso)

### Automação

- **Cron** (Linux) ou **Task Scheduler** (Windows)

- **Git hooks** (pre-commit validations)

---

## 📁 Estrutura Arquivos

```plaintext
Dashboard/
├─ README.md                  # Este arquivo

├─ index.html                 # [A CRIAR] Página principal

├─ style.css                  # [A CRIAR] Estilos glassmorphism

├─ app.js                     # [A CRIAR] Lógica frontend

├─ dashboard.py               # [A CRIAR] API Python

├─ requirements.txt           # [A CRIAR] Deps Python

│
├─ data/
│  ├─ metrics.json            # [AUTO-GERADO] Cache métricas

│  ├─ timeline.json           # [AUTO-GERADO] Fotos progresso

│  └─ commits-stats.json      # [AUTO-GERADO] Git activity

│
├─ scripts/
│  ├─ update-metrics.py       # [A CRIAR] Atualizar JSON

│  ├─ commit-auto.sh          # [A CRIAR] Git automation

│  ├─ scrape-grok.js          # [A CRIAR] Captura Grok

│  └─ photo-timeline.py       # [A CRIAR] Organiza fotos

│
└─ assets/
   ├─ logo-deivitech.svg      # [A ADICIONAR] Logo

   └─ photos/                 # [A CRIAR] Fotos progresso físico

      └─ .gitkeep

```text

---

## 🚀 Roadmap Implementação

### Fase 1: MVP Estático (Semana 1)

- [x] Criar estrutura pastas

- [x] README.md planejamento

- [ ] index.html skeleton

- [ ] style.css glassmorphism dark

- [ ] app.js dados mock (hardcoded)

- [ ] 3 cards: Peso, Finanças, Pendências

### Fase 2: Backend Python (Semana 2)

- [ ] dashboard.py FastAPI básico

- [ ] Endpoint `/metrics` (parse Vida-Deivison.json)

- [ ] Endpoint `/commits` (gitpython stats)

- [ ] Endpoint `/tasks` (parse Pendencias/)

- [ ] CORS configurado

- [ ] Frontend consome API

### Fase 3: Gráficos Dinâmicos (Semana 3)

- [ ] Integrar Chart.js

- [ ] Gráfico linha: peso última semana

- [ ] Gráfico barra: calorias/proteínas

- [ ] Gráfico pizza: finanças por categoria

- [ ] Heatmap commits (inspirado GitHub)

### Fase 4: Ações Rápidas (Semana 4)

- [ ] Form: adicionar peso

- [ ] Form: registrar humor

- [ ] Form: adicionar tarefa

- [ ] Botão: commit rápido (msg automática)

- [ ] Upload foto progresso

### Fase 5: Automação (Futuro)

- [ ] Cron diário: atualizar metrics.json

- [ ] Cron semanal: commit auto roadmap

- [ ] Scrape Grok automático (new conversas)

- [ ] Notificações: meta peso, foto quinzenal

---

## 💡 Features Avançadas (Brainstorm)

### IA Integrada

- **Gemini API:** Análise semanal texto ("Você comeu 105g proteína média, +5% da meta")

- **Qwen CLI:** Sugestões cardápio baseado em sobra orçamento

- **Grok:** Responder perguntas sobre transcrições ("Quando falei de camerologia?")

### Visualizações

- **Mapa calor:** Humor vs dia semana (segundas ruins?)

- **Comparação fotos:** Lado-a-lado progresso físico

- **Timeline interativa:** Eventos importantes (mudanças rotina, compras grandes)

### Gamificação

- **Badges:** "7 dias proteína 100g+", "30 commits mês", "10kg ganho"

- **Streaks:** Dias consecutivos tracking peso

- **Levels:** XP por tarefa completa (Pendências/)

---

## 🔒 Segurança & Privacidade

- ✅ **100% local:** Roda em `localhost:8000`, zero cloud

- ✅ **Dados privados:** Nunca sai do PC/celular

- ✅ **Git público:** Dashboard/ pode ser .gitignore (se quiser)

- ✅ **API autenticada:** JWT tokens (futuro se expor web)

---

## 📖 Como Usar (Quando Pronto)

### Iniciar Dashboard

```bash

# Backend

cd Dashboard/
python dashboard.py  # Roda em localhost:8000

# Frontend

# Abrir index.html no navegador

# OU usar Live Server (VS Code extension)

```text

### Atualizar Métricas Manual

```bash
python scripts/update-metrics.py --peso 61.5 --humor 4

```text

### Commit Automático

```bash
bash scripts/commit-auto.sh "update: métricas 16/11/2025"

```text

---

## 🎨 Design Inspiração

**Referências:**

- **Glassmorphism:** backdrop-filter blur + transparência

- **Dark Mode:** #1a1a1a bg, #00ff88 accent (verde DeiviTech)

- **Cards:** border-radius 16px, box-shadow sutil

- **Fonts:** Inter 400/600, monospace para números

**Paleta Cores:**

```css
--bg-dark: #0d0d0d;
--card-bg: rgba(30, 30, 30, 0.7);
--accent: #00ff88;
--text: #e0e0e0;
--text-dim: #888888;

```text

---

## ⚡ Tecnologias Escolhidas (Justificativa)

### Por que Vanilla JS?

- ✅ Zero build step (abrir HTML = funciona)

- ✅ Mais rápido que React (sem virtual DOM)

- ✅ Aprende fundamentos (não abstração framework)

- ✅ 100% offline (sem CDN)

### Por que FastAPI?

- ✅ Async nativo (não bloqueia scraping)

- ✅ Auto-docs (Swagger UI `/docs`)

- ✅ Type hints Python 3.13

- ✅ Mais rápido que Flask (Starlette base)

### Por que Chart.js?

- ✅ Biblioteca madura (10+ anos)

- ✅ Responsivo out-of-the-box

- ✅ 8 tipos gráficos (linha, barra, pizza, etc)

- ✅ Customizável (cores, labels, tooltips)

### Por que JSON como DB?

- ✅ Humano-legível (Git diff funciona)

- ✅ Versionável (histórico mudanças)

- ✅ Sem servidor (SQLite seria overkill)

- ✅ Pandas lê fácil (df = pd.read_json())

---

## 🚧 Status Atual

**Criado:** 16/11/2025  
**Progresso:** 10% (estrutura pastas + planejamento)

**Próximos Passos:**

1. Criar `index.html` skeleton (cards mockados)

2. Estilizar `style.css` glassmorphism dark

3. `app.js` dados hardcoded (testar layout)

4. `dashboard.py` endpoint `/metrics` básico

**Meta:** MVP funcional até 23/11/2025 (7 dias)

---

*Dashboard orquestrado por DevSan | Auto-aprovado | Em construção ativa* 🚀
