// =============================================================================
// Scrape v3.0 - Markdown Estruturado + Metadados Inteligentes
// =============================================================================
// Autor: Deivison Santana + DevSan (Claude Sonnet 4.5)
// Data: 02/NOV/2025
// Metodologia: v3.0 (diferenciação falantes, naming dinâmico, metadados DOM)
// =============================================================================

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// ============================================================================
// CONFIGURAÇÃO
// ============================================================================

const GROK_LINK = process.argv[2] || 'https://grok.com/share/c2hhcmQtMg%3D%3D_c825f0bd-a6ba-47a1-803f-92743614a8a9';
const OUTPUT_DIR = path.join(__dirname, '..', 'Transcricoes');

// ============================================================================
// FUNÇÕES AUXILIARES
// ============================================================================

/**
 * Detecta dispositivo baseado User-Agent
 */
function detectarDispositivo(userAgent) {
  if (/iphone|ipad/i.test(userAgent)) return 'Mobile iOS';
  if (/android/i.test(userAgent)) return 'Mobile Android';
  if (/mobile/i.test(userAgent)) return 'Mobile (genérico)';
  if (/linux/i.test(userAgent)) return 'Desktop Linux';
  if (/windows/i.test(userAgent)) return 'Desktop Windows';
  if (/mac/i.test(userAgent)) return 'Desktop macOS';
  return 'Desconhecido';
}

/**
 * Gera nome arquivo inteligente: [DATA]_[TOPICO]_[DIF].md
 */
function gerarNomeArquivo(palavrasChave) {
  const data = new Date().toISOString().split('T')[0].replace(/-/g, ''); // 20251102
  const topico = palavrasChave.slice(0, 3).join('-').toLowerCase()
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Remove acentos
    .replace(/[^a-z0-9-]/g, ''); // Remove especiais
  
  // Verifica duplicatas
  let nomeBase = `${data}_${topico}`;
  let contador = 1;
  let nomeFinal = `${nomeBase}.md`;
  
  while (fs.existsSync(path.join(OUTPUT_DIR, nomeFinal))) {
    contador++;
    nomeFinal = `${nomeBase}_v${contador}.md`;
  }
  
  return nomeFinal;
}

/**
 * Extrai palavras-chave básicas do texto (top 5 palavras mais comuns)
 */
function extrairPalavrasChave(texto) {
  const stopwords = ['o', 'a', 'de', 'da', 'do', 'e', 'que', 'para', 'com', 'não', 'uma', 'um'];
  const palavras = texto.toLowerCase()
    .replace(/[^\w\sçãõáéíóú]/g, '')
    .split(/\s+/)
    .filter(p => p.length > 3 && !stopwords.includes(p));
  
  // Conta frequência
  const frequencia = {};
  palavras.forEach(p => frequencia[p] = (frequencia[p] || 0) + 1);
  
  // Top 5
  return Object.entries(frequencia)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([palavra]) => palavra);
}

/**
 * Formata mensagem Markdown estruturada
 */
function formatarMensagem(msg, idx) {
  const emoji = msg.autor === 'Deivison' ? '🧑' : '🤖';
  const contexto = [];
  
  if (msg.ehPergunta) contexto.push('Pergunta');
  if (msg.ehCorrecao) contexto.push('Correção');
  if (msg.temEmocao) contexto.push('Ênfase emocional');
  
  const contextoStr = contexto.length > 0 ? `\n**Contexto:** ${contexto.join(', ')}` : '';
  
  return `### ${emoji} ${msg.autor} [msg ${idx + 1}]

> ${msg.texto.replace(/\n/g, '\n> ')}
${contextoStr}

---
`;
}

// ============================================================================
// SCRAPE PRINCIPAL
// ============================================================================

