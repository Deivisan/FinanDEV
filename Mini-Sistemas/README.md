# 🛠️ Mini-Sistemas FinanDEV - Ideias & Implementações

> **Propósito:** Módulos autônomos que automatizam aspectos específicos do backup mental  
> **Status:** 2 ATIVOS + 9 planejados  
> **Fonte:** Conversas transcritas 16/11/2025 + 02/12/2025 + 08/12/2025 (Grok)
> **Última atualização:** 09/DEZ/2025

---

## 📂 ESTRUTURA REORGANIZADA (09/DEZ/2025)

```
Mini-Sistemas/
├── Ativos/                    # ✅ Sistemas em uso ativo
│   ├── README.md
│   ├── SAUDE-MENTAL-ATIVO.md  # Desde 08/12
│   └── SLEEP-TRACKING-ATIVO.md # Desde 08/12
├── Inativos/                  # 🔴 Templates não ativos
│   └── README.md
└── [arquivos legado]          # Templates originais
```

## 🟢 SISTEMAS ATIVOS (2)

| Sistema | Desde | Check-in | Arquivo |
|---------|-------|----------|---------|
| **Saúde Mental** | 08/12/2025 | Domingo 20h | [Ativos/SAUDE-MENTAL-ATIVO.md](Ativos/SAUDE-MENTAL-ATIVO.md) |
| **Sleep Tracking** | 08/12/2025 | Diário manhã | [Ativos/SLEEP-TRACKING-ATIVO.md](Ativos/SLEEP-TRACKING-ATIVO.md) |

### Metas Ativas
- **Saúde Mental:** Marcar terapia SUS até 20/12, anotar 3 irritações/dia
- **Sleep Tracking:** Dormir 23h, acordar 05h, anotar sono diário

---

## 🔥 ATUALIZAÇÃO 08/DEZ/2025

### Sistemas Ativados
1. ✅ **Saúde Mental** → Check-in domingo 20h, terapia SUS até 20/12
2. ✅ **Sleep Tracking** → Papel cabeceira, meta 23h-05h

### Status Atual
- **Ansiedade:** 9/10
- **Sono:** Completamente desregulado (meta: regularizar)
- **Daniel:** Morando junto desde 24/11
- **CETENS:** Saída planejada março/2026

---

## ✅ Implementados (Funcionais)

### 1. 🎭 Scrape v3.0 - Captura Conversas Grok
**Localização:** `Docs/Metodologia-Scrape.md` + `Scrape/scrape-v3.js`

**O que faz:**
- Captura conversas Grok Share via Playwright
- Auto-scroll até 50 scrolls (2s delay)
- Diferencia speakers (👤 Deivison vs 🤖 Grok)
- Output: JSON + Markdown estruturado
- Análise contextual: confirmações, correções, sentimentos

**Como usar:**
```bash
node Scrape/scrape-v3.js "https://grok.com/share/c2hhcmQtMg_UUID"
```

**Expansão futura:**
- Suporte múltiplas plataformas (ChatGPT, Claude, Gemini)
- Detecção automática idioma
- Tradução inline PT/ES/EN

---

### 2. 💾 Backup Mental - Sistema Core
**Localização:** Repo completo (raiz)

**Componentes:**
- `Vida-Deivison.json`: Dados vetoriais densos
- `Rotinas/Diarias/*.md`: Segunda-Domingo
- `Transcricoes/*.md`: Conversas capturadas
- `Deivison.md`: Perfil psicológico (1295 linhas)
- `DeiviTech.md`: Contexto profissional (2258 linhas)

**Filosofia:** "Se não tá escrito, esqueço" → Markdown como hack da vida

---

### 3. 📚 Metodologia Captura
**Localização:** `Docs/Metodologia-Scrape.md`

**Documenta:**
- Pipeline Playwright completo
- Seletores com fallback
- Speaker detection (conversacional analysis)
- Performance: 2.3s para 460 mensagens

---

## ⚠️ Planejados (Aguardando Implementação)

### 4. 📅 Aprendizados Semanais
**Origem:** Conversa linha 596-602 (finandev-backup-mental)

**Conceito:**
- Extrai insights de 5-7 transcrições semanais
- Agrupa por data automaticamente
- Atualiza `APRENDIZADOS-SEMANAIS.md`
- Detecta padrões: decisões técnicas, mudanças rotina, descobertas

