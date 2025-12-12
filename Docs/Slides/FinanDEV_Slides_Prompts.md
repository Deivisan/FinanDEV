# FinanDEV — Prompts para Notebook LM (Slides)

> Objetivo: Gerar uma apresentação de até 12 slides que represente o workspace FinanDEV, sua identidade, rotinas, mini-sistemas, tecnologia e roteiros de ação.

Resumo rápido
- Fonte de verdade (prioridade): `CORE/Vida-Deivison.json`, `CORE/Deivison.md`, `CORE/DeiviTech.md`, `ROTINA-VIDA-DEIVISON-2025.md`.
- Transcrições (intocáveis): `Transcricoes/*` (usar como referência de conteúdo e citações).
- Imagens locais: `Ambiente-Dev/Celular/Camerologia/` (usar fotos 360°/tracking se existirem). Caso a imagem não exista, gerar uma alternativa AI (descrições abaixo).
- Exportar slides para `Docs/Slides/FinanDEV_Presentation/` (PNG por slide + PDF final).

Configurações de estilo para o Notebook LM
- Tema: Dark (bg #0f1720), accent #00ff88, fonte Inter / Montserrat.
- Formato: 16:9.
- Layout: Título + 3–5 bullets + imagem/visual + 2–3 notas do apresentador por slide.
- Acessibilidade: gerar alt-text para cada imagem.

Direção geral para o Notebook LM
1. Ler os arquivos CORE mencionados para buscar dados e citações exatas.
2. Gerar 12 slides conforme o roteiro a seguir; se faltar dados, criar placeholders "TO_FILL: <source>".
3. Para gráficos, usar matplotlib/plotly com dados extraídos de `CORE/Vida-Deivison.json`.
4. Salvar arte final e imagens geradas em `Docs/Slides/FinanDEV_Presentation/`.

---

## Slides (1–12)

1) Slide 1 — Capa
- Prompt: "Crie uma capa visual para FinanDEV: Título ‘FinanDEV — Backup Mental & Roadmap’, subtítulo ‘Deivison Santana (25)’, incluir data última atualização do `CORE/Vida-Deivison.json`."
- Imagem prompt (AI): "Retrato cyber-neon estilizado de um dev 25 anos, traços afro-brasileiros, tom confiante, fundo escuro, neon green accents, 3D/2D híbrido, high contrast".
- Conteúdo: Nome, objetivo da apresentação, 1 linha: "Sistema escrito = hack vida".
- Notas apresentador: 1-min resumo da missão do workspace.

2) Slide 2 — Identidade & Filosofia
- Prompt: "Resuma a identidade (perfil psicológico e filosofia) com 3 bullets e 1 citação: 'Se não tá escrito, esqueço.'"
- Data source: `CORE/Deivison.md`.

3) Slide 3 — Arquitetura do Backup Mental (diagrama)
- Prompt: "Desenhe um diagrama mostrando a arquitetura: `CORE/Vida-Deivison.json` → `Transcricoes/` → `Rotinas/` → `Mini-Sistemas/` → `Ambiente-Dev/`"
- Visual: esquema com nodes e setas, cor accent verde.
- Nota apresentador: como qualquer IA entende o workspace.

4) Slide 4 — Rotina & Roadmap (gráfico)
- Prompt: "Plote um gráfico timeline de peso (Nov→Mai alvo 70kg) usando dados de `CORE/Vida-Deivison.json` e com anotações das missões quinzenais".
- Código snippet: incluir pandas+matplotlib sample para o notebook LM (ver abaixo).

5) Slide 5 — Mini-systems ativos (cards)
- Prompt: "Crie 4 cards visuais com: Saúde Mental, Sleep Tracking, FalaComTodos, ImpulsosRegistrados; para cada card 1-2 métricas chave e estado atual."
- Source: `Mini-Sistemas/Ativos/*` e JSON.

6) Slide 6 — Tech Stack & Projects Snapshot
- Prompt: "Resumo visual dos principais repositórios e stack (DeiviTech, FreelancerDeiviTech, automation-scripts, Eventos-FSA)." 
- Visual: tiles com badges (Tailwind, Python, Playwright, Gemini, Copilot).

7) Slide 7 — Camerologia & Face-Capture
- Prompt: "Exibir metodologia para tracking visual: 9-poses grid + 360-setup. Usar `Ambiente-Dev/Celular/Camerologia/` assets; se vazios, gerar AI 9-pose photorealistic grid".
- Nota: explicar pipeline MediaPipe → SVG → Animação.

8) Slide 8 — Finanças & Orçamento (gráfico)
- Prompt: "Criar pie chart com gastos fixos (água, luz, internet) vs sobra; use `CORE/Vida-Deivison.json`."

