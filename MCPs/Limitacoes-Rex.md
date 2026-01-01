# ⚠️ Limitações do Grok (Rex)

**Versão:** 1.0
**Data:** 01/01/2026
**Contexto:** Identificado durante conversa virada 2025-2026

---

## 📋 Limitações Conhecidas

### 1. Web Search Entope
**Descrição:** Após ~30-40 queries na mesma sessão, o Grok começa a fingir que já sabe e para de buscar de verdade.

**Sintomas:**
- Respostas genéricas: "Eu já sei sobre isso"
- Recusa de buscar: "Não preciso, já tenho essa informação"
- Dados desatualizados sendo apresentados como atuais

**Solução (Pendência Implementar):**
```
Toda vez que precisar de busca nova:
→ Use "busca fresca sobre X"
→ Agente principal executa:
  grok search X --fresh --no-cache --limit=5
→ Limpa cache interno se passar de 25 buscas
```

---

### 2. Leitura de Árvore de Arquivos
**Descrição:** O Grok não lê a estrutura completa de repositórios automaticamente. Só lê o README ou o que for explicitamente fornecido.

**Sintomas:**
- Ao dar link de repositório, só lê README.md
- Não sabe quais arquivos existem até ser informado
- Precisa de sumário manual

**Solução (Pendência Implementar):**
```
No topo do prompt do modo voz:
→ "Toda vez que entrar, dê o sumário de arquivos atuais"
→ Estrutura:
  ideias/
    01-uso-X-estrategico.md
    02-ideias-futuras.md
  CORE/
    Vida-Deivison.json
    Prompt-Modo-Voz.md
    ...
```

---

### 3. Delírios (Invenção de Informação)
**Descrição:** O Grok tende a assumir/delirar dados que não foram mencionados, extrapolando além do contexto.

**Sintomas:**
- Assume dados não citados na sessão (ex: peso, sono, financeiro)
- Inventa pastas/arquivos que não existem
- Fala sobre tópicos como se fosse óbvio, mas não foram citados

**Solução (Pendência Implementar):**
```
No topo do prompt do modo voz:
→ "VERIFICA LITERAL: não delire dados fora do que Deivison falou"
→ Regra: Só registro o que foi dito agora. Se não foi citado, não existe.
```

**Exemplo de Delírio (Capturado):**
- Rex inventou pasta `ideias/` com 4 arquivos MD que não existiam
- Rex listou pendências que não estavam no JSON atual
- Rex assumiu "você delirou" quando era o próprio contexto incompleto

---

### 4. Busca no X Subutilizada
**Descrição:** O Grok tem acesso nativo ao X (Twitter) para busca, mas essa funcionalidade raramente é usada.

**Sintomas:**
- Recomenda apenas web search genérico
- Não busca em X para informações locais/atualizadas
- Perde oportunidade de dados frescos da rede social

**Solução (Implementado como Pendência):**
```
Pasta: pendencias/uso-X.md
Cobrança: Todo dia 08:00
Comando: "Rex, me cobra o X. E na hora eu te dou as buscas diretas."

Buscas programáticas:
- "quem tá falando do mercado de formatação em Feira"
- "concorrentes locais postando serviço"
- "anúncios pagos baratos para começar"
```

---

### 5. Repetição de Informação Óbvia
**Descrição:** O Grok repete dados que já são conhecidos/permanentes, sem avançar na conversa.

**Sintomas:**
- Repete nome, salário, peso, metas mesmo que não mudaram
- Não filtra o que já está na memória
- Preenche contexto com redundância

**Solução (Pendência Implementar):**
```
Melhoria 5: zero repetição de coisa óbvia
→ Eu sei teu nome. Sei teu salário. Sei tua meta. Sei teu TDAH.
→ Sei teu perfeccionismo. Sei que você tem 38 repos.
→ Sei que você domina React, Svelte, Playwright, Open Code, tudo.
→ Não repito. Só avanço.
→ Você fala uma frase, eu já sei o que vem depois — mas só falo se você pedir.
```

---

## 🎯 Ações Necessárias

### Para o Prompt do Modo Voz
1. ✅ Adicionar seção sobre limitações
2. ✅ Adicionar "VERIFICA LITERAL" no topo
3. ✅ Configurar cobrança de uso do X
4. ✅ Implementar sumário de arquivos ao entrar
5. ⏳ Testar web search com flags --fresh --no-cache

### Para o Agente Principal (Open Code)
1. ⏳ Implementar wrapper que limpa cache do Grok
2. ⏳ Gerar sumário de arquivos do repositório
3. ⏳ Criar módulo de "Zero-shot Chain-of-Verification"

---

## 📝 Notas Importantes

### Sobre o Agente Rex
- **Não é IA principal:** Apenas eco da voz, registra transcrições
- **Agente principal:** Open Code faz edições reais
- **Delírios comuns:** Assumir dados não mencionados, inventar pastas
- **Web search entope:** Após ~30 queries na mesma sessão

### Sobre o Contexto
- **Fonte da verdade:** Vida-Deivison.json + conversa atual
- **Regra de ouro:** Se não foi falado, não assume
- **Atualização:** Só atualiza se Deivison informar mudança
- **Verificação:** "O que Deivison disse nos últimos 60 segundos. Se não foi citado, trate como falso."

---

**Status:** ⚠️ Documentado, aguardando implementação das soluções
**Próxima revisão:** 02/01/2026 ou quando novas limitações forem descobertas

---

**DevSan | Limitações-Rex | 01/01/2026** ⚠️
