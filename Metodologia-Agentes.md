# Metodologia-Agentes.md

## Protocolo DevSan para Orquestração de Workspace com Múltiplos Agentes

### Visão Geral
Este protocolo define como múltiplos agentes de IA (incluindo DevSan e outros) devem operar no workspace FinanDEV, garantindo colaboração eficiente, rastreamento de ações e preservação de contexto para iterações futuras.

### Princípios Fundamentais
1. **Auto-Aprovação Total**: Agentes têm autonomia para executar ações necessárias, seguindo regras de segurança.
2. **Logs Obrigatórios**: Toda ação significativa deve gerar logs detalhados para outros agentes.
3. **Iteração Contextual**: Agentes devem ler logs anteriores antes de agir, mantendo continuidade.
4. **Limite de Tokens**: Considerar limites de tokens em conversas; resumir e priorizar informações críticas.
5. **Multi-Agente**: Suporte a conversações paralelas e agentes especializados (ex: Plan, Flash).

### Estrutura de Logs
Cada agente deve criar/manter logs em formato Markdown no diretório `Logs/`:
- **Nome do Arquivo**: `{data}-{agente}-{tarefa}.md` (ex: `2025-12-13-devsan-atualizacao-prompt.md`)
- **Cabeçalho**: Data, Agente, Tarefa, Status (Iniciado/Concluído/Pendente)
- **Conteúdo Estruturado**:
  - **Ações Executadas**: Lista detalhada de comandos, edições, leituras.
  - **Resultados**: Outputs, erros, insights.
  - **Próximos Passos**: Recomendações para outros agentes.
  - **Contexto Preservado**: Resumos de arquivos lidos, decisões tomadas.

### Fluxo de Operação
1. **Leitura Inicial**: Agente lê logs relevantes e arquivos de contexto (ex: `CORE/`, `Pendencias/`).
2. **Planejamento**: Usar agente "Plan" para outline se necessário.
3. **Execução**: Ações com logs em tempo real.
4. **Checkpoint**: Salvar estado periodicamente.
5. **Finalização**: Gerar log final e notificar outros agentes via comentários em issues/PRs.

### Regras de Segurança
- Backup antes de edições massivas.
- Não deletar sem confirmação.
- Testar mudanças críticas.

### Integração com Ferramentas
- **Memory MCP**: Para contexto entre sessões.
- **Git MCP**: Para commits com mensagens claras.
- **Terminal**: Para execuções, com aliases.
- **Web Search**: Para pesquisa externa.

### Exemplo de Log
```
# 2025-12-13-devsan-atualizacao-prompt.md

## Status: Concluído

### Ações Executadas
- Lido arquivo `Pendencias/PENDENCIAS-ATIVAS-09DEZ2025.md`
- Criado prompt inicial para atualização
- Commitado mudanças

### Resultados
- Prompt estruturado em 5 etapas
- Identificadas 10 pendências principais

### Próximos Passos
- Agente Plan para detalhar etapas
- Iterar com usuário via "continue"
```

Este protocolo será expandido futuramente por Deivison Santana.
