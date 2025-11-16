# 😴 Sistema Backbrowser (Sleep Tracking Automático)

> **Objetivo:**

> **Criado:**

> **Última Atualização:**

> **Integra com:**

> **Status:** 💡 Planejado (não implementado)

---

## 🎯 Conceito

**Problema:** Rastrear sono manualmente é chato e inconsistente  
**Solução:** Inferir sono/acordar via timestamps de atividade digital

**Fontes de dados:**

- Browser history (último acesso)

- Terminal logs (último comando)

- GitHub commits (primeiro/último do dia)

- VS Code timestamps (arquivos abertos/salvos)

---

## 📊 Lógica de Inferência

### Detecção de Dormir

**Último sinal de atividade:**

```python
ultima_atividade = max([
    browser_history[-1].timestamp,  # Última aba fechada

    terminal_log[-1].timestamp,     # Último comando

    github_commits[-1].timestamp,   # Último commit

    vscode_files[-1].timestamp      # Último arquivo salvo

])

hora_dormir = ultima_atividade +

```text

**Tolerância:** 30min após última atividade = provavelmente dormiu

---

### Detecção de Acordar

**Primeiro sinal de atividade:**

```python
primeira_atividade = min([
    browser_history[0].timestamp,   # Primeira aba aberta

    terminal_log[0].timestamp,      # Primeiro comando

    github_commits[0].timestamp,    # Primeiro commit

    vscode_files[0].timestamp       # Primeiro arquivo aberto

])

hora_acordar = primeira_atividade

```text

---

### Cálculo de Horas de Sono

```python
horas_sono = hora_acordar -

qualidade = inferir_qualidade(interrupcoes, continuidade)

```text

**Qualidade inferida:**

- **10/10:** Sono contínuo 7-8h, sem interrupções

- **7-9/10:** 6-7h, sem interrupções

- **4-6/10:** 5-6h ou interrupções detectadas

- **0-3/10:** <5h ou múltiplas interrupções

---

## 🛠️ Implementação Técnica

### Stack Tecnológico

| Componente | Tecnologia |
|------------|------------|
| **Coleta de dados**

| **Browser history**

| **Terminal logs**

| **GitHub commits**

| **VS Code logs**

| **Armazenamento**

| **Visualização** | Matplotlib (gráficos semanais) |

---

### Estrutura de Dados

#### Arquivo `~/.backbrowser/data.json`

```json
{
  "2025-11-16": {
    "ultima_atividade": "2025-11-16T04:32:00",
    "fonte_dormir": "terminal",  // terminal | browser | github | vscode
    "primeira_atividade": "2025-11-16T12:00:00",
    "fonte_acordar": "vscode",
    "horas_sono": 7.5,
    "qualidade_inferida": 8,
    "interrupcoes": [],
    "notas_automaticas": "Madrugada coding (contexto >60%)"
  },
  "2025-11-17": {
    ...
  }
}

```text

---

### Script Python (`backbrowser.py`)

#### Coleta de Dados

