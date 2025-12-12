📦 Arquivo movido para `Ideias/IDEIAS-FUTURAS.md` para manter raiz mais limpa. Para editar, abra e altere a cópia em `Ideias/`.

---

**Nota:** Conteúdo original arquivado em `Ideias/IDEIAS-FUTURAS.md`.
---

## 🎯 Mini-Sistemas Propostos (Não Implementados)

### 1. 🤖 Sistema Aliases - Atalhos Contextuais IA
**Origem:** Linha 664-722 (finandev-backup-mental)

**O que é:** Palavras-chave que ativam contextos completos instantaneamente

**Exemplos concretos você mencionou:**
```
"modo-refator" → Carrega padrões clean code, foco otimização
"repo-finandev" → Lê README + último commit, pronto editar
"captura-completa [URL]" → Executa scrape-v3.js + commit
"backup-semanal" → Extrai insights 7 últimas transcrições
```

**Como implementar (2025):**
- NLP intent detection (similaridade semântica 85%+)
- YAML config aliases customizáveis
- Integração Grok/Gemini via custom instructions
- Termux + Tasker: wake words mobile

**Referências web:**
- Voice AI custom wake words (Trengo)
- Speech-to-meaning architecture
- Multi-domain understanding contexts

**Prioridade:** 🔥 ALTA (Quick Win - YAML + regex básico)

---

### 2. 📅 Aprendizados Semanais - Extração Automática
**Origem:** Linha 596-602 (finandev-backup-mental)

**O que é:** Script Python analisa 5-7 transcrições últimas, extrai insights

**Você quer capturar:**
- Decisões técnicas ("decidi usar X", "migrei pra Y")
- Mudanças rotina ("agora faço Z às 7h")
- Descobertas ("aprendi que W funciona melhor")
- Frustrações ("travei em K")

**Output esperado:**
```markdown
## Semana 46/2025 (13-19 Nov)

### ✅ Decisões Técnicas
- Confirmado B450M (não B550) - conversa 16/11 linha 2812
- Scrape v3.0 production ready - metodologia completa

### 🔄 Mudanças Rotina
- Adicionei 2 bananas/dia (meta proteína)
- Batch cooking agora 19-21h domingo

### 💡 Descobertas
- Conversational analysis > scoring automático (speakers)
- JSON vetorial > SQL relacional (backup mental)

### ⚠️ Frustrações Resolvidas
- Grok corrigia erroneamente Sonnet 4.5 → usar web search sempre
```

**Implementação:**
```python
# weekly_learnings.py
import spacy
from datetime import datetime, timedelta

nlp = spacy.load("pt_core_news_sm")

def extract_insights(transcricao_md):
    doc = nlp(transcricao_md)
    
    decisoes = [sent for sent in doc.sents if "decidi" in sent.text.lower()]
    mudancas = [sent for sent in doc.sents if "agora" in sent.text.lower()]
    descobertas = [sent for sent in doc.sents if "aprendi" in sent.text.lower()]
    
    return {
        'decisoes': decisoes,
        'mudancas': mudancas,
        'descobertas': descobertas
    }
```

**Prioridade:** 🔥 ALTA (PKM essencial, web research confirma)

---

### 3. 🌙 BackBrowser - Check-up Fim/Início Conversa
**Origem:** Linha 766-784 (finandev-backup-mental)

**O que é:** Agente detecta encerramento, faz perguntas rápidas

**Perguntas você propôs:**

**Fim conversa:**
- "Dormiu quantas horas ontem?"
- "Energia hoje 1-5?"
- "Maior ganho da semana?"
- "Algo que travou?"

**Início conversa:**
- "O que rolou de novo na cabeça?"
- "Insight do dia pra fixar?"

**Atualiza automaticamente:**
- `Rotinas/Sono.md`
- `Vida-Deivison.json` (energia array)
- `APRENDIZADOS-SEMANAIS.md`

