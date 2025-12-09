// =============================================================================
// Scrape Capture - Versão Simplificada e Funcional
// =============================================================================
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const GROK_LINK = process.argv[2] || 'https://grok.com/share/c2hhcmQtMg_79a4bade-ac65-4501-ad78-df8838368520';
const OUTPUT_DIR = path.join(__dirname, '..', 'Transcricoes');

(async () => {
  console.log('🚀 Iniciando captura Grok...');
  console.log(`📥 Link: ${GROK_LINK}\n`);
  
  // Cria pasta se não existir
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }
  
  const browser = await chromium.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-gpu']
  });
  
  const page = await browser.newPage();
  
  console.log('📡 Carregando página...');
  await page.goto(GROK_LINK, { timeout: 60000 });
  
  console.log('⏳ Aguardando conteúdo carregar (10s)...');
  await page.waitForTimeout(10000);
  
  console.log('🔍 Extraindo conteúdo...');
  const textoCompleto = await page.innerText('body');
  
  console.log(`✅ ${textoCompleto.length} caracteres captados`);
  
  // Extrai UUID do link
  const uuid = GROK_LINK.split('_').pop() || 'unknown';
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-').split('T')[0];
  
  // Salva RAW
  const arquivoRaw = path.join(OUTPUT_DIR, `${timestamp}_${uuid.substring(0, 8)}_raw.txt`);
  fs.writeFileSync(arquivoRaw, textoCompleto, 'utf-8');
  
  console.log(`\n✅ Captura salva: ${arquivoRaw}`);
  console.log(`📄 Tamanho: ${(textoCompleto.length / 1024).toFixed(2)} KB`);
  
  await browser.close();
  
  console.log('\n🎉 Captura concluída!');
  console.log('📋 Próximo passo: Processar conteúdo e estruturar Markdown\n');
  
  // Retorna caminho para processamento
  return arquivoRaw;
})();
