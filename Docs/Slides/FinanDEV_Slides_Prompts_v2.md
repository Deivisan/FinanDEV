# FinanDEV — Prompts para Notebook LM (Slides) [Versão Disruptiva 2.0]

> Objetivo: Gerar uma apresentação de até 12 slides que represente o workspace FinanDEV como um sistema vivo, inteligente e disruptivo — identidade, rotinas, mini-sistemas, tecnologia, ideias políticas e roteiros de ação. Foco: Inventivo, curioso, visualmente impactante, com elementos de surpresa e inovação.

Resumo rápido
- Fonte de verdade (prioridade): `CORE/Vida-Deivison.json`, `CORE/Deivison.md`, `CORE/DeiviTech.md`, `ROTINA-VIDA-DEIVISON-2025.md`.
- Transcrições (intocáveis): `Transcricoes/*` (usar como referência de conteúdo e citações curiosas, e.g., insights de conversas com Grok).
- Imagens locais: `Ambiente-Dev/Celular/Camerologia/` (usar fotos 360°/tracking se existirem). Caso a imagem não exista, gerar alternativas AI disruptivas (descrições abaixo — focar em cyberpunk, neon, híbrido 3D/2D).
- Exportar slides para `Docs/Slides/FinanDEV_Presentation/` (PNG por slide + PDF final + animações GIF se possível).

Configurações de estilo para o Notebook LM
- Tema: Cyberpunk Dark (bg #0f1720), accent #00ff88 (neon green), fonte Inter / Montserrat — com glitch effects sutis para slides disruptivos.
- Formato: 16:9, com transições animadas (fade-in, zoom).
- Layout: Título + 3–5 bullets inventivos + imagem/visual disruptiva (e.g., mind maps animados, infográficos 3D) + 2–3 notas do apresentador curiosas.
- Acessibilidade: gerar alt-text para cada imagem; incluir citações de transcrições para humanizar.

Direção geral para o Notebook LM
1. Ler os arquivos CORE mencionados para buscar dados e citações exatas; extrair insights curiosos de `Transcricoes/` (e.g., "como hackear a vida com scripts").
2. Gerar 12 slides conforme o roteiro a seguir; se faltar dados, criar placeholders "TO_FILL: <source>" com twist inventivo.
3. Para gráficos, usar matplotlib/plotly com dados extraídos de `CORE/Vida-Deivison.json` — adicionar animações ou elementos visuais disruptivos (e.g., particles, neon overlays).
4. Salvar arte final e imagens geradas em `Docs/Slides/FinanDEV_Presentation/`; incluir versão animada se suportado.
5. Injetar curiosidade: Adicionar perguntas retóricas, citações disruptivas, e elementos visuais que "quebrem a quarta parede" (e.g., avatars interativos).

---

## Slides (1–12) — Versão Disruptiva

1) Slide 1 — Capa Disruptiva
- Prompt: "Crie uma capa visual cyberpunk para FinanDEV: Título 'FinanDEV — Hack da Vida', subtítulo 'Deivison Santana (25) — Sistema Vivo', incluir data última atualização do `CORE/Vida-Deivison.json` com efeito glitch."
- Imagem prompt (AI): "Retrato cyber-neon estilizado de um dev 25 anos afro-brasileiro, traços confiantes com implantes digitais, fundo escuro com matrix code, neon green accents, 3D/2D híbrido, high contrast, glitch overlay para surpresa visual".
- Conteúdo: Nome, objetivo: "Sistema escrito = hack vida", citação disruptiva: "Se não tá escrito, esqueço — mas agora, lembro tudo."
- Notas apresentador: 1-min resumo: "Este workspace é meu backup mental, e você vai ver como ele transforma caos em ordem."

2) Slide 2 — Identidade & Filosofia (Mind Map Interativo)
- Prompt: "Resuma a identidade (perfil psicológico e filosofia) com 3 bullets inventivos e 1 citação curiosa de `Transcricoes/`: 'Impulsividade é meu superpoder disfarçado.' Gerar mind map animado conectando TDAH, perfeccionismo e memória frágil."
- Data source: `CORE/Deivison.md` + citações de transcrições (e.g., insights sobre impulsos).

3) Slide 3 — Arquitetura do Backup Mental (Diagrama 3D Disruptivo)
- Prompt: "Desenhe um diagrama 3D cyberpunk mostrando a arquitetura: `CORE/Vida-Deivison.json` → `Transcricoes/` → `Rotinas/` → `Mini-Sistemas/` → `Ambiente-Dev/` — com setas neon e nodes flutuantes, efeito de 'sistema vivo'."
- Visual: esquema com nodes e setas, cor accent verde, glitch para curiosidade.
- Nota apresentador: "Qualquer IA entende isso — imagine o que você pode hackear na sua vida."

