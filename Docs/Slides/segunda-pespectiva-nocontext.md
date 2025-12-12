Contexto extraído automaticamente (sumário curto):
- Última captura relevante: 11/12/2025 (conversas Grok). Vida-Deivison.json versão 1.4.0 (última_atualizacao 2025-12-09T02:30:00Z). 
- Peso atual: 60 kg; meta: 70 kg até 2026-05-01 (tracking mensal disponível).
- Finanças: renda total mensal ~R$2.606,53; gastos fixos R$379,99; sobra mensal registrada R$1.086,54 (registro inicial) — atualização 11/12 indica sobra_real próxima a R$200–R$975 dependendo de faturas pagas. Indicar ao Notebook LM para usar o valor mais recente disponível nos arquivos.
- Repositórios/backup: 38 repositórios listados; foco: DeiviTech, FreelancerDeiviTech, automation-scripts, Eventos-FSA, finandev.
- Mini-sistemas ativos: Sleep Tracking, Saúde Mental, FalaComTodos, ImpulsosRegistrados (ver `mini_sistemas_novos` no JSON e `Mini-Sistemas/Ativos/`).
- Citações chave para usar em slides: "Se não tá escrito, esqueço." / "Sistema escrito = hack vida." / "Juventude 25-30 não pode ser jogada fora." Use `Transcricoes/*` para contextos e trechos completos.
- Dados úteis para gráficos: `CORE/Vida-Deivison.json` (meta_peso_6meses, financas, missoes_quinzenais, rotinas), `ROTINA-VIDA-DEIVISON-2025.md` (detalhes de rotina, compras), `CORE/Deivison.md` (perfil psicológico), `CORE/DeiviTech.md` (portfólio, commits como proxy de esforço).
- Observações importantes: preferir ilustração/vetorial (sem fotos); gerar manifest.json listando arquivos usados por slide; marcar placeholders TO_FILL:<path> quando arquivo ausente.