**Implementação webhook:**
```javascript
// backbrowser.js
function detectEncerramento(mensagem) {
  const triggers = /vou encerrar|tchau|até|pão milho/i;
  if (triggers.test(mensagem)) {
    return {
      perguntas: [
        "Dormiu quantas horas?",
        "Energia 1-5?",
        "Ganho da semana?"
      ]
    };
  }
}
```

**Prioridade:** 🟡 MÉDIA (requer integração chat API)

---

### 4. ⏰ Detecção Horário/Contexto Automática
**Origem:** Linha 790 (finandev-backup-mental)

**O que é:** Agente sabe hora + dia, cruza com Rotinas/Diarias/*.md

**Exemplo você deu:**
```
14h terça → "Deveria estar no trabalho, certo?"
19h domingo → "Hora batch cooking! Lista pronta?"
```

**Implementação:**
```python
# context_detector.py
from datetime import datetime

def get_context():
    agora = datetime.now()
    dia = agora.strftime("%A").lower() # terça
    hora = agora.hour # 14
    
    rotina = load_md(f"Rotinas/Diarias/{dia}.md")
    bloco = parse_time(rotina, hora) # "14-17h: Trabalho"
    
    return f"Você tá em: {bloco['atividade']}"
```

**Prioridade:** 🟡 MÉDIA (útil mas não urgente)

---

### 5. 📸 Tracking Visual Corpo/Moda
**Origem:** Linha 1258-1264 (finandev), 695-731 (prompt-voz)

**O que é:** Fotos periódicas corpo + outfit, análise temporal

**Você quer:**
- Meta: 60kg → 70kg (maio/2026)
- Fotos semanais (9 poses fitness)
- Outfit diário (evolução moda)
- Setup 360° (Relic Mode 10 anos)

**Estrutura:**
```
Celular/Camerologia/
  Tracking-Corpo/2025-11/16-frente-60kg.jpg
  Outfit-Diario/16-camisa-preta.jpg
  360-Setup/16-setup-completo.jpg
  ANALISE-VISUAL.md (métricas)
```

**Apps sugeridos (web research 2025):**
- Metamorph (líder progress photos)
- Gym Body Tracker (9 pontos medição)
- Me 360 (scan 3D corpo)

**GCam configs:**
- MGC 9.4 BSG (panorama 360°)
- LMC 8.4 R18 (HDR+ corpo)

**Prioridade:** 🟢 BAIXA (requer disciplina foto regular)

---

### 6. 💰 Finanças API - Comparador Preços
**Origem:** Linha 946 (finandev-backup-mental)

**O que é:** Scrape Shopee + Mercado Livre, retorna menor preço

**Caso de uso você deu:**
```
Input: "Adaptador DisplayPort → VGA"
Output:
- Shopee: R$ 25,90 + frete R$ 12 = R$ 37,90
- ML: R$ 29,90 frete grátis
→ Recomenda: ML (entrega 3 dias)
```

**Implementação:**
```javascript
// price_compare.js
async function comparePrice(produto) {
  const shopee = await scrapeShopee(produto);
  const ml = await scrapeMercadoLivre(produto);
  
  return {
    melhor: shopee.total < ml.total ? 'shopee' : 'ml',
    economia: Math.abs(shopee.total - ml.total)
  };
}
```

**Dados web 2025:**
- Shopee Brasil: 8% mercado, +25%/ano
- ML: 13% mercado, API oficial
- Scraping legal para preços públicos

**Prioridade:** 🟢 BAIXA (legalidade APIs, complexo)

---

### 7. 📱 Sensor-Rotina - Automação Física
**Origem:** Linha 1037-1087 (prompt-modo-voz)

**O que é:** Termux lê sensores Poco X5 → dispara ações

**Exemplos você propôs:**
```python
# Sedentarismo
acelerometro < 0.1 (30min) → "Levanta! Caminha 5min"

# Batch Cooking
luz_ambiente < 100 (escurecendo) → "Hora cozinhar!"

# Treino
giroscopio detecta rotações → conta repetições
```

**Sensores Poco X5:**
- Acelerômetro, giroscópio, magnetômetro
- Luz ambiente, proximidade
- Todos acessíveis via `termux-sensor`

**Implementação:**
```bash
# Termux
termux-sensor -s accelerometer | python3 sensor_routine.py
```

**Prioridade:** 🟢 BAIXA (setup Termux complexo)

---

### 8. 😴 Mini-Sistema Sono
**Origem:** Linha 1087-1149 (prompt-modo-voz)

**O que é:** Acelerômetro noturno + correlação humor/energia

**Você mencionou apps:**
- Sleep as Android (export JSON)
- Sleep Cycle (API)

**Análise proposta:**
```python
# sleep_analysis.py
sono = load_json("sleep_android_export.json")
humor = load_json("Vida-Deivison.json")["energia"]

correlacao = sono['qualidade'].corr(humor)
# Output: -0.78 (sono ruim → energia baixa 78%)
```

**Prioridade:** 🟢 BAIXA (depende apps externos)

---

## 🌍 Ideias Expandidas (Além Mini-Sistemas)

### 9. 🔗 Prompt Modo Voz Universal
**Origem:** Linha 656-682 (finandev-backup-mental)

**O que é:** PROMPT-MODO-VOZ.md como boot agentes IA

**Você quer migrar:**
- Teste-assitentevoz repo → FinanDEV
- Contexto PC + Mobile unificado
- Protocolos CO5P + VNE documentados

**Status:** ✅ FEITO (transcricao-prompt-modo-voz.md capturou) - Usado regularmente nas conversas Grok

---

### 10. 🎮 Bot WhatsApp Grupo Família
**Origem:** Linha 1632-1638 (finandev-backup-mental)

**O que é:** Bot acorda grupo com vídeos personalizados

**Ideias você deu:**
- Mensagem matinal: "Ei João, lembra da ideia sexta? Fiz gif"
- Mini rifas coletivas: "R$ 10 almoço mês"
- Reestruturação madrugada → acordam com novidade

**Implementação:**
- Baileys (WhatsApp Web API)
- Cronjob 7h manhã
- Gemini gera mensagens personalizadas

**Prioridade:** 🟢 BAIXA (projeto social, não backup mental)

---

### 11. 🏢 Orquestração CETENS - Upgrades PC
**Origem:** Linha 1446-1500 (finandev-backup-mental)

**O que é:** Metas mini-tarefas trabalho até fim 2025

**Você mencionou:**
- Upgrade OptiPlex 7010: 8GB RAM + SSD
- Mini-sistemazinhos orquestração diária
- Repo separado: Orquestração-Settings

**Prioridade:** 🟢 BAIXA (contexto profissional específico)

---

### 12. 🌐 FinanDEV Open Source Comunitário
**Origem:** Linha 98 (finandev-backup-mental - Grok sugeriu)

**O que é:** Template clonável outros devs (especialmente Bahia)

**Potencial:**
- 150% crescimento PKM tools pós-2023
- Foco TDAH/neuroatípicos
- Inclusão digital via backup mental acessível

**Prioridade:** 🟡 MÉDIA (longo prazo, impacto social)

**Atualização 02/DEZ:** Com +33 repositórios novos em 16 dias, você já está semi-open source na prática. Falta documentar e organizar.

---

## 📊 Priorização Global (Framework RICE)

| Ideia | Reach | Impact | Confidence | Effort | Score |
|-------|-------|--------|------------|--------|-------|
| Sistema Aliases | 10 | 9 | 90% | 2 sem | 40.5 |
| Aprendizados Semanais | 10 | 10 | 95% | 1 sem | 95 |
| BackBrowser | 8 | 7 | 80% | 3 sem | 14.9 |
| Detecção Horário | 6 | 6 | 70% | 2 sem | 12.6 |
| Tracking Visual | 7 | 8 | 60% | 4 sem | 8.4 |
| Finanças API | 5 | 7 | 50% | 6 sem | 2.9 |
| Sensor-Rotina | 4 | 6 | 40% | 5 sem | 1.9 |
| Sono Análise | 6 | 7 | 50% | 3 sem | 7 |

**Top 3 implementar primeiro:**
1. 🥇 Aprendizados Semanais (95 pts)
2. 🥈 Sistema Aliases (40.5 pts)
3. 🥉 BackBrowser (14.9 pts)

---

## ✅ Próximos Passos Concretos

**Esta semana (02-08 DEZ):**
- [ ] **DIA 5 (sexta):** Receber salário, pagar contas, abrir Mini-Sistema Final-Dezembro
- [ ] **DIA 6 (sábado):** Primeiro script Playwright com storage_state salvo (mesmo com erro)
- [ ] Tirar primeira foto tracking visual (baseline corpo)
- [ ] Ativar Sleep as Android compartilhamento dados

**Até dia 15 DEZ (segunda):**
- [ ] Estar de boa: contas pagas, compras feitas, roupas novas
- [ ] 3+ aplicações via Playwright funcionando
- [ ] Canal anônimo: gerar modelo 3D no Luma/Flux

**2026 (longo prazo):**
- [ ] Sair CETENS até março/2026 (salário-alvo 2k líquido)
- [ ] Finanças API MVP
- [ ] Sensor-Rotina Termux setup
- [ ] Open source FinanDEV comunitário
- [ ] DevSan Open School (ajudar jovens pobres com código)

---

## 🔗 Referências Completas (Web Research 2025)

**PKM Automation:**
- dsebastien.net: 8000 notas + 64000 links analysis
- Obsidian Auto Note Mover plugin
- Logseq weekly templates
- AppFlowy share to database (iOS/Android)

**Voice AI Context:**
- Pageon.ai: Top AI Voice Assistants 2025
- Trengo: Custom wake words + speech-to-meaning
- Otter.ai: Real-time transcription (72% time save)
- Andreessen Horowitz: Voice bots outperform humans

**Smartphone Sensors:**
- YouTube: Mining sensor data with Python
- Termux-sensor wiki (JSON output)
- Sleep as Android sensor docs
- Medium: Sleep tracking accelerometer ML

**E-commerce Brasil:**
- Slashdot: Mercado Libre vs Shopee comparison
- Shopee Brazil: 8% mercado, +25% growth
- ML API oficial disponível
- Web scraping legal preços públicos

**Fitness Photography:**
- Trainero: Visual progress tracking (9 points)
- Metamorph: Leading app 2025
- Gym Body Tracker: OCR measurements
- Me 360: 3D body scan phone camera

---

**Última atualização:** 02/DEZ/2025  
**Próxima revisão:** Dia 5 (recebe salário) ou Dia 15 (deadline final dezembro)

---

## 🔥 ATUALIZAÇÕES 02/DEZ/2025 (Conversa Grok 2h+)

### Status Geral
- **Peso:** 60kg (mais magro, dieta furada)
- **Sono:** Completamente desregulado (~00:00)
- **Ansiedade:** 9/10
- **Orgulho:** +33 repositórios criados em 16 dias
- **CETENS:** Frustrado, saída planejada março/2026

### Novas Pendências Críticas
1. **Tracking Visual** → Primeira foto nunca tirada
2. **Mini-Sistema Sono** → Sleep as Android instalado, dados não compartilhados
3. **Finanças Dezembro** → Não existe arquivo, dia 5 cai salário
4. **New-Job Automations** → storage_state.json nunca salvo, 10 aplicações manuais
5. **Aprendizados Semanais** → Template existe, zero entradas

### Novas Ideias Capturadas
- **DriveDroid** → Instalado Poco X5, ISO Windows 11 pendente
- **Canal Anônimo** → Avatar 3D + voz IA (500 fotos, zero modelo gerado)
- **DevSan Open School** → Ajudar jovens pobres com código (planejado)
- **Mini-Sistema Final-Dezembro** → Controle finanças fim de ano

---