(async () => {
  console.log('🚀 Scrape v3.0 - Markdown Estruturado Iniciado');
  console.log(`📥 Link: ${GROK_LINK}\n`);
  
  // Cria pasta Transcricoes/ se não existir
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }
  
  const browser = await chromium.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-gpu']
  });
  
  const page = await browser.newPage();
  const userAgent = await page.evaluate(() => navigator.userAgent);
  
  await page.setExtraHTTPHeaders({
    'User-Agent': userAgent
  });
  
  console.log('📡 Carregando página...');
  await page.goto(GROK_LINK, { timeout: 30000 }); // SEM waitUntil - mais rápido
  
  console.log('⏳ Aguardando 8s para conteúdo dinâmico...');
  await page.waitForTimeout(8000);
  
  // ============================================================================
  // EXTRAÇÃO METADADOS
  // ============================================================================
  
  console.log('🔍 Extraindo conteúdo completo...');
  
  // ESTRATÉGIA 1: innerText body completo (funciona sempre)
  const textoCompleto = await page.innerText('body');
  
  console.log(`✅ ${textoCompleto.length} caracteres captados`);
  
  // Salvar RAW primeiro (backup)
  const arquivoRaw = path.join(OUTPUT_DIR, `${metadados.uuid}_raw.txt`);
  fs.writeFileSync(arquivoRaw, textoCompleto, 'utf-8');
  console.log(`💾 Backup raw: ${arquivoRaw}`);
  
  // ============================================================================
  // ANÁLISE CONTEXTUAL
  // ============================================================================
  
  const textoCompleto = mensagens.map(m => m.texto).join(' ');
  const palavrasChave = extrairPalavrasChave(textoCompleto);
  
  console.log(`📊 Palavras-chave: ${palavrasChave.join(', ')}`);
  
  // ============================================================================
  // GERAÇÃO MARKDOWN
  // ============================================================================
  
  const nomeArquivo = gerarNomeArquivo(palavrasChave);
  console.log(`📝 Arquivo: ${nomeArquivo}`);
  
  let markdown = `---
data_captacao: ${metadados.captadoEm}
data_criacao_arquivo: ${new Date().toISOString()}
fonte: Grok (${metadados.linkOriginal})
uuid: ${metadados.uuid}
dispositivo: ${metadados.dispositivo}
duracao_estimada: ${metadados.duracaoEstimada}
user_agent: ${metadados.userAgent}
palavras_chave: ${palavrasChave.join(', ')}
participantes:
  - Deivison Santana
  - Grok (xAI)
total_mensagens: ${mensagens.length}
status: ✅ Transcrita estruturada v3.0
---

# 💬 Conversa Grok - ${palavrasChave[0] || 'geral'}

> **Captação:** ${new Date(metadados.captadoEm).toLocaleString('pt-BR')}  
> **Dispositivo:** ${metadados.dispositivo}  
> **Duração estimada:** ${metadados.duracaoEstimada}

---

## 📝 Transcrição

`;
  
  mensagens.forEach((msg, idx) => {
    markdown += formatarMensagem(msg, idx);
  });
  
  // Seção análise contextual
  const correcoes = mensagens.filter(m => m.ehCorrecao);
  const perguntas = mensagens.filter(m => m.ehPergunta);
  const emocoes = mensagens.filter(m => m.temEmocao);
  
  markdown += `\n---

## 📊 Análise Conversacional

### Estatísticas

- **Total mensagens:** ${mensagens.length}
- **Perguntas:** ${perguntas.length}
- **Correções detectadas:** ${correcoes.length}
- **Mensagens com ênfase:** ${emocoes.length}

### Palavras-Chave Top 5

${palavrasChave.map((p, i) => `${i + 1}. **${p}**`).join('\n')}

### Metadados Técnicos

- **UUID:** \`${metadados.uuid}\`
- **Link original:** [Grok Share](${metadados.linkOriginal})
- **User-Agent:** \`${metadados.userAgent}\`
- **Dispositivo:** ${metadados.dispositivo}

---

*Transcrito automaticamente por Scrape v3.0 - Metodologia Markdown Estruturado*
`;
  
  // Salva arquivo
  const caminhoCompleto = path.join(OUTPUT_DIR, nomeArquivo);
  fs.writeFileSync(caminhoCompleto, markdown, 'utf-8');
  
  console.log(`\n✅ Transcrição salva: ${caminhoCompleto}`);
  console.log(`📄 Tamanho: ${(markdown.length / 1024).toFixed(2)} KB`);
  
  await browser.close();
  
  console.log('\n🎉 Scrape v3.0 concluído com sucesso!');
})();
