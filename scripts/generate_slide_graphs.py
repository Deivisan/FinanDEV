#!/usr/bin/env python3
import json
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / 'CORE'
OUT = ROOT / 'Docs' / 'Slides' / 'FinanDEV_Presentation'
OUT.mkdir(parents=True, exist_ok=True)

vida_path = CORE / 'Vida-Deivison.json'
if not vida_path.exists():
    print('Vida-Deivison.json not found in CORE/')
    exit(1)

try:
    vida = json.load(open(vida_path, 'r', encoding='utf-8'))
except Exception:
    vida = json.load(open(vida_path, 'r', encoding='latin-1'))


# timeline of weight
tracking = vida.get('meta', {}).get('tracking', []) or vida.get('meta_peso_6meses', {}).get('tracking', [])
if tracking:
    df = pd.DataFrame(tracking)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    elif 'mes' in df.columns:
        df['date'] = pd.to_datetime(df['mes'].str.replace('_', ' '))
    df = df.sort_values('date')
    # normalize weight column names
peso_cols = ['peso', 'weight', 'peso_kg', 'peso_kg', 'peso_kg']
for c in peso_cols:
    if c in df.columns:
        df['peso'] = df[c]
        break
    plt.figure(figsize=(10,4))
    plt.plot(df['date'].astype(str), df['peso'], marker='o', color='#B87333')
    plt.title('Weight — FinanDEV')
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.tight_layout()
    plt.savefig(OUT / 'slide04_weight.png', dpi=150)
    plt.close()
    print('Saved slide04_weight.png')
else:
    print('No tracking data found for weight.')

# pie chart finances (gastos fixos)
fin = vida.get('financas', {})
fixos = fin.get('gastos_fixos', {})
if fixos:
    labels = list(fixos.keys())
    values = [fixos[k] for k in labels]
    plt.figure(figsize=(6,6))
    colors = ['#8B5A2B','#B87333','#0F4C5C','#7B2636']
    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors[:len(labels)], explode=[0.02]*len(labels))
    plt.title('Gastos Fixos — FinanDEV')
    plt.tight_layout()
    plt.savefig(OUT / 'slide11_finances.png', dpi=150)
    plt.close()
    print('Saved slide11_finances.png')
else:
    print('No fixed expenses data found in finanças.')
