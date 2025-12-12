```markdown
# Plano-Organizado - FinanDEV

Este plano é fluido e será atualizado por agentes (Grok Code Fast 1 e agentes locais) conforme novas ações forem executadas.
Arquivos-chave e contexto ficam em `CORE/`. Transcrições em `Transcricoes/` permanecem intocadas.

---

## Objetivo

Centralizar identidade, rotina e contexto técnico em `CORE/` para reduzir arquivos soltos na raiz, manter histórico e facilitar ações por agentes.

## Regras de Ouro

- Não mover, editar nem apagar arquivos em `Transcricoes/`.
- `Meu-PC.md` e `Android16.md` NÃO são CORE; são contexto técnico adicional.
- Toda ação que remover arquivos da raiz deve deixar um placeholder apontando para `CORE/` (por ex. `-- moved to CORE/`).
- O Plano é fluido: agentes podem preencher [VAZIOS] com contexto e metas.

---

## CORE (Fonte de Verdade - movidos para `CORE/`)

- `CORE/Deivison.md` — Perfil psicológico completo
- `CORE/DeiviTech.md` — Contexto técnico profundo (stack e repositórios)
- `CORE/ROTINA-VIDA-DEIVISON-2025.md` — Rotina / roadmap de vida
- `CORE/Vida-Deivison.json` — JSON vetorial denso (contexto machine-readable)

Observação: `Meu-PC.md`, `Android16.md` e `PROMPT-MODO-VOZ-*.md` permanecem fora do CORE por serem contexto de ambiente e prompts.

---

## Ações Executadas (até 12/12/2025)

1. CRIADO: `CORE/` (arquivos movidos em cópia para centralizar). Veja `CORE/*`.
2. CRIADO: `Plano-Organizado.md` (este arquivo).
3. `Dashboard/` arquivado em `Backup/Dashboard_removed_2025-12-12/` e placeholder inserido em `Dashboard/`.
4. Root files apontam para `CORE/` (placeholders criados) para reduzir arquivos soltos.
5. `scripts/organize_workspace.py` e `scripts/duplicate_detector.py` criados para automação de organização.
6. `Transcricoes/` backup placeholder criado em `Backup/Transcricoes_ARCHIVE_2025-12-12/`.

---

## Próximos Passos (Fase 1: 0-3 dias)

1. Consolidar `Camerologia/` em `Ambiente-Dev/Celular/Camerologia/` (concluído):
   - Mesclar `Celular/Camerologia/README.md` + `Ambiente-Dev/Celular/Camerologia/README.md` em um só arquivo consolidado.
   - Backup: mover o antigo `Celular/Camerologia/README.md` para `Celular/Camerologia/README_legacy.md` antes de deletar.
2. Criar `CORE/Backup/` com uma cópia ZIP do `Transcricoes/` (somente leitura para agentes), para garantir integridade histórica. (Aguardando criação automatizada)
3. Criar `scripts/organize_workspace.py` com heurísticas de duplicatas e movimento (identificar arquivos soltos no root e sugerir movê-los).

---

## Próximos Passos (Fase 2: 3-14 dias)

1. Automatizar: Hook git (pre-commit) para detectar arquivos soltos na raiz; oferecer mover para `CORE/` ou outra pasta temática.
2. Audit: Rodar script `scripts/duplicate_detector.py` e consolidar duplicatas verificadas (ex.: `Celular/Camerologia` duplicado).
3. Mover `ANALISE-CRONOLOGICA-COMPLETA.md` para `Docs/` e `IDEIAS-FUTURAS.md` para `Ideias/`.

---

## Vãos para Agentes (Edite com cuidado)

- [VAZIO - Agente 1] Sugestão de automação e prioridade
- [VAZIO - Agente 2] Checklist de testes (camerologia / GCam ports)
- [VAZIO - Agente 3] Sugestão de limpeza Temp/ e arquivo arquivamento
- [VAZIO - Agente 4] Plano de rollback em caso de perda de dados

---

## Observações Importantes

- Transcrições são chaves mestres. Não editá-las sob risco de corromper aulas/insights.
- Rotinas e JSON vetorial são a fonte de verdade para agentes; alterações programáticas preferem `CORE/*`.
- Se o workspace ficar desorganizado novamente, agentes usarão `Plano-Organizado.md` como checkpoint e executarão `scripts/organize_workspace.py`.

---

## Histórico de Mudanças

- 2025-12-12: Criado `CORE/` e `Plano-Organizado.md`; criados placeholders de redirecionamento na raiz.

---

## Assinatura

Grok Code Fast 1 (Denominação aceita) — Agente principal para organização FinanDEV

```