4) Slide 4 — Rotina & Roadmap (Gráfico Timeline Inventivo)
- Prompt: "Plote um gráfico timeline animado de peso (Nov→Mai alvo 70kg) usando dados de `CORE/Vida-Deivison.json`, com anotações disruptivas das missões quinzenais e citações curiosas (e.g., 'Bike consertada: vitória contra a procrastinação')."
- Código snippet: incluir pandas+matplotlib sample com animação (ver abaixo).

5) Slide 5 — Mini-systems Ativos (Cards Holográficos)
- Prompt: "Crie 4 cards visuais holográficos com: Saúde Mental, Sleep Tracking, FalaComTodos, ImpulsosRegistrados; para cada card 1-2 métricas chave, estado atual e twist curioso (e.g., 'Impulsos: meu diário de loucuras')."
- Source: `Mini-Sistemas/Ativos/*` e JSON.

6) Slide 6 — Tech Stack & Projects Snapshot (Collage Disruptivo)
- Prompt: "Resumo visual dos principais repositórios e stack (DeiviTech, FreelancerDeiviTech, automation-scripts, Eventos-FSA) — com badges animados e efeitos neon, incluindo pergunta retórica: 'O que um dev 25 anos pode construir?'"
- Visual: tiles com badges (Tailwind, Python, Playwright, Gemini, Copilot) em layout 3D.

7) Slide 7 — Camerologia & Face-Capture (Grid 9-Pose Inovador)
- Prompt: "Exibir metodologia para tracking visual: 9-poses grid + 360-setup com efeito cyberpunk. Usar `Ambiente-Dev/Celular/Camerologia/` assets; se vazios, gerar AI 9-pose photorealistic grid com twist curioso (e.g., poses 'disruptivas' como 'pose de hackear')."
- Nota: explicar pipeline MediaPipe → SVG → Animação, com citação: "Tracking visual: meu olho no futuro."

8) Slide 8 — Finanças & Orçamento (Gráfico Pie Disruptivo)
- Prompt: "Criar pie chart 3D com gastos fixos (água, luz, internet) vs sobra; use `CORE/Vida-Deivison.json` — adicionar animação de 'explosão' para destacar sobras, com pergunta: 'Quanto sobra para hackear?'"

9) Slide 9 — Perfil Psicológico: Pontos Fortes & Contramedidas (Infográfico Curioso)
- Prompt: "Infográfico neon: impulsividade, perfeccionismo, memória frágil; listar 3 contramedidas acionáveis (alarme jantar, write-it-down, ImpulsosRegistrados) — incluir citações disruptivas de transcrições (e.g., 'Perfeccionismo: meu inimigo invisível').",
- Source: `CORE/Deivison.md`.

10) Slide 10 — Comunidade & Parcerias (Mapa Mental Inovador)
- Prompt: "Mapa ideias animado: Events-FSA, DevSan Open School, open-source FinanDEV; listar CTAs curiosos: 'Contribua e hackeie junto', 'Teste meu caos organizado', 'Invista no futuro disruptivo'."
- Visual: mind map com logos de github/discord/telegram, efeitos flutuantes.

11) Slide 11 — Ideias Disruptivas & Roadmap de Experimentos (Cards com Twist)
- Prompt: "Cards neon: Aprendizados Semanais script, Sistema Aliases, BackBrowser, Sensor-Rotina (Termux). Incluir prioridade (RICE) e citações inventivas (e.g., 'BackBrowser: navegador do passado para insights futuros')."
- Source: `Ideias/` + `ANALISE-CRONOLOGICA-COMPLETA.md`.

12) Slide 12 — Aspecto Político & Próximos Passos (Timeline Disruptivo)
- Prompt: "Adicionar visão política: ideias sobre sociedade, tecnologia e mudança (e.g., 'Tecnologia para igualdade social'). Timeline 0–7d, 7–30d, 30–90d com 5 ações imediatas: fotos tracking, storage_state.json, terapia SUS, conserto bike, new-job automations; incluir link para `Plano-Organizado.md` e CTA: 'Junte-se à revolução pessoal'."
- Visual: Timeline com elementos políticos (e.g., ícones de protesto, inovação social).

---