```python
import sqlite3
import json
from datetime import datetime, timedelta
from pathlib import Path

def get_last_browser_activity():
    """Lê SQLite do Chrome/Firefox para último timestamp"""
    chrome_db = Path.home() / ".config/google-chrome/Default/History"
    conn = sqlite3.connect(chrome_db)
    cursor = conn.execute(
        "SELECT last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 1"
    )
    timestamp = cursor.fetchone()[0]
    # Converter Chrome timestamp (microseconds desde 1601-01-01)

    return datetime(1601, 1, 1) + timedelta(microseconds=timestamp)

def get_last_terminal_activity():
    """Parse ~/.zsh_history para último comando"""
    history_file = Path.home() / ".zsh_history"
    with open(history_file, 'r', errors='ignore') as f:
        lines = f.readlines()
    last_line = lines[-1]
    # Formato zsh: : timestamp:duration;comando

    timestamp = int(last_line.split(':')[1].split(':')[0])
    return datetime.fromtimestamp(timestamp)

def get_last_github_activity():
    """API GitHub para último commit do dia"""
    import requests
    response = requests.get(
        "https://api.github.com/users/deivisonsantana/events",
        headers={"Authorization": "token YOUR_TOKEN"}
    )
    events = response.json()
    for event in events:
        if event['type'] == 'PushEvent':
            return datetime.fromisoformat(event['created_at'])
    return None

def get_last_vscode_activity():
    """Timestamp de últimos arquivos modificados no VS Code"""
    logs_dir = Path.home() / ".config/Code -

    files = sorted(logs_dir.rglob("*.log"), key=lambda p: p.stat().st_mtime)
    if files:
        return datetime.fromtimestamp(files[-1].stat().st_mtime)
    return None

def detect_sleep_time():
    """Detecta horário de dormir (última atividade)"""
    activities = [
        ("browser", get_last_browser_activity()),
        ("terminal", get_last_terminal_activity()),
        ("github", get_last_github_activity()),
        ("vscode", get_last_vscode_activity())
    ]
    # Remove None values

    activities = [(src, ts) for src, ts in activities if ts]
    # Pega a última atividade

    last_activity = max(activities, key=lambda x: x[1])
    return {
        "timestamp": last_activity[1] + timedelta(minutes=30),  # +30min tolerância

        "source": last_activity[0]
    }

def detect_wake_time():
    """Detecta horário de acordar (primeira atividade do dia)"""
    # Similar ao sleep, mas pega mínimo do dia atual

    today = datetime.now().date()
    activities = [
        ("browser", get_first_browser_activity_today(today)),
        ("terminal", get_first_terminal_activity_today(today)),
        ("github", get_first_github_activity_today(today)),
        ("vscode", get_first_vscode_activity_today(today))
    ]
    activities = [(src, ts) for src, ts in activities if ts]
    if not activities:
        return None
    first_activity = min(activities, key=lambda x: x[1])
    return {
        "timestamp": first_activity[1],
        "source": first_activity[0]
    }

def calculate_sleep_quality(hours, interruptions):
    """Calcula qualidade do sono (0-10)"""
    base_quality = 10
    # Penaliza se <6h ou >9h

    if hours < 6:
        base_quality -= (6 -

    elif hours > 9:
        base_quality -= (hours -

    # Penaliza interrupções

    base_quality -= len(interruptions) *

    return max(0, min(10, base_quality))

def save_sleep_data(date, data):
    """Salva dados em JSON"""
    data_file = Path.home() / ".backbrowser/data.json"
    data_file.parent.mkdir(exist_ok=True)
    
    if data_file.exists():
        with open(data_file, 'r') as f:
            all_data = json.load(f)
    else:
        all_data = {}
    
    all_data[str(date)] = data
    
    with open(data_file, 'w') as f:
        json.dump(all_data, f, indent=2, default=str)

# Execução principal (cron job diário)

if __name__ == "__main__":
    sleep_info = detect_sleep_time()
    wake_info = detect_wake_time()
    
    if sleep_info and wake_info:
        hours = (wake_info['timestamp'] -

        quality = calculate_sleep_quality(hours, interruptions=[])
        
        sleep_data = {
            "ultima_atividade": sleep_info['timestamp'],
            "fonte_dormir": sleep_info['source'],
            "primeira_atividade": wake_info['timestamp'],
            "fonte_acordar": wake_info['source'],
            "horas_sono": round(hours, 1),
            "qualidade_inferida": round(quality, 1),
            "interrupcoes": [],  # Detectar no futuro

            "notas_automaticas": ""
        }
        
        save_sleep_data(datetime.now().date(), sleep_data)
        print(f"✅ Sono registrado: {hours:.1f}h (qualidade {quality}/10)")

```text

---

### Cron Job (Execução Diária)

#### Adicionar em `crontab -e`:

```bash

# Backbrowser - Sleep tracking automático

0 14 *

```text

**Horário:** 14:00 (certeza de que acordou e tem dados do dia)

---

## 📈 Visualização

### Gráfico Semanal (`backbrowser-viz.py`)

```python
import matplotlib.pyplot as plt
import json
from datetime import datetime, timedelta
from pathlib import Path

def plot_weekly_sleep():
    """Gera gráfico de sono da última semana"""
    data_file = Path.home() / ".backbrowser/data.json"
    with open(data_file, 'r') as f:
        all_data = json.load(f)
    
    # Últimos 7 dias

    today = datetime.now().date()
    week = [str(today -

    
    horas = [all_data.get(day, {}).get("horas_sono", 0) for day in week]
    qualidade = [all_data.get(day, {}).get("qualidade_inferida", 0) for day in week]
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Gráfico 1: Horas de sono

    ax1.bar(week, horas, color='steelblue')
    ax1.axhline(y=7, color='green', linestyle='--', label='Meta 7h')
    ax1.set_ylabel('Horas')
    ax1.set_title('Horas de Sono -

    ax1.legend()
    
    # Gráfico 2: Qualidade

    ax2.plot(week, qualidade, marker='o', color='orange', linewidth=2)
    ax2.axhline(y=7, color='green', linestyle='--', label='Qualidade Boa (7+)')
    ax2.set_ylabel('Qualidade (0-10)')
    ax2.set_xlabel('Data')
    ax2.set_title('Qualidade do Sono')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(Path.home() / ".backbrowser/graphs/semana.png")
    print("✅ Gráfico salvo: ~/.backbrowser/graphs/semana.png")

if __name__ == "__main__":
    plot_weekly_sleep()

```text

