#!/usr/bin/env python3
"""
🔧 Fix Transcrições - Corrige formato User/Assistant

Problema: Todas mensagens aparecem como "### 👤 Deivison"
Solução: Alterna automaticamente User → Grok baseado em padrões

Uso: python3 fix-transcricoes.py
"""

import re
from pathlib import Path

# Diretório transcrições
TRANSCRICOES_DIR = Path(__file__).parent.parent / "Transcricoes"

def detect_speaker(text: str, index: int) -> str:
    """
    Detecta quem está falando baseado em padrões de texto
    
    Patterns Deivison (User):
    - Textos curtos (< 200 chars)
    - Começa com perguntas: "vamos", "pode", "quero"
    - Referências próprias: "meu", "eu", "vou"
    - Comandos: "crie", "faça", "mostre"
    
    Patterns Grok (Assistant):
    - Textos longos (> 200 chars)
    - Começa com confirmações: "Beleza", "Certo", "Entendi"
    - Explicações técnicas: "markdown", "commit", "repo"
    - Listas/estruturas: começa com "- ", "1. "
    """
    text_clean = text.strip()
    
    # Patterns Grok (respostas longas)
    grok_patterns = [
        r'^(Beleza|Certo|Entendi|Sim|É|Perfeito|Tá|Ah)',
        r'^(Pensado por|Analisando|Pesquisei|Criei|Commitei)',
        r'(```|markdown|python|javascript)',  # Code blocks
        r'^\s*[-\*]\s',  # Listas
        r'^\s*\d+\.\s',  # Listas numeradas
        len(text_clean) > 300,  # Textos longos
    ]
    
    # Patterns Deivison (perguntas/comandos curtos)
    user_patterns = [
        r'^(vamos|pode|quero|preciso|me|meu|eu\s)',
        r'^(crie|faça|mostre|liste|ajude|explique)',
        r'\?$',  # Termina com pergunta
        len(text_clean) < 150,  # Textos curtos
    ]
    
    # Checka Grok patterns
    for pattern in grok_patterns[:4]:  # Regex patterns
        if re.search(pattern, text_clean, re.IGNORECASE):
            return "Grok"
    if grok_patterns[4]:  # Length check
        return "Grok"
    
    # Checka User patterns
    for pattern in user_patterns[:3]:  # Regex patterns
        if re.search(pattern, text_clean, re.IGNORECASE):
            return "Deivison"
    if user_patterns[3]:  # Length check
        return "Deivison"
    
    # Default: alterna baseado em índice (User/Grok/User/Grok...)
    return "Deivison" if index % 2 == 0 else "Grok"


def fix_transcricao(file_path: Path) -> tuple[int, int]:
    """
    Corrige uma transcrição alternando User/Grok
    
    LÓGICA NOVA:
    - Divide por separador "---"
    - Mensagens ímpares (0, 2, 4...) = User (Deivison)
    - Mensagens pares (1, 3, 5...) = Assistant (Grok)
    
    Returns: (total_messages, grok_messages_fixed)
    """
    print(f"\n📝 Processando: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split por "---" (separador mensagens)
    parts = re.split(r'\n---\n', content)
    
    if len(parts) < 2:
        print("⚠️  Arquivo sem formato esperado (sem separadores ---)")
        return 0, 0
    
    # Header (antes da primeira mensagem)
    header = parts[0]
    
    # Rebuild com alternância correta
    fixed_parts = [header]
    message_count = 0
    grok_count = 0
    
    for i, part in enumerate(parts[1:], start=0):
        # Determina speaker baseado em posição
        is_grok = (i % 2 == 1)  # Ímpar = Grok
        
        # Replace marker atual
        if is_grok:
            fixed_part = re.sub(
                r'### [👤🤖] (?:Deivison|Grok)\s*\n',
                '### 🤖 Grok\n',
                part,
                count=1
            )
            grok_count += 1
        else:
            fixed_part = re.sub(
                r'### [👤🤖] (?:Deivison|Grok)\s*\n',
                '### 👤 Deivison\n',
                part,
                count=1
            )
        
        fixed_parts.append(fixed_part)
        message_count += 1
    
    # Rejoin com separadores
    fixed_content = '\n---\n'.join(fixed_parts)
    
    # Salva arquivo corrigido
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"✅ {message_count} mensagens processadas ({grok_count} Grok corrigidas)")
    return message_count, grok_count


def main():
    """Corrige todas transcrições .md"""
    print("🔧 Fix Transcrições - Iniciando...")
    
    md_files = list(TRANSCRICOES_DIR.glob("*.md"))
    
    if not md_files:
        print("❌ Nenhum arquivo .md encontrado em Transcricoes/")
        return
    
    print(f"📂 Encontrados {len(md_files)} arquivos:")
    
    total_msgs = 0
    total_grok = 0
    
    for md_file in md_files:
        msgs, grok = fix_transcricao(md_file)
        total_msgs += msgs
        total_grok += grok
    
    print(f"\n✅ Concluído!")
    print(f"📊 Total: {total_msgs} mensagens processadas")
    print(f"🤖 Grok: {total_grok} mensagens corrigidas")
    print(f"👤 User: {total_msgs - total_grok} mensagens")


if __name__ == "__main__":
    main()