Crie um Slide Deck de 12 slides (Presenter Slides) com estilo steampunk desenhado: paleta de cobre, sépia, bronze, teal e borgonha; texturas de papel, engrenagens e linhas à mão. Tudo em ilustração (desenho, vetorial, aquarela digital) — sem fotos de pessoas. O Notebook LM deve ler e extrair dados dos arquivos chave do repositório: CORE/Vida-Deivison.json, CORE/Deivison.md, CORE/DeiviTech.md, ROTINA-VIDA-DEIVISON-2025.md, Transcricoes/*, Mini-Sistemas/, Ideias/. Pesquise o repositório para obter citações, datas e métricas reais e use-as nos gráficos.

Diretriz geral: menos futurista, mais calor humano mecânico: engrenagens, tubos, papel, carimbo e tinta. Linguagem visual > texto. Cada slide entregue como arte vetorial + PNG exportável. Salvar arte em Docs/Slides/FinanDEV_Presentation/. Incluir alt-text para acessibilidade.

Slides (breve e direto):

1) Abertura — Pergunta provocadora sobre reinvenção pessoal: "O que você hackearia na sua vida?" Capa ilustrada em sépia com carimbo metálico e tipografia serifada mecânica.

2) Identidade — Mapa orgânico: conecte código, arte, filosofia, política. Use formas tipo papel recortado e engrenagens para representar TDAH, impulsividade, perfeccionismo. Cite trecho curto de CORE/Deivison.md.

3) Workspace — Diagrama radial steampunk: `CORE/` no centro, ramificações para Rotinas, Mini-Sistemas, Ideias, Transcricoes. Render como diagrama estilo blueprint com linhas desenhadas.

4) Rotinas — Timeline espiralada (não-linear) com marcos do road map e gráfico de peso animado. Extraia dados de CORE/Vida-Deivison.json; gerar GIF ou SVG animado.

5) Metodologia — Máquina Escher steampunk: ciclos produtivos e paradoxos. Mostrar loop de entrada (ideia) → protótipo → teste → rotina.

6) Parcerias — Grafo força/constelação com nós como lanternas de bronze (Eventos-FSA, DevSan Open School etc.). Render como force-directed desenhado à tinta.

7) Projetos — Linha do tempo empilhada (stacked area) mostrando evolução de esforço por projeto (DeiviTech, FreelancerDeiviTech, automation-scripts). Use commits/últimas datas como proxy se disponíveis.

8) Filosofia — Painel simbólico: ícones mecânicos para valores, com citações curtas extraídas de Transcricoes/*.

9) Política — Infográfico abstrato: balança/engrenagem combinadas; mostrar 3 pontos de posicionamento com barras coloridas (stacked bar) representando prioridade de ação social.

10) Inovação — Sankey simplificado mostrando fluxo de ideias → experimentos → produtos; destacar Ideias/Financas-Automatizadas.md.

11) Impacto — Radar chart com dimensões: alcance, frequência, profundidade, escala, sustentabilidade; e um pie/donut colorido mostrando alocação financeira com efeito "explosão" para destaque.

12) Convite — Call-to-action com QR-artístico carimbado. Texto curto: "Junte-se à revolução pessoal." Link para Plano-Organizado.md.

Gráficos adicionais solicitados ao Notebook LM:
- Timeline animada do peso (GIF/SVG) com anotações das missões — extrair dados de CORE/Vida-Deivison.json.
- Stacked area para esforço por projeto (usar commits ou datas de pasta como proxy).
- Pie/donut 3D para gastos e poupança (dados de CORE/Vida-Deivison.json). Explodir fatia de sobra para destacar.
- Radar chart para perfil psicológico e energia semanal (sintetizar a partir de CORE/Deivison.md e Transcricoes/).
- Sankey do fluxo de informação do workspace (CORE → Transcricoes → Rotinas → Mini-Sistemas → Saídas).
- Force-directed graph para parcerias e colaborações.
- Heatmap de atividade semanal (commits ou timestamps nas pastas Transcricoes/ e Rotinas/).

Exigências de estilo e formatos:
- Ilustrações (vetorial/line-art + aquarela digital), sem fotos reais.
- Paleta steampunk: bronze (#8B5A2B), cobre (#B87333), sépia (#704214), teal profundo (#0F4C5C), borgonha (#7B2636).
- Tipografia: serif mecânica para títulos, sans legível para notas.
- Exportar: cada slide PNG (3000x1688) + SVG fonte + PDF final.
- Arquivos salvos em Docs/Slides/FinanDEV_Presentation/ com nomes slide01_... slide12_...

Snippet curto (matplotlib/seaborn) para timeline de peso e pie chart:
import json
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

root = Path('CORE')
vida = json.load(open(root/'Vida-Deivison.json', encoding='utf-8'))
# timeline de peso (exemplo)
tracking = vida.get('meta', {}).get('tracking', [])
if tracking:
	df = pd.DataFrame(tracking)
	df['date'] = pd.to_datetime(df['date'])
	df.sort_values('date', inplace=True)
	plt.figure(figsize=(10,4))
	plt.plot(df['date'], df['weight'], marker='o', color='#B87333')
	plt.title('Weight — FinanDEV')
	plt.savefig('Docs/Slides/FinanDEV_Presentation/slide04_weight.png', dpi=150)

# pie chart finanças
data = vida.get('financas', {})
fixos = data.get('gastos_fixos', {})
labels = list(fixos.keys())
values = [fixos[k] for k in labels]
plt.figure()
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['#8B5A2B','#B87333','#0F4C5C'])
plt.savefig('Docs/Slides/FinanDEV_Presentation/slide11_finances.png', dpi=150)

Observação final: peça ao Notebook LM para "ler todo o diretório do repositório FinanDEV" antes de gerar e indicar claramente quais arquivos não foram encontrados (placeholder TO_FILL:<path>). Gerar também um manifest.json com fontes de dados usadas por slide.

Checklist final para o Notebook LM antes de gerar os slides:
- Ler `CORE/` (principais arquivos). Se faltar algo, indicar com TO_FILL:<path>.
- Ler `Transcricoes/*.md` e extrair 3 citações curtas para usar nos slides (identificar fonte e linha).
- Checar `Ambiente-Dev/Celular/Camerologia/README.md` para gerar slide Face-Capture (9-pose grid, pipeline MediaPipe → SVG).
- Para cada gráfico, indicar a fonte exata (arquivo/linha JSON) no `manifest.json`.
- Gerar `manifest.json` com: slides, fontes_usadas, arquivos_encontrados, arquivos_faltantes, imagens_geradas.

Contexto adicional e dados extraídos do workspace (leitura completa):
- Repositórios relacionados: DeiviTech, FreelancerDeiviTech, automation-scripts, Eventos-FSA, finandev, Experimentos, DeiviTech-Monte-Seu-Notebook. Use commits/datas como proxy de esforço e evolução. Se possível gere um gráfico de commits por repo (últimos 6 meses).
- NewJob & storage_state: estado atual - 10 aplicações manuais LinkedIn, 0 automáticas; storage_state.json pendente — sugerir operação no script New-Job (Playwright) para salvar state.
- Camerologia: 5 GCam ports listados, testes com Poco X5; pipeline de Face-Capture (MediaPipe → SVG → animações). Slide específico: comparar antes/depois de fotos tracking (veja `Ambiente-Dev/Celular/Camerologia/`).
- Sleep & Saúde Mental: status ativos desde 08/12; incluir gráfico heatmap semanal de sono (dias x hora) ao lado de radar do impacto mental.
- Bike: quadro quebrado + 2 pneus furados; orcamento conserto ~R$1050; incluir slide com timeline do conserto e custo vs benefício (economia transporte).
- Filantropia: DevSan Open School — incluir slide de impacto social, metas, e CTAs para mentoria/voluntariado.
- Storage/Backup: 38 repositórios; incluir slide: estado do backup (zip + upload Drive) e recomendação de nomeação `Deivison_Core`.

Sugestões de slides variants (adicionais opcionales) — caso precise reduzir ou trocar um dos 12:
- Job Hunting Automation (Playwright): script status, storage_state, commits, e roadmap para automações 1–3 (automatizar 50 vagas/dia)
- Camerologia Testes vs AI Generated: 9-pose grid comparativo e workflow
- Dashboard & KPIs: métricas chave do dia: peso atual, sobra mensal, impulso count, commits semanais
- Security & Privacy: quais dados anonimizados, backups locais vs Drive, guia rápido de limpeza antes de publicar

Snippets extra (matplotlib/plotly/seaborn/plotly express):
# commits per repo (git log proxy)
import subprocess, json, os
from collections import defaultdict
import pandas as pd

repos = ['DeiviTech','FreelancerDeiviTech','automation-scripts','Eventos-FSA','finandev']
counts = defaultdict(int)
for r in repos:
    try:
        out = subprocess.check_output(['git','-C', f'c:/Projetos/FinanDEV/{r}', 'log', '--since=6.months', '--pretty=oneline']).decode('utf-8')
        counts[r] = len(out.splitlines())
    except Exception as e:
        counts[r] = 0

df = pd.DataFrame(list(counts.items()), columns=['repo','commits'])

# stacked area example (effort-over-time per project, requires CSV per repo)
import pandas as pd
import matplotlib.pyplot as plt

# assume df_time format: ['date','DeiviTech','FreelancerDeiviTech',...]
df_time = pd.read_csv('data/commits_by_month.csv', parse_dates=['date'])
df_time.set_index('date').plot.area(colormap='copper')
plt.title('Effort per Project (stacked area)')
plt.savefig('Docs/Slides/FinanDEV_Presentation/slide07_projects_stacked.png', dpi=150)

# heatmap of activity weekly
import glob, pandas as pd, seaborn as sns
files = glob.glob('Transcricoes/*.md')
dates = []
for f in files:
    md = open(f, 'r', encoding='utf-8').read()
    # quick heuristic: find 'data_captacao: YYYY' lines
    import re
    m = re.search(r'data_captacao: ([0-9T\-:\.Z]+)', md)
    if m:
        dates.append(pd.to_datetime(m.group(1)))

s = pd.Series(1, index=pd.DatetimeIndex(dates))
heatmap = s.groupby([s.index.weekday, s.index.hour]).count().unstack(fill_value=0)
sns.heatmap(heatmap, cmap='copper')
plt.title('Atividade: transcrições por dia/hora')
plt.savefig('Docs/Slides/FinanDEV_Presentation/heatmap_activity.png', dpi=150)

# sankey example (plotly)
import plotly.graph_objects as go
nodes = ['CORE','Transcricoes','Rotinas','Mini-Sistemas','Outputs']
source=[0,0,0,0]
target=[1,2,3,4]
value=[50,40,30,20]
fig = go.Figure(go.Sankey(node=dict(label=nodes), link=dict(source=source, target=target, value=value)))
fig.write_image('Docs/Slides/FinanDEV_Presentation/slide10_sankey.png')

***

Pedir ao Notebook LM que gere um `manifest.json` com: slides: [slide01... slide12], fontes_usadas: [], arquivos_encontrados: [], arquivos_faltantes: [] — lista completa de onde os dados vieram.
***