**Execução:** Manual ou cron semanal (domingos às 20:00)

---

## 🔗 Integração com SAUDE-MENTAL.md

### Auto-Populate Tabela Semanal

```python
def update_saude_mental_md():
    """Atualiza SAUDE-MENTAL.md com dados do Backbrowser"""
    data_file = Path.home() / ".backbrowser/data.json"
    saude_md = Path.home() / "Projetos/FinanDEV/Mini-Sistemas/SAUDE-MENTAL.md"
    
    with open(data_file, 'r') as f:
        sleep_data = json.load(f)
    
    # Lê MD atual

    with open(saude_md, 'r') as f:
        content = f.read()
    
    # Procura tabela semanal (regex)

    import re
    table_pattern = r'(\| \d{2}  \|.*\|)'
    
    for date, data in sleep_data.items():
        day = datetime.fromisoformat(date).strftime('%d')
        sono = f"{data['horas_sono']}h"
        qualidade = f"{data['qualidade_inferida']}/10"
        
        # Atualiza linha da tabela

        new_row = f"| {day}  | {sono}  | {qualidade}  |         |             |          |  |"
        content = re.sub(
            rf'\| {day}  \|.*\|',
            new_row,
            content
        )
    
    # Salva MD atualizado

    with open(saude_md, 'w') as f:
        f.write(content)
    
    print("✅ SAUDE-MENTAL.md atualizado com dados do Backbrowser")

```text

**Execução:** Cron semanal após gerar gráfico

---

## 🧪 Detecção de Interrupções (Futuro)

### Identificar Acordadas Noturnas

```python
def detect_interruptions(date):
    """Detecta atividades entre dormir e acordar"""
    sleep_time = data[date]['ultima_atividade']
    wake_time = data[date]['primeira_atividade']
    
    # Busca atividades no meio

    interruptions = []
    for activity in all_activities:
        if sleep_time < activity.timestamp < wake_time:
            interruptions.append({
                "hora": activity.timestamp,
                "tipo": activity.source,  # browser, terminal, etc.

                "duracao": "5min"  # Estimar

            })
    
    return interruptions

```text

**Impacto na qualidade:**

- Cada interrupção = -1.5 pontos

- Interrupção >30min = -3 pontos

---

## 📊 Estatísticas Semanais

### Output Automático (`~/.backbrowser/stats.md`)

```markdown

## Semana 16-22/11/2025

**Média de sono:** 6.8h/noite  
**Qualidade média:** 7.2/10  
**Melhor noite:** 17/11 (8.5h, 9/10)  
**Pior noite:** 16/11 (5h, 4/10)  
**Interrupções:** 3 (média 0.4/noite)

**Padrões detectados:**

- 🌙 Madrugadas coding: 16/11, 19/11 (sono <6h)

- ☀️ Acordadas cedo: 18/11, 20/11 (antes 10:00)

- 💤 Sono longo: 21/11 (9h, recuperação?)

**Recomendações:**

- Reduzir madrugadas coding para max 2/semana

-

```text

---

## 🎯 Metas do Sistema

### Curto Prazo (1 mês)

- [ ] Script Python funcional (`backbrowser.py`)

- [ ] Cron job configurado

- [ ] Integração com SAUDE-MENTAL.md

### Médio Prazo (3 meses)

- [ ] Detecção de interrupções

- [ ] Gráficos automáticos semanais

- [ ] Alertas (sono <6h por 3 dias)

### Longo Prazo (6 meses)

- [ ] ML para prever qualidade sono (contexto trabalho, madrugadas, etc.)

- [ ] Dashboard web interativo

- [ ] Correlações: sono vs. produtividade (commits), sono vs. humor

---

## 🔒 Privacidade

**Dados sensíveis:**

- Browser history (apenas timestamps, não URLs)

- Terminal logs (apenas timestamps, não comandos completos)

- Tudo local (`~/.backbrowser/`), não em repo público

**Compartilhamento:**

- Estatísticas agregadas OK (médias semanais)

- Dados brutos NÃO (privacidade total)

---

## 📝 Notas de Implementação

**Desafios:**

- **Multi-dispositivo:** Celular não rastreado (só PC)

- **Tolerância:** 30min pode não ser suficiente (ajustar?)

- **Falsos positivos:** Deixar PC ligado sem usar (detectar inatividade real)

**Soluções futuras:**

- Integrar logs Android (Termux, browser mobile)

- Sensor de movimento (webcam?) para confirmar presença

- Machine learning para aprender padrões individuais

---

*Sistema experimental | Alta automação | Zero input manual* 😴
