# 🧠 Sistema de Saúde Mental

> **Objetivo:** Monitorar padrões de sono, energia, humor e estresse  
> **Criado:** 16/11/2025  
> **Última Atualização:** 16/11/2025  
> **Integra com:** ROTINA-VIDA-DEIVISON-2025.md, CONTEXTO-TRABALHO-CETENS.md

---

## 📊 Métricas Principais

### 1. Sono
- **Horas dormidas:** Total de sono por noite
- **Qualidade:** Escala 0-10 (subjetivo)
- **Horário deitar/acordar:** Tracking de padrão circadiano

### 2. Energia Diária
- **Escala:** 0-10
  - 0-3: Exausto, mal consegue funcionar
  - 4-6: Operacional mas cansado
  - 7-9: Energia boa, produtivo
  - 10: Pico de energia, fluxo total

### 3. Humor Pós-Trabalho
- **Estados:** Neutro / Positivo / Negativo
- **Nota descritiva:** Contexto breve

### 4. Estresse
- **Fonte:** CETENS / Finanças / Social / Pessoal
- **Nível:** Baixo / Médio / Alto

---

## 📅 Registro Semanal

### Semana 16-22/11/2025

| Dia | Sono  | Qualidade | Energia | Humor       | Estresse | Notas |
|-----|-------|-----------|---------|-------------|----------|-------|
| 16  | 5h    | 4/10      | 4/10    | Neutro      | Médio    | Madrugada coding 3h+ com Grok, CETENS tedioso |
| 17  |       |           |         |             |          |  |
| 18  |       |           |         |             |          |  |
| 19  |       |           |         |             |          |  |
| 20  |       |           |         |             |          |  |
| 21  |       |           |         |             |          |  |
| 22  |       |           |         |             |          |  |

**Média Semanal:**
- Sono: -- h/noite
- Energia: --/10
- Humor predominante: --

---

## 🔍 Padrões a Observar

### Sono vs. Produtividade
- **Hipótese:** <6h sono = energia <5/10 no dia seguinte?
- **Teste:** Comparar semanas com 7h+ vs. 5h- de sono

### Trabalho vs. Humor
- **Hipótese:** Dias no CETENS sem chamados = humor neutro/negativo (tédio)?
- **Teste:** Correlacionar dias ociosos com humor

### Madrugadas Coding vs. Energia
- **Hipótese:** Madrugadas produtivas (Grok, projetos) drenam energia mas melhoram humor?
- **Teste:** Dias pós-madrugada vs. energia/humor

---

## 🔗 Integração com Outros Sistemas

### ROTINA-FISICA.md
- Peso estagnado + energia baixa = possível déficit calórico?
- Humor negativo persistente = rever alimentação?

### CONTEXTO-TRABALHO-CETENS.md
- Frustração no trabalho impacta sono?
- Dias sem desafios = tédio = baixa energia?

### LEARNINGS.md
- Extrair insights semanais sobre padrões mentais
- "Semana X: Descobri que 5h sono = -30% produtividade"

---

## 🤖 Automação Futura

### Sistema Backbrowser (SLEEP-TRACKING.md)
- **Fonte:** Browser history, logs de terminal, commits GitHub
- **Detecção automática:**
  - Último comando terminal = hora de dormir aproximada
  - Primeiro commit do dia = hora de acordar aproximada
- **Output:** Gráfico semanal de sono sem input manual

### Alertas Inteligentes
- Se energia <4/10 por 3 dias seguidos → sugerir break/ajuste rotina
- Se sono <6h por 5 dias → alerta "risco de burnout"

---

## 📝 Template de Entrada Diária

```markdown
## YYYY-MM-DD (Dia da Semana)
**Sono:** Xh (deitar HH:MM, acordar HH:MM)  
**Qualidade:** X/10  
**Energia:** X/10  
**Humor:** Neutro/Positivo/Negativo  
**Estresse:** Fonte + Nível (Baixo/Médio/Alto)  
**Nota:** Contexto breve (ex: "Madrugada refatorando FinanDEV, CETENS sem chamados")
```

---

## 🧪 Experimentos Futuros

### Teste 1: Rotina de Respiração Quadrada
- **Método:** 5min manhã (acordar) conforme ROTINA-VIDA-DEIVISON
- **Hipótese:** Melhora qualidade sono + energia diária?
- **Duração:** 2 semanas
- **Métrica:** Comparar energia média antes/depois

### Teste 2: Limite de Madrugadas Coding
- **Método:** Max 2 madrugadas/semana (após 02:00)
- **Hipótese:** Reduz fadiga acumulada sem perder produtividade?
- **Duração:** 1 mês
- **Métrica:** Energia semanal média

---

## 🎯 Metas de Saúde Mental (2026)

- [ ] Média 6.5h+ sono/noite (consistência)
- [ ] Energia média 7/10 (sustentável)
- [ ] Humor predominante Neutro→Positivo (ambiente de trabalho melhor)
- [ ] Estresse Baixo 70% dos dias (controle ambiental)

---

*Sistema ativo | Revisão semanal | Ajustes mensais*