**Implementação proposta (baseada em PKM 2025):**
```python
# Mini-Sistema: weekly_learnings.py
import json
from datetime import datetime, timedelta

def extract_insights(transcriptions_folder):
    """
    Lê últimas 7 transcrições, extrai:
    - Decisões técnicas (palavras-chave: "decidi", "vou usar")
    - Mudanças rotina (referências a horários, alimentação)
    - Descobertas ("descobri", "aprendi", "percebi")
    """
    # Usa NLP básico (NLTK ou spaCy)
    # Agrupa por semana ISO (datetime.isocalendar())
    # Salva em APRENDIZADOS-SEMANAIS.md com template:
    ## Semana 46/2025 (13-19 Nov)
    ### Decisões Técnicas
    - Migrei de B550 → B450M (conversa 16/11)
    ### Mudanças Rotina
    - Adicionei 2 bananas/dia (conversa alimentação)
```

**Referências Web:**
- Obsidian Auto Note Mover (tags → pastas automático)
- Logseq weekly templates
- PKM frameworks com 8000+ notas analisadas

---

### 5. 🎤 Sistema Aliases - Atalhos Contextuais
**Origem:** Conversa linha 664-722 (finandev-backup-mental)

**Conceito:**
- Palavras-chave ativam contextos completos
- Similar aliases Linux (`gs` = `git status`)
- Agente IA detecta e carrega contexto específico

**Exemplos propostos:**

```yaml
aliases:
  modo-refator:
    trigger: "modo-refator"
    ação: |
      - Carrega padrões clean code
      - Foca em otimização sem explicações
      - Saída: sugestões diretas
  
  repo-X:
    trigger: "repo-finandev"
    ação: |
      - Lê README.md + último commit
      - Carrega estrutura completa
      - Pronto para edições
  
  captura-completa:
    trigger: "captura-completa [URL]"
    ação: |
      - Executa Scrape/scrape-v3.js
      - Análise automática speakers
      - Commit em Transcricoes/
  
  backup-semanal:
    trigger: "backup-semanal"
    ação: |
      - Extrai insights últimas 7 transcrições
      - Atualiza APRENDIZADOS-SEMANAIS.md
      - Git commit com resumo
```

**Implementação (baseada em Voice AI 2025):**
- NLP intent detection (similaridade semântica)
- Context injection em prompt IA
- Trigger automático via wake words
- Integração Termux + Tasker (mobile)

**Referências Web:**
- Custom voice models & wake words (Trengo 2025)
- Speech-to-meaning architecture
- Multi-domain understanding

---

### 6. 🌙 BackBrowser - Check-up Fim Conversa
**Origem:** Conversa linha 766-784 (finandev-backup-mental)

**Conceito:**
- Agente detecta fim de conversa ("vou encerrar")
- Faz perguntas curtas pré-definidas
- Atualiza MDs específicos automaticamente

**Perguntas propostas:**

**Fim conversa:**
```
- "Dormiu quantas horas ontem?"
- "Nível de energia hoje (1-5)?"
- "Qual foi o maior ganho dessa semana?"
- "Algo que te travou que a gente pode desarmar?"
```

**Início conversa:**
```
- "O que rolou de novo na sua cabeça hoje?"
- "Tem algum insight do dia que quer fixar?"
```

**Atualiza:**
- `Rotinas/Sono.md`: Horas dormidas + qualidade
- `Vida-Deivison.json`: Energia diária (array)
- `APRENDIZADOS-SEMANAIS.md`: Insights + travas

**Implementação:**
- Regex detecta frases encerramento
- Webhook dispara perguntas
- Respostas parseadas → JSON vetorial

---

### 7. ⏰ Detecção Horário/Contexto
**Origem:** Conversa linha 790 (finandev-backup-mental)

**Conceito:**
- Agente sabe horário + dia atual
- Cruza com `Rotinas/Diarias/*.md`
- Ajusta comportamento: "Você deveria estar no trabalho agora?"

**Exemplo:**
```
Hora: 14h terça-feira
Rotina terça-sexta.md: "14-17h: Trabalho CETENS"
→ Agente: "Tá no trampo? Quer pausar notificações?"

Hora: 19h domingo
Rotina domingo.md: "19-21h: Batch cooking"
→ Agente: "Hora do batch cooking! Lista compras pronta?"
```

