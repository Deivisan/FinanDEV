#!/usr/bin/env python3
"""
🔧 Fix Markdown Lint - Corrige erros MD022, MD032, MD031, MD040

Erros frequentes:
- MD022: Headings sem blank lines antes/depois
- MD032: Lists sem blank lines antes/depois  
- MD031: Code blocks sem blank lines
- MD040: Code blocks sem language

Uso: python3 fix-markdown-lint.py
"""

import re
from pathlib import Path
from typing import List

# Diretório raiz
ROOT_DIR = Path(__file__).parent.parent

def fix_md022(content: str) -> str:
    """
    MD022: Headings should be surrounded by blank lines
    
    Adiciona linha em branco antes e depois de headings
    """
    # Adiciona blank line ANTES de headings (se não tiver)
    content = re.sub(
        r'([^\n])\n(#{1,6} )',
        r'\1\n\n\2',
        content
    )
    
    # Adiciona blank line DEPOIS de headings (se não tiver)
    content = re.sub(
        r'(#{1,6} [^\n]+)\n([^\n#])',
        r'\1\n\n\2',
        content
    )
    
    return content


def fix_md032(content: str) -> str:
    """
    MD032: Lists should be surrounded by blank lines
    
    Adiciona linha em branco antes e depois de listas
    """
    # Blank line ANTES de lista (-, *, +, ou 1.)
    content = re.sub(
        r'([^\n])\n([-\*\+]|\d+\.) ',
        r'\1\n\n\2 ',
        content
    )
    
    # Blank line DEPOIS de lista (próxima linha não é lista)
    content = re.sub(
        r'([-\*\+]|\d+\.) [^\n]+\n([^-\*\+\d\n#])',
        r'\1\n\n\2',
        content
    )
    
    return content


def fix_md031_md040(content: str) -> str:
    """
    MD031: Code blocks should be surrounded by blank lines
    MD040: Code blocks should have language specified
    
    Adiciona blank lines e sugere language
    """
    # Fix code blocks sem language (``` → ```text)
    content = re.sub(
        r'\n```\n',
        r'\n```text\n',
        content
    )
    
    # Blank line ANTES de code block
    content = re.sub(
        r'([^\n])\n(```)',
        r'\1\n\n\2',
        content
    )
    
    # Blank line DEPOIS de code block
    content = re.sub(
        r'(```)\n([^\n`])',
        r'\1\n\n\2',
        content
    )
    
    return content


def fix_markdown_file(file_path: Path) -> int:
    """
    Corrige um arquivo markdown
    
    Returns: número de fixes aplicados
    """
    print(f"\n📝 Processando: {file_path.relative_to(ROOT_DIR)}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        original = f.read()
    
    content = original
    
    # Aplica fixes em sequência
    content = fix_md022(content)
    content = fix_md032(content)
    content = fix_md031_md040(content)
    
    # Remove múltiplas blank lines consecutivas (>2 → 2)
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    # Conta mudanças
    changes = len([i for i, (a, b) in enumerate(zip(original, content)) if a != b])
    
    if changes > 0:
        # Salva arquivo corrigido
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {changes} caracteres corrigidos")
    else:
        print("⏭️  Nenhuma correção necessária")
    
    return changes


def main():
    """Corrige todos markdowns do repo"""
    print("🔧 Fix Markdown Lint - Iniciando...")
    
    # Find all .md files (exceto node_modules, .git)
    md_files = [
        f for f in ROOT_DIR.rglob("*.md")
        if not any(part.startswith('.') or part == 'node_modules' for part in f.parts)
    ]
    
    if not md_files:
        print("❌ Nenhum arquivo .md encontrado")
        return
    
    print(f"📂 Encontrados {len(md_files)} arquivos markdown")
    
    total_changes = 0
    files_changed = 0
    
    for md_file in md_files:
        changes = fix_markdown_file(md_file)
        if changes > 0:
            files_changed += 1
            total_changes += changes
    
    print("\n✅ Concluído!")
    print(f"📊 {files_changed}/{len(md_files)} arquivos corrigidos")
    print(f"✏️  {total_changes} caracteres modificados no total")


if __name__ == "__main__":
    main()
