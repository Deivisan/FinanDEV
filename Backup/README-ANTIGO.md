# 🧬 ROTINA DE VIDA - Deivison Santana

> **Projeto:** Mapeamento completo rotina alimentação, saúde física/mental, finanças  
> **Owner:** Deivison Santana (25 anos, Técnico TI, UFRB CETENS)  
> **Local:** Feira de Santana/BA  
> **Iniciado:** 02 Novembro 2025  
> **Status:** 🟢 Ativo - Fase 1 (Captação Dados)

---

## 🎯 OBJETIVO

Estruturar rotina de vida completa baseada em:

1. **Alimentação** - Ganhar 10kg (60→70kg), orçamento R$ 200-250 quinzenal
2. **Saúde Física** - Massa muscular, energia, disposição
3. **Saúde Mental** - Reduzir ansiedade oral, impulsos, sono qualidade
4. **Finanças** - Mapeamento renda/despesas, liberdade financeira
5. **Produtividade** - Rotina trabalho UFRB CETENS + side hustles

---

## 📁 ESTRUTURA REPOSITÓRIO

```
FinanDEV/
├── README.md                          # Este arquivo
├── Rotinas/
│   ├── rotina.ipynb                   # Notebook Jupyter principal
│   ├── LISTA-COMPRAS-03NOV-QUINZENAL.md
│   └── [rotinas-dia-semana]/          # Futuro: seg, ter, qua...
├── Transcricoes/
│   ├── conversa-alimentacao-raw.txt   # Conversa original Grok
│   └── conversa-atualizacao-refatoracao.txt
├── Docs/
│   ├── Metodologia-Scrape.md          # Como captar conversas
│   ├── scrape.js                      # Script extração
│   ├── CONTEXTO-TRABALHO-CETENS.md
│   └── QUESTIONARIO-LACUNAS.md
└── Scrape/                            # Ferramentas captação
```

---

## 🚀 QUICK START

### 1. Ler Contexto Completo

```bash
# Leia as transcrições primeiro
cat Transcricoes/conversa-alimentacao-raw.txt
cat Transcricoes/conversa-atualizacao-refatoracao.txt
```

### 2. Abrir Rotina Principal

```bash
# Jupyter Notebook
jupyter notebook Rotinas/rotina.ipynb

# OU VSCode
code Rotinas/rotina.ipynb
```

### 3. Lista Compras Atual

```bash
# Ver lista quinzenal 03/NOV
cat Rotinas/LISTA-COMPRAS-03NOV-QUINZENAL.md
```

---

## 📊 DADOS CONTEXTUAIS

### 👤 PERFIL DEIVISON

- **Idade:** 25 anos
- **Peso atual:** 60kg → Meta 70kg (ganhar 10kg massa)
- **Altura:** ~1,75m (estimado)
- **Trabalho:** Técnico TI UFRB CETENS (Seg-Sex 8h-18h)
- **Renda líquida:** R$ 1.866,53/mês
- **Vale alimentação:** R$ 420 (Pluxee/Sodexo)
- **Vale transporte:** R$ 320

### 🏠 CONTEXTO VIDA

- Mora sozinho (apartamento próprio)
- Sem despesas aluguel
- Gastos fixos: R$ 380 (água R$ 150 + luz R$ 150 + internet R$ 80)
- Orçamento alimentação quinzenal: R$ 200-250
- A pé mercados (limita volume compras)

### 🎯 METAS ATUAIS

1. ✅ Lista compras quinzenal estruturada (03/NOV → 09/NOV)
2. ⏳ Criar rotina dia-a-dia (seg-dom)
3. ⏳ Batch cooking domingos (frango, ovos, porções freezer)
4. ⏳ Reduzir ansiedade oral (goma, frutas, limão)
5. ⏳ Mapear finanças completas (FGTS, patrimônio)

---

## 🛠️ FERRAMENTAS & METODOLOGIA

### Captação Conversas

- **Metodologia:** Ver `Docs/Metodologia-Scrape.md`
- **Script:** `Docs/scrape.js` (extrair conversas Grok/ChatGPT)
- **Formato:** TXT com metadados cabeçalho (melhor que JSON pra AI!)

### Análise & Estruturação

- **LLMs usados:** Grok (Doctor Mode), Claude Sonnet 4.5 (DevSan)
- **Formato saída:** Markdown + Jupyter Notebook
- **Versionamento:** Git (este repo)

### AI Training Data

