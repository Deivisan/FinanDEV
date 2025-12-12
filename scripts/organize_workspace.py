#!/usr/bin/env python3
"""
organize_workspace.py
Simple script to suggest moves for files in repository root and detect candidates to move into CORE or proper folder.

Usage: python scripts/organize_workspace.py
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / 'CORE'
EXCLUDE = {'node_modules', '.git', 'Backup', 'Transcricoes', 'Temp'}

def suggest_moves():
    suggestions = []
    for p in ROOT.iterdir():
        if p.name in EXCLUDE:
            continue
        if p.is_file():
            if p.suffix in {'.md', '.json'} and p.name.lower() not in {f.name.lower() for f in CORE.iterdir()}:
                # suggest moving some known files
                if 'rotina' in p.name.lower() or 'vida' in p.name.lower() or 'deivison' in p.name.lower():
                    suggestions.append({'path': str(p), 'suggested': 'CORE/'})
                elif 'dashboard' in p.name.lower() or 'analise' in p.name.lower():
                    suggestions.append({'path': str(p), 'suggested': 'Docs/'})
                elif 'ideias' in p.name.lower():
                    suggestions.append({'path': str(p), 'suggested': 'Ideias/'})
                else:
                    suggestions.append({'path': str(p), 'suggested': 'Review'})
    return suggestions

if __name__ == '__main__':
    s = suggest_moves()
    print('\nSuggested moves:')
    print(json.dumps(s, indent=2, ensure_ascii=False))