**Implementação:**
```python
# detect_context.py
from datetime import datetime
import json

def get_current_context():
    now = datetime.now()
    dia_semana = now.strftime("%A").lower() # segunda, terça...
    hora = now.hour
    
    rotina = load_markdown(f"Rotinas/Diarias/{dia_semana}.md")
    bloco = parse_time_block(rotina, hora)
    
    return {
        "momento": bloco["atividade"], # "Trabalho CETENS"
        "local": bloco["local"], # "Escritório UFRB"
        "sugestao": bloco["dica"] # "Foco deep work"
    }
```

---

### 8. 📸 Tracking Visual Moda/Corpo
**Origem:** Conversa linha 1258-1264 (finandev-backup-mental), linha 695-731 (prompt-voz)

**Conceito:**
- Fotos periódicas corpo (peso, massa muscular)
- Fotos outfit diário (evolução moda)
- MD com análise temporal

**Estrutura proposta:**
```
Rotinas/
  Tracking-Visual/
    README.md (metodologia)
    2025-11/
      16-corpo-60kg.jpg
      16-outfit-camisa-preta.jpg
      23-corpo-61kg.jpg
    ANALISE-VISUAL.md
```

**ANALISE-VISUAL.md template:**
```markdown
## Novembro 2025

| Data | Peso | Circunf. Braço | Outfit | Observações |
|------|------|----------------|--------|-------------|
| 16/11 | 60kg | 28cm | Camisa preta oversized | Início tracking |
| 23/11 | 61kg | 29cm | Moletom cinza | +1kg massa |

### Meta Maio/2026: 70kg
- Progresso: 1kg/6 meses = 16% meta
- Ritmo necessário: +1.5kg/mês
```

**Implementação (baseada em fitness apps 2025):**
- **Metamorph app** (líder 2025): Template fotos consistentes
- **Gym Body Tracker**: 9 pontos circunferência
- **Me 360**: Scan 3D corpo via câmera phone
- Script Python: OCR extrai peso de fotos balança

**GCam configs (Poco X5):**
- **MGC 9.4 BSG**: Modo Panorama 360° (setup completo)
- **LMC 8.4 R18 Hasli**: HDR+ alta res (detalhes corpo)

---

### 9. 💰 Mini-Sistema Finanças API
**Origem:** Conversa linha 946 (finandev-backup-mental)

**Conceito:**
- Busca preços Shopee + Mercado Livre
- Compara + retorna menor preço com frete
- Salva histórico `Financas/Compras-Otimizadas.json`

**Caso de uso:**
```
Você: "Preciso adaptador DisplayPort → VGA"
Sistema:
1. Scrape Shopee API: R$ 25,90 + frete R$ 12
2. Scrape ML API: R$ 29,90 frete grátis
→ Recomenda: Mercado Livre R$ 29,90 (entrega 3 dias)
```

**Implementação (baseada em ecommerce Brasil 2025):**

```javascript
// price_compare.js
const axios = require('axios');

async function comparePrice(produto) {
  // Shopee API (scraping autorizado termos uso)
  const shopee = await axios.get(`https://shopee.com.br/api/search?keyword=${produto}`);
  const shopeePreco = shopee.data.items[0].price / 100000; // centavos → reais
  
  // Mercado Livre API oficial
  const ml = await axios.get(`https://api.mercadolibre.com/sites/MLB/search?q=${produto}`);
  const mlPreco = ml.data.results[0].price;
  
  return {
    shopee: { preco: shopeePreco, link: shopee.data.items[0].itemid },
    ml: { preco: mlPreco, link: ml.data.results[0].permalink },
    melhor: shopeePreco < mlPreco ? 'shopee' : 'ml'
  };
}
```

**Dados web:**
- Shopee Brasil: 8% mercado, crescendo 25%/ano
- ML: 13% mercado, API oficial disponível
- Web scraping legal para preços públicos

---

### 10. 📱 Sensor-Rotina - Automação Física
**Origem:** Conversa linha 1037-1087 (prompt-modo-voz)

**Conceito:**
- Termux Python lê sensores Poco X5
- Dispara ações baseado em movimento/ambiente
- Logs salvos `Ambiente-Dev/Sensores/`

**Sensores Poco X5:**
- Acelerômetro: Detecta movimento/parado
- Giroscópio: Rotação (exercícios)
- Magnetômetro: Direção (bússola)
- Luz ambiente: Qualidade ambiente
- Proximidade: Auto-pause logs

**Casos de uso:**

```python
# sensor_routine.py (Termux)
import json
from termux import sensor

