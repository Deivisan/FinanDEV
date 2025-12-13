from pathlib import Path
p=Path('CORE/Vida-Deivison.json')
with p.open('rb') as f:
    b=f.read(256)
print(b[:256])
print('len',len(b))
