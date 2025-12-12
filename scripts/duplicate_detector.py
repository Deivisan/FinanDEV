#!/usr/bin/env python3
"""
duplicate_detector.py
Find duplicate-named directories or similar files (e.g., Camerologia in multiple locations)
"""
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]

def dir_occurrences():
    occurrences = defaultdict(list)
    for p in ROOT.rglob('*'):
        if p.is_dir():
            occurrences[p.name].append(str(p))
    return {k: v for k, v in occurrences.items() if len(v) > 1}

if __name__ == '__main__':
    dup = dir_occurrences()
    if not dup:
        print('No duplicate directory names found.')
    else:
        print('Duplicate directories:')
        for name, paths in dup.items():
            print(f'- {name}:')
            for p in paths:
                print(f'  - {p}')