## Prompts de Imagem (Disruptivos — Curiosos e Inventivos)
- Avatar (slide 1): "Afro-Brazilian dev, neon cyberpunk portrait, subtle smile com implante digital, 3D hybrid, accent green, glitch effect".
- 360 Setup (slide 7): "Dev desk 2 monitors, Ryzen 7 5700G, black desk, neon green accent, photorealistic com matrix code background".
- 9-pose tracking grid: "Male model 9-pose grid, neutral background, consistent lighting, photorealistic com poses 'hackeadoras' (e.g., typing furiously, thinking deeply)".
- Financial chart art: "Minimalist pie chart vector with neon accents e explosão animada".
- Tech stack collage: "Icons: HTML5, Tailwind, Python, Playwright, Gemini, paired as modern badges com efeitos holográficos".
- Novo: Mind Map (slide 2): "Neon mind map com nodes flutuantes, conectores animados".
- Timeline (slide 12): "Cyberpunk timeline com ícones políticos (balança, engrenagem, revolução)".

## Código de Exemplo (P/ Notebook LM): Gráficos e Extratores com Twist
- Extração peso e plot (pandas + matplotlib com animação):
```python
import json, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

root = Path('CORE')
vida = json.load(open(root/'Vida-Deivison.json', 'r', encoding='utf-8'))
tracking = vida.get('meta', {}).get('tracking', [])
if not tracking and 'rotina_semanal' in vida:
    # Parse rotina_semanal for weights
    months = list(vida['rotina_semanal'].keys())
    weights = [vida['rotina_semanal'][m].get('peso', 0) for m in months]

# Plot animado disruptivo
fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o', color='#00ff88')
ax.set_xlim(0, len(months))
ax.set_ylim(min(weights)-5, max(weights)+5)
ax.set_title('Weight Tracking — Hack do Corpo')

def animate(i):
    line.set_data(months[:i+1], weights[:i+1])
    return line,

ani = FuncAnimation(fig, animate, frames=len(months), interval=500)
ani.save('Docs/Slides/FinanDEV_Presentation/slide4_weight.gif')
```

- Pie chart de finanças com explosão:
```python
data = vida.get('financas', {})
fixos = data.get('gastos_fixos', {})
labels = list(fixos.keys())
values = [fixos[k] for k in labels]
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%', explode=[0.1]*len(values), colors=['#00ff88', '#ff0088', '#8800ff'])
ax.set_title('Gastos Fixos — Onde Hackear?')
plt.savefig('Docs/Slides/FinanDEV_Presentation/slide8_finances.png')
```

- Timeline events from transcripts com curiosidade:
```python
import frontmatter, glob, pandas as pd
files = glob.glob('Transcricoes/*.md')
events = []
for f in files:
    p = frontmatter.load(f)
    dt = p.get('data_conversa') or p.get('data_captacao')
    insight = p.get('conteudo', '').split('.')[0]  # Primeiro insight curioso
    if dt:
        events.append({'date': dt, 'insight': insight, 'file': f})
# Plot timeline com annotations
df = pd.DataFrame(events)
df['date'] = pd.to_datetime(df['date'])
df.sort_values('date', inplace=True)
plt.figure(figsize=(10,5))
plt.scatter(df['date'], [1]*len(df), c='#00ff88')
for i, row in df.iterrows():
    plt.annotate(row['insight'], (row['date'], 1), xytext=(5,5), textcoords='offset points')
plt.title('Insights Curiosos das Transcrições')
plt.savefig('Docs/Slides/FinanDEV_Presentation/timeline_insights.png')
```

---

## Export e Commit (Após Geração)
- Salvar cada slide PNG/GIF em `Docs/Slides/FinanDEV_Presentation/` e o PDF `Docs/Slides/FinanDEV_Presentation.pdf`.
- Comando para rodar (no notebook):
```bash
# Dentro do notebook: gerar slides com animações
python export_slides.py --output Docs/Slides/FinanDEV_Presentation/FinanDEV_Presentation.pdf --animations
# Depois commitar
git add Docs/Slides/FinanDEV_Presentation/ ; git commit -m "Add disruptive FinanDEV slides v2.0" ; git push
```

---

## Observações e Preferências Disruptivas
- Não apagar transcrições originais em `Transcricoes/`.
- Se a imagem real do `Ambiente-Dev/Celular/` existir, prefira essa imagem; se preferir placeholder, gere imagens AI disruptivas e insira label "GENERATED — Cyber Hack".
- Manter slides enxutos, mas com máximo impacto visual e curiosidade — adicionar perguntas retóricas para engajar o público.
- Twist final: Incluir um slide bônus se o Notebook LM permitir, com "O que você hackearia na sua vida?".

---

## Vantagem Desse Método Disruptivo
- Deck pronto para apresentação com dados reais, design cyberpunk e elementos inventivos — lembrado 6x melhor devido ao visual superiority effect.
- Reutilizável como index para roteiros, entrevistas e procura de emprego — transforme caos em inovação.

---

Pronto: Versão 2.0 mais disruptiva, inventiva e curiosa. Captou a ideia original e elevou com twists políticos, animações e citações. Quer gerar agora ou ajustar mais? 🚀💡