# 🎤 Sistema de Aliases Modo Voz

> **Objetivo:**

> **Criado:**

> **Última Atualização:**

> **Integra com:** PROMPT-MODO-VOZ.md, todos os repositórios

---

## 🎯 Conceito

**Problema:** Modo voz é lento para comandos repetitivos  
**Solução:** Atalhos verbais que agente reconhece e expande

**Exemplo:**

```text
❌ Lento: "Abra o repositório FinanDEV, ative o modo de refatoração, e capture a conversa atual"
✅ Rápido: "repo-finandev, modo-refator, captura-agora"

```text

---

## 📋 Aliases de Repositório

### Repos Principais

| Alias | Ação | Descrição |
|-------|------|-----------|
| `repo-finandev` | `cd ~/Projetos/FinanDEV && code .` | Abre FinanDEV no VS Code |
| `repo-transcricoes` | Acessa Temp-Transcrições | Repo universal de backups |
| `repo-amigos` | Acessa Grupo-Amigos-Bot | Sistema social WhatsApp |
| `repo-ateus` | Acessa Ateus-Debates | Debates lógicos |
| `repo-cetens` | Acessa Orquestracao-Settings | Mini-tarefas diárias CETENS |

### Atalhos Genéricos

- `repo-X` → Onde X é o nome de qualquer repositório

- `lista-repos` → Mostra todos os repos disponíveis

- `ultimo-repo` → Retorna ao último repo aberto

---

## 🔄 Aliases de Modo de Trabalho

### Modos Principais

| Alias | Modo | Ação |
|-------|------|------|
| `modo-refator` | Refatoração | Analisa estrutura, sugere melhorias |
| `modo-debug` | Debug | Foca em bugs, erros, inconsistências |
| `modo-doc` | Documentação | Cria/atualiza MDs, README, specs |
| `modo-cria` | Criação | Gera novos arquivos, mini-sistemas |
| `modo-aprende` | Aprendizado | Extrai insights, padrões, learnings |

### Combinações

```text
"repo-finandev, modo-refator"
→ Abre FinanDEV + ativa análise de estrutura

"repo-transcricoes, modo-aprende"
→ Acessa transcrições +

```text

---

## 🕹️ Aliases de Contexto

### Ambientes

| Alias | Contexto | Foco |
|-------|----------|------|
| `ctx-trabalho` | CETENS | Chamados, upgrades, mini-tarefas |
| `ctx-casa` | Projetos pessoais | FinanDEV, scripts, grupos |
| `ctx-madrugada` | Coding noturno | Projetos disruptivos, experimentais |
| `ctx-vida` | Rotinas diárias | Alimentação, saúde mental, física |

### Uso

```text
"ctx-trabalho, lista-pendentes"
→ Mostra chamados/tarefas CETENS pendentes

"ctx-madrugada, repo-finandev, modo-cria"
→ Ambiente criativo noturno +

```text

---

## ⚡ Aliases de Ação Rápida

### Capturas e Salvamentos

| Alias | Ação | Descrição |
|-------|------|-----------|
| `captura-agora` | Inicia gravação voz | Playwright scrape atual conversa |
| `salva-transcricao` | Salva no Temp-Transcrições | MD estruturado com emojis |
| `dump-contexto` | Exporta contexto atual | Quando buffer >60% cheio |

### Resumos

| Alias | Ação | Descrição |
|-------|------|-----------|
| `resume-hoje` | Resumo do dia | Commits +

| `resume-semana` | Resumo semanal | Learnings +

| `resume-mes` | Resumo mensal | Metas atingidas vs. planejadas |

### Git e Commits

| Alias | Ação | Descrição |
|-------|------|-----------|
| `commit-urgente` | Git add +

| `commit-descritivo` | Commit detalhado | Agente escreve mensagem longa |
| `desfaz-ultimo` | Git reset HEAD~1 | Desfaz último commit (soft) |

### Análises

| Alias | Ação | Descrição |
|-------|------|-----------|
| `analisa-repo` | Estrutura completa | Arquivos, dependências, TODOs |
| `busca-bugs` | Grep por bugs/FIXMEs | Lista todos os bugs pendentes |
| `lista-pendentes` | TODOs não resolvidos | Todos os [ ] nos MDs |

---

## 🔗 Aliases de Integração

### Mini-Sistemas