def check_sedentarism():
    accel = sensor.accelerometer()
    if accel['movement'] < 0.1: # Parado >30min
        notify("Levanta! Caminha 5min")
        log_to_json("sedentarismo_detectado")

def optimize_batch_cooking():
    luz = sensor.light()
    if luz < 100: # Escurecendo
        notify("Dia escurecendo, hora batch cooking!")
```

**Implementação (baseada em Android sensors 2025):**
- **termux-sensor**: JSON output nativo
- **termux-api**: Notificações + automação
- Sleep as Android: Acelerômetro noturno (toss/turns)

**Referências:**
- Mining smartphone sensor data with Python (YouTube)
- Termux-sensor wiki oficial
- Stack Overflow: Gyro para sleep study

---

### 11. 😴 Mini-Sistema Sono
**Origem:** Conversa linha 1087-1149 (prompt-modo-voz)

**Conceito:**
- Acelerômetro detecta movimentos noturnos
- Cruza com humor `Vida-Deivison.json`
- Identifica padrões: sono ruim → energia baixa

**Integração apps existentes:**
- **Sleep as Android**: Export JSON logs
- **Sleep Cycle**: API disponível
- Script Python importa → `Rotinas/Sono.md`

**Análise proposta:**
```python
# sleep_analysis.py
import pandas as pd

sono = pd.read_json("sleep_android_export.json")
humor = pd.read_json("Vida-Deivison.json")["humor_diario"]

# Correlação Pearson
correlacao = sono['qualidade'].corr(humor['energia'])
# Output: -0.78 (sono ruim → energia baixa 78% casos)

insight = f"Dormir <6h reduz energia em {correlacao*100}%"
append_to_md("APRENDIZADOS-SEMANAIS.md", insight)
```

**Implementação:**
- Deixar celular no colchão (acelerômetro)
- Export semanal → Backup Mental
- Dashboard visual (matplotlib)

---

## 🎯 Priorização Implementação (Sugestão)

**Alta prioridade (Quick Wins):**
1. ✅ Aprendizados Semanais (Python script simples)
2. ✅ Sistema Aliases (YAML + NLP básico)
3. ✅ BackBrowser (regex + webhook)

**Média prioridade:**
4. ⚠️ Tracking Visual (requer disciplina foto periódica)
5. ⚠️ Detecção Horário (integração Rotinas/)

**Baixa prioridade (Complexidade técnica):**
6. 🔧 Finanças API (scraping legalidade)
7. 🔧 Sensor-Rotina (requer Termux setup)
8. 🔧 Mini-Sistema Sono (depende apps externos)

---

## 📚 Referências Web Utilizadas

**PKM Automation:**
- Personal Knowledge Management at Scale (8000 notas, dsebastien.net)
- Obsidian Auto Note Mover plugin
- Logseq mobile transcription

**Voice AI:**
- AI Voice Assistants 2025 (Pageon.ai)
- Custom wake words & context injection (Trengo)
- Speech-to-meaning architecture

**Android Sensors:**
- Mining smartphone sensor data (YouTube)
- Termux-sensor official wiki
- Sleep tracking with accelerometer (Medium)

**E-commerce Brasil:**
- Shopee vs Mercado Libre comparison 2025
- SKU volume analysis web scraping
- API integration best practices

**Fitness Tracking:**
- Metamorph (leading progress app 2025)
- Gym Body Tracker (9-point measurements)
- Me 360 (3D body scanning)

---

## 🚀 Próximos Passos

1. **DIA 5 (sexta):** Abrir Mini-Sistema Final-Dezembro (salário → contas → sobra)
2. **DIA 6 (sábado):** storage_state.json no Indeed ou GeekHunter
3. Ativar Sleep as Android compartilhamento dados
4. Primeira foto tracking visual
5. Testar sistema aliases (3 exemplos)

**Última atualização:** 02/DEZ/2025  
**Fonte:** Análise conversas + pesquisa web 2025 + Conversa Grok 02/12 (2h+)