**Por que Markdown?**
- 40-60% melhor compreensão AI vs TXT puro
- Preserva hierarquia/estrutura
- Fácil ler humano + máquina
- Conversível JSON quando necessário

**TXT com metadados:**
```
===
DATA CAPTAÇÃO: 02/11/2025 15:30
DATA CRIAÇÃO: 02/11/2025 16:45
FONTE: Grok Doctor Mode
TÓPICO: Alimentação rotina trabalho
PALAVRAS-CHAVE: hambúrguer, café, limão, ansiedade
===

[conteúdo conversa...]
```

---

## 📝 DESCOBERTAS CHAVE (CONVERSAS)

### 🍔 Alimentação Trabalho

**Linha 456 conversa-alimentacao-raw.txt:**
> "Três hambúrgueres por dia. Dois pela manhã e um hambúrguer pela tarde"

- Segunda a sexta: 3 hambúrgueres/dia (2 café + 1 lanche)
- Sábado/domingo: 2 hambúrgueres/dia (café)
- **TOTAL semanal:** 19 hambúrgueres

### ☕ Café Grátis Trabalho

**Linha 476:**
> "Café é grátis lá. Você leva um grande copo da casa, enche de café"

- Copa trabalho tem café grátis
- Substituir Tang (açúcar) por café + limão

### 🍋 Limão vs Suco Pó

**Linha 476:**
> "Se quiser sabor, compra um limão, espreme no copo, leva. Custa um real, dura uma semana"

- Limão tahiti: R$ 1-2/kg
- 1 limão = 300ml limonada
- Mais saudável que Tang (sem açúcar)

### 🍌 Banana: Come 2, Não 1!

**Linha 544:**
> "Geralmente eu não como uma só, eu como duas às vezes"

- Comprar banana 3kg (não 2kg!)
- 2 bananas/dia x 10 dias = 3kg quinzenal

### 🥕 Batata Doce + Banana Terra

**Você mencionou:** "Gosto também de batata-doce, banana da Terra"

- Pode levar frango + batata doce/banana terra trabalho
- Substitui almoço vale/janta
- Carboidrato lento, nutritivo

---

## 🔄 PRÓXIMOS PASSOS

### Fase 1: Captação Dados ✅ (Concluída)

- [x] Transcrever conversas Grok/Claude
- [x] Estruturar lista compras quinzenal
- [x] Criar repositório GitHub
- [x] Documentar metodologia

### Fase 2: Rotina Dia-a-Dia ⏳ (Em andamento)

- [ ] Criar `rotina.ipynb` principal
- [ ] Criar rotinas específicas seg-dom
- [ ] Mapear horários exatos (acordar, trabalho, batch cooking)
- [ ] Adicionar opções modulares (frango vs batata doce, etc)

### Fase 3: Produtos Limpeza ⏳

- [ ] Conversa Grok sobre limpeza
- [ ] Adicionar seção limpeza lista compras
- [ ] Orçamento R$ 47-84 disponível

### Fase 4: Finanças ⏳

- [ ] Mapear FGTS acumulado
- [ ] Patrimônio líquido completo
- [ ] Projeção liberdade financeira

---

## 📚 REFERÊNCIAS

- [Markdown para AI Training (2025)](https://www.docs-to-md.com/blog/markdown-gold-standard-ai-training)
- [TXT vs Markdown AI](https://webcrawlerapi.com/blog/cleaned-text-vs-markdown-choosing-the-right-output-format)
- Conversas originais: `Transcricoes/`

---

## 🤝 CONTRIBUINDO

Este é repositório pessoal Deivison, mas:

1. **IAs podem contribuir:** Ler transcrições, sugerir melhorias rotina
2. **Formato:** Markdown, Jupyter Notebook
3. **Commits:** Sempre adicionar contexto (data captação, data criação)

---

## 📅 CHANGELOG

### 2025-11-02

- ✅ Estrutura repositório criada
- ✅ README.md completo
- ✅ Lista compras quinzenal 03/NOV
- ✅ Transcrições movidas `Transcricoes/`
- ✅ Metodologia movida `Docs/`

### Próximo Update: 2025-11-03

- [ ] Rotina Jupyter Notebook criada
- [ ] Compras domingo realizadas
- [ ] Batch cooking executado

---

**🔥 LEMBRETE:** Este projeto evolui diariamente. Sempre ler transcrições atualizadas antes de fazer sugestões!

---

**Feito com 💪 por Deivison + DevSan (Claude) + Grok Doctor Mode**