| Alias | Mini-Sistema | Ação |
|-------|--------------|------|
| `atualiza-peso` | ROTINA-FISICA | Registra peso do dia |
| `captura-outfit` | ROTINA-FISICA | Descreve roupa de hoje |
| `registra-sono` | SAUDE-MENTAL | Horas +

| `humor-hoje` | SAUDE-MENTAL | Neutro/Positivo/Negativo +

| `learnings-semana` | LEARNINGS | Extrai insights da semana |

### Vida-Deivison.json

| Alias | Campo JSON | Ação |
|-------|------------|------|
| `meta-peso` | meta_peso_6meses | Atualiza meta 60→70kg |
| `salario-atual` | salario_liquido | "Ver último holerite" |
| `sobra-mes` | sobra_mensal | Calcula sobra após despesas |

### Grupos Sociais

| Alias | Sistema | Ação |
|-------|---------|------|
| `rifa-amigos` | Grupo-Amigos-Bot | Inicia nova rifa coletiva |
| `debate-ateus` | Ateus-Debates | Gera argumento lógico |

---

## 🧠 Aliases de Raciocínio

### Planejamento

| Alias | Ação | Descrição |
|-------|------|-----------|
| `planeja-dia` | Plano diário | Baseado em contexto e metas |
| `planeja-semana` | Plano semanal | Prioriza tarefas ALTA/MÉDIA/BAIXA |
| `roadmap-mes` | Roadmap mensal | Como roadmap-mudancas-novembro |

### Decisões

| Alias | Ação | Descrição |
|-------|------|-----------|
| `decide-por-mim` | Decisão baseada em contexto | Quando indeciso entre opções |
| `pros-contras` | Lista prós/contras | Análise de decisão complexa |
| `prioriza` | Ordena tarefas | Por urgência + impacto |

---

## 📝 Sintaxe de Combinação

### Encadeamento (`,`)

```text
"repo-finandev, modo-refator, analisa-repo"
→ Abre FinanDEV +

```text

### Sequência (`então`)

```text
"captura-agora, então salva-transcricao, então learnings-semana"
→ Captura conversa → salva MD → extrai insights

```text

### Condicional (`se`)

```text
"se energia < 5/10, então sugere-break"
→ Verifica energia (SAUDE-MENTAL.md), sugere descanso se baixa

```text

---

## 🤖 Implementação Técnica

### PROMPT-MODO-VOZ.md (Expansão)

Adicionar seção no prompt principal:

```markdown

## Aliases Modo Voz

Você reconhece os seguintes atalhos verbais:

### Repositórios

- repo-finandev → cd ~/Projetos/FinanDEV && code .

- repo-X → Onde X é qualquer repositório

- lista-repos → Mostra todos disponíveis

### Modos

- modo-refator → Analisa estrutura, sugere melhorias

- modo-debug → Foca em bugs e erros

-

...

[Lista completa de aliases]

```text

### Detecção Automática

- **Padrão regex:** `^(repo|modo|ctx|alias)-[a-z-]+$`

- **Parser:** Converte alias em comando completo

- **Feedback:** Confirma ação antes de executar

---

## 📊 Métricas de Uso (Futuro)

**Rastrear:**

- Aliases mais usados (top 10)

- Combinações frequentes (ex: `repo-finandev, modo-refator`)

- Tempo economizado (estimativa)

**Output semanal:**

```markdown

## Semana 16-22/11/2025

**Aliases usados:** 47
**Top 3:** captura-agora (12x), repo-finandev (8x), resume-hoje (6x)
**Tempo economizado:**

```text

---

## 🎯 Aliases Customizáveis

### Usuário Pode Criar

```text
"cria-alias: projeto-urgente = repo-finandev, modo-refator, commit-urgente"
→ Agente salva novo alias no sistema

```text

### Aliases Temporários (Sessão)

```text
"alias-temp: foco-cetens = ctx-trabalho, lista-pendentes"
→ Válido apenas nesta conversa

```text

---

## 🔒 Segurança

### Aliases NÃO Permitidos

- `rm -rf` ou similares destrutivos

- Comandos sudo/root sem confirmação

- Alterações em `/etc/` diretas

### Aliases Confirmação Obrigatória

- `formata-disco`

- `deleta-repo`

- `reboot-sistema`

---

## 📚 Documentação Completa

**Ver:** PROMPT-MODO-VOZ.md (seção Aliases completa)  
**Lista viva:** Atualizada conforme novos aliases criados

---

*Sistema em desenvolvimento | Expansível pelo usuário | Auto-documentado* 🎤