9) Slide 9 — Perfil psicológico: pontos fortes & contramedidas
- Prompt: "Infográfico: impulsividade, perfeccionismo, memória frágil; listar 3 contramedidas acionáveis (alarme jantar, write-it-down, ImpulsosRegistrados).",
- Source: `CORE/Deivison.md`.

10) Slide 10 — Comunidade & Parcerias
- Prompt: "Mapa ideias: Events-FSA, DevSan Open School, open-source FinanDEV; listar CTAs: contribua, teste, invista".
- Visual: mind map, logos de github/discord/telegram.

11) Slide 11 — Ideias disruptivas & roadmap de experimentos
- Prompt: "Cards: Aprendizados Semanais script, Sistema Aliases, BackBrowser, Sensor-Rotina (Termux). Incluir prioridade (RICE)." 
- Source: `Ideias/` + `ANALISE-CRONOLOGICA-COMPLETA.md`.

12) Slide 12 — Próximos Passos & CTA
- Prompt: "Timeline 0–7d, 7–30d, 30–90d com 5 ações imediatas: fotos tracking, storage_state.json, terapia SUS, conserto bike, new-job automations; incluir link para `Plano-Organizado.md`."

---

## Prompts de Imagem (curtos — a serem passados ao gerador de imagens)
- Avatar (slide 1): "Afro-Brazilian dev, neon cyberpunk portrait, subtle smile, 3D hybrid, accent green".
- 360 Setup (slide 7): "Dev desk 2 monitors, Ryzen 7 5700G, black desk, neon green accent, photorealistic".
- 9-pose tracking grid: "Male model 9-pose grid, neutral background, consistent lighting, photorealistic".
- Financial chart art: "Minimalist pie chart vector with neon accents".
- Tech stack collage: "Icons: HTML5, Tailwind, Python, Playwright, Gemini, paired as modern badges".

## Código de exemplo (p/ Notebook LM): gráficos e extratores
- Extração peso e plot (pandas + matplotlib):
```python
import json, pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

root = Path('CORE')
vida = json.load(open(root/'Vida-Deivison.json', 'r', encoding='utf-8'))
# Estrutura: vida.get('meta','tracking') ou parse rotinas
tracking = vida.get('meta', {}).get('tracking', [])
# fallback from `rotina_semanal` in `vida['rotina_semanal']`
if not tracking and 'rotina_semanal' in vida:
    months = []
    for k,v in vida['rotina_semanal'].items():
        # placeholder dựng for monthly
        pass

# Plot exemplo
# months = ['Nov','Dec','Jan'] ; weights = [61, 62.5, 64]
# plt.plot(months, weights, marker='o')
# plt.title('Weight Tracking')
# plt.savefig('Docs/Slides/FinanDEV_Presentation/slide4_weight.png')
```

- Pie chart de finanças:
```python
data = vida.get('financas', {})
fixos = data.get('gastos_fixos', {})
labels = list(fixos.keys())
values = [fixos[k] for k in labels]
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Gastos Fixos')
plt.savefig('Docs/Slides/FinanDEV_Presentation/slide8_finances.png')
```

- Timeline events from transcripts:
```python
import frontmatter, glob, pandas as pd
files = glob.glob('Transcricoes/*.md')
events = []
for f in files:
    p = frontmatter.load(f)
    dt = p.get('data_conversa') or p.get('data_captacao')
    if dt:
        events.append({'date': dt, 'file': f})
# Plot timeline or print events list
```

---

## Export e Commit (após geração)
- Salvar cada slide PNG em `Docs/Slides/FinanDEV_Presentation/` e o PDF `Docs/Slides/FinanDEV_Presentation.pdf`.
- Comando para rodar (no notebook):
```bash
# dentro do notebook: gerar slides
python export_slides.py --output Docs/Slides/FinanDEV_Presentation/FinanDEV_Presentation.pdf
# depois commitar
git add Docs/Slides/FinanDEV_Presentation/ ; git commit -m "Add generated FinanDEV slides" ; git push
```

---

## Observações e preferências
- Não apagar transcrições originais em `Transcricoes/`.
- Se a imagem real do `Ambiente-Dev/Celular/` existir, prefira essa imagem; se preferir placeholder, gere imagens AI e insira label "GENERATED".
- Manter slides enxutos e com máximo impacto visual.

---

## Vantagem desse método
- Deck pronto para apresentação com dados reais e design visual atualizado.
- Reutilizável como index para roteiros, entrevistas e procura de emprego.

---

Pronto: criei o prompt de forma inteligente e objetiva para que o Notebook LM gere a apresentação. Quer que eu gere agora as imagens automaticamente (AI) ou que eu só produza os slides placeholders com gráficos? 