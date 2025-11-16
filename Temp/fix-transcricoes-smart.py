#!/usr/bin/env python3
"""
🔧 Fix Transcrições SMART - Detecta speaker por padrão linguístico

Problema: Script anterior alternava cegamente (par/ímpar)
Solução: Analisa CONTEÚDO para detectar Deivison vs Grok

Uso: python3 fix-transcricoes-smart.py
"""

import re
from pathlib import Path

# Diretório transcrições
TRANSCRICOES_DIR = Path(__file__).parent.parent / "Transcricoes"

def detect_speaker_smart(text: str) -> str:
    """
    Detecta quem está falando por PADRÕES LINGUÍSTICOS
    
    DEIVISON (User) - Padrões:
    - Perguntas/comandos: "vamos", "pode fazer", "preciso que", "quero"
    - Referências próprias: "meu repo", "minha energia", "eu acho"
    - Comandos diretos: "crie", "faça", "mostre", "corrija"
    - Textos curtos (< 200 chars geralmente)
    - Confirmações: "pronto", "beleza", "entendi"
    - Coloquial: "né?", "entendeu?", "tá", "vamos supor"
    
    GROK (Assistant) - Padrões:
    - Confirmações longas: "Beleza, Deivison", "Entendi perfeitamente"
    - Explicações técnicas: "markdown", "commit", "JSON", "vetorial"
    - Listas/estruturas: começa com "- ", "1. ", "```"
    - Textos longos (> 300 chars)
    - Fala em 3ª pessoa sobre Deivison: "você mencionou", "seu agente"
    - Busca web: "vasculhei", "pesquisei", "internalizei"
    - Tutoriais: "Pra fazer isso", "O ideal é", "Dá pra"
    """
    text_clean = text.strip()
    text_lower = text_clean.lower()
    
    # Score system (positivo = Grok, negativo = Deivison)
    score = 0
    
    # PADRÕES GROK (+ score)
    grok_indicators = [
        (r'^(beleza|certo|entendi|sim|perfeito),?\s+(deivison|d\w+)', 5),  # "Beleza, Deivison"
        (r'(vasculhei|internalizei|pesquisei|analisei)', 4),
        (r'(markdown|json|commit|vetorial|api|script)', 3),
        (r'^pensado por \d+s', 5),  # "Pensado por 23s"
        (r'^\s*[-\*•]\s', 2),  # Listas
        (r'^\s*\d+\.\s', 2),  # Listas numeradas
        (r'```', 3),  # Code blocks
        (r'(você mencionou|seu agente|seu repo|sua rotina)', 3),
        (r'(pra fazer|o ideal|dá pra|melhor|sugiro)', 2),
    ]
    
    for pattern, weight in grok_indicators:
        if re.search(pattern, text_lower):
            score += weight
    
    # Texto longo = Grok
    if len(text_clean) > 350:
        score += 4
    elif len(text_clean) > 250:
        score += 2
    
    # PADRÕES DEIVISON (- score)
    user_indicators = [
        (r'^(vamos|pode|quero|preciso|me\s|meu\s|eu\s)', -4),
        (r'^(crie|faça|mostre|liste|ajude|explique|corrija)', -5),
        (r'\?$', -3),  # Termina com pergunta
        (r'\b(né\?|entendeu\?|tá\?|vamos supor)', -4),  # Coloquial
        (r'^(pronto|beleza|ótimo|legal)\.?\s*$', -3),  # Confirmações curtas
        (r'(minha energia|meu repo|eu acho|eu tô)', -3),
    ]
    
    for pattern, weight in user_indicators:
        if re.search(pattern, text_lower):
            score += weight  # weight já é negativo
    
    # Texto curto = Deivison
    if len(text_clean) < 100:
        score -= 3
    elif len(text_clean) < 200:
        score -= 1
    
    # Decisão final
    if score > 2:
        return "Grok"
    elif score < -2:
        return "Deivison"
    else:
        # Ambíguo - usa primeira palavra como hint
        first_word = text_clean.split()[0].lower() if text_clean else ""
        if first_word in ["beleza", "entendi", "certo", "sim"]:
            return "Grok"
        else:
            return "Deivison"


def fix_transcricao_smart(file_path: Path) -> tuple[int, int, int]:
    """
    Corrige transcrição com detecção inteligente de speaker
    
    Returns: (total_msgs, deivison_count, grok_count)
    """
    print(f"\n📝 Processando: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split por "---" (separador mensagens)
    parts = re.split(r'\n---\n', content)
    
    if len(parts) < 2:
        print("⚠️  Arquivo sem formato esperado (sem separadores ---)")
        return 0, 0, 0
    
    # Header (antes da primeira mensagem)
    header = parts[0]
    
    # Rebuild com detecção inteligente
    fixed_parts = [header]
    deivison_count = 0
    grok_count = 0
    
    for part in parts[1:]:
        # Extrai texto da mensagem (remove header "### X")
        text_match = re.search(r'### [👤🤖] (?:Deivison|Grok)\s*\n(.+)', part, re.DOTALL)
        if not text_match:
            fixed_parts.append(part)
            continue
        
        message_text = text_match.group(1).strip()
        
        # Detecta speaker por conteúdo
        speaker = detect_speaker_smart(message_text)
        
        # Replace header
        if speaker == "Grok":
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
            deivison_count += 1
        
        fixed_parts.append(fixed_part)
    
    # Rejoin com separadores
    fixed_content = '\n---\n'.join(fixed_parts)
    
    # Salva arquivo corrigido
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    total = deivison_count + grok_count
    print(f"✅ {total} msgs ({deivison_count} Deivison 👤 | {grok_count} Grok 🤖)")
    return total, deivison_count, grok_count


def main():
    """Corrige todas transcrições com detecção inteligente"""
    print("🔧 Fix Transcrições SMART - Iniciando...")
    
    md_files = list(TRANSCRICOES_DIR.glob("*.md"))
    
    if not md_files:
        print("❌ Nenhum arquivo .md encontrado em Transcricoes/")
        return
    
    print(f"📂 Encontrados {len(md_files)} arquivos:")
    
    total_msgs = 0
    total_deivison = 0
    total_grok = 0
    
    for md_file in md_files:
        msgs, deiv, grok = fix_transcricao_smart(md_file)
        total_msgs += msgs
        total_deivison += deiv
        total_grok += grok
    
    print(f"\n✅ Concluído!")
    print(f"📊 Total: {total_msgs} mensagens processadas")
    print(f"👤 Deivison: {total_deivison} mensagens ({total_deivison/total_msgs*100:.1f}%)")
    print(f"🤖 Grok: {total_grok} mensagens ({total_grok/total_msgs*100:.1f}%)")
    
    # Mostra distribuição
    ratio = total_deivison / total_grok if total_grok > 0 else 0
    if 0.8 <= ratio <= 1.2:
        print("✅ Distribuição equilibrada (50/50 esperado)")
    else:
        print(f"⚠️  Distribuição desbalanceada (ratio {ratio:.2f}:1)")


if __name__ == "__main__":
    main()
