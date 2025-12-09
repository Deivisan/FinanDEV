// =============================================================================
// Scrape Inteligente - Contorna Cloudflare + Captura Completa
// =============================================================================
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const GROK_LINK = process.argv[2] || 'https://grok.com/share/c2hhcmQtMg_79a4bade-ac65-4501-ad78-df8838368520';
const OUTPUT_DIR = path.join(__dirname, '..', 'Transcricoes');

// =============================================================================
// ESTRATÉGIAS ANTI-CLOUDFLARE
// =============================================================================

async function esperarCloudflarePassar(page) {
  console.log('🛡️ Detectado Cloudflare, aguardando...');
  
  // Espera até 30s pelo challenge passar
  try {
    await page.waitForFunction(() => {
      const body = document.body.innerText;
      return !body.includes('Verify you are human') && 
             !body.includes('Cloudflare') &&
             body.length > 500; // Conteúdo real carregado
    }, { timeout: 30000 });
    
    console.log('✅ Cloudflare passou!');
    return true;
  } catch (e) {
    console.log('⚠️ Cloudflare não passou automaticamente');
    return false;
  }
}

async function scrollParaBaixo(page) {
  console.log('📜 Scrolling para carregar conversa completa...');
  
  let alturaAnterior = 0;
  let tentativas = 0;
  const maxTentativas = 10;
  
  while (tentativas < maxTentativas) {
    // Scroll até o final
    await page.evaluate(() => {
      window.scrollTo(0, document.body.scrollHeight);
    });
    
    // Aguarda carregar mais conteúdo
    await page.waitForTimeout(1500);
    
    // Verifica se carregou mais
    const alturaAtual = await page.evaluate(() => document.body.scrollHeight);
    
    if (alturaAtual === alturaAnterior) {
      console.log(`✅ Scroll completo após ${tentativas + 1} tentativas`);
      break;
    }
    
    alturaAnterior = alturaAtual;
    tentativas++;
    console.log(`   Tentativa ${tentativas}/${maxTentativas} - Altura: ${alturaAtual}px`);
  }
  
  // Scroll de volta pro topo
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(1000);
}

async function extrairMensagens(page) {
  console.log('🔍 Extraindo mensagens estruturadas...');
  
  return await page.evaluate(() => {
    const mensagens = [];
    
    // ESTRATÉGIA 1: Tentar seletores específicos Grok
    const seletoresPossiveis = [
      '[data-testid="message"]',
      '[role="article"]',
      '.message',
      '[class*="message"]',
      '[class*="chat"]',
      'div[class*="Message"]'
    ];
    
    let elementos = null;
    for (const seletor of seletoresPossiveis) {
      elementos = document.querySelectorAll(seletor);
      if (elementos.length > 0) {
        console.log(`Encontrado ${elementos.length} msgs com seletor: ${seletor}`);
        break;
      }
    }
    
    // Se encontrou elementos estruturados
    if (elementos && elementos.length > 0) {
      elementos.forEach((el, idx) => {
        const texto = el.innerText.trim();
        if (texto.length > 0) {
          mensagens.push({
            index: idx,
            texto: texto,
            html: el.innerHTML.substring(0, 200) // Primeiros 200 chars HTML
          });
        }
      });
    }
    
    // ESTRATÉGIA 2: Se não encontrou, pegar body completo e dividir
    if (mensagens.length === 0) {
      const textoCompleto = document.body.innerText;
      
      // Divide por padrões comuns de separação
      const linhas = textoCompleto.split('\n').filter(l => l.trim().length > 0);
      
      linhas.forEach((linha, idx) => {
        if (linha.length > 10) { // Ignora linhas muito curtas
          mensagens.push({
            index: idx,
            texto: linha.trim(),
            html: null
          });
        }
      });
    }
    
    return {
      mensagens: mensagens,
      totalCaracteres: document.body.innerText.length,
      metodo: elementos && elementos.length > 0 ? 'estruturado' : 'texto_completo'
    };
  });
}

// =============================================================================
// MAIN
// =============================================================================

(async () => {
  console.log('🚀 Scrape Inteligente v2.0 - Anti-Cloudflare');
  console.log(`📥 Link: ${GROK_LINK}\n`);
  
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }
  
  const browser = await chromium.launch({
    headless: false, // Mostra navegador para debug
    args: [
      '--disable-blink-features=AutomationControlled', // Esconde automação
      '--no-sandbox',
      '--disable-gpu'
    ]
  });
  
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    viewport: { width: 1920, height: 1080 },
    locale: 'pt-BR',
    timezoneId: 'America/Sao_Paulo'
  });
  
  // Remove sinais de automação
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => false });
    window.chrome = { runtime: {} };
  });
  
  const page = await context.newPage();
  
  console.log('📡 Carregando página...');
  await page.goto(GROK_LINK, { 
    waitUntil: 'domcontentloaded',
    timeout: 60000 
  });
  
  // Aguarda inicial
  await page.waitForTimeout(5000);
  
  // Verifica Cloudflare
  const temCloudflare = await page.evaluate(() => {
    return document.body.innerText.includes('Verify you are human') ||
           document.body.innerText.includes('Cloudflare');
  });
  
  if (temCloudflare) {
    const passou = await esperarCloudflarePassar(page);
    if (!passou) {
      console.log('❌ Cloudflare bloqueou. Tente:');
      console.log('   1. Abrir o link manualmente no navegador');
      console.log('   2. Resolver o captcha');
      console.log('   3. Copiar cookies/sessão');
      await browser.close();
      return;
    }
  }
  
  // Scroll completo para carregar tudo
  await scrollParaBaixo(page);
  
  // Extrai mensagens
  const resultado = await extrairMensagens(page);
  
  console.log(`\n📊 Resultado:`);
  console.log(`   Método: ${resultado.metodo}`);
  console.log(`   Mensagens: ${resultado.mensagens.length}`);
  console.log(`   Caracteres: ${resultado.totalCaracteres}`);
  
  // Salva RAW completo
  const textoCompleto = await page.innerText('body');
  const uuid = GROK_LINK.split('_').pop()?.substring(0, 8) || 'unknown';
  const timestamp = new Date().toISOString().split('T')[0];
  
  const arquivoRaw = path.join(OUTPUT_DIR, `${timestamp}_${uuid}_raw.txt`);
  fs.writeFileSync(arquivoRaw, textoCompleto, 'utf-8');
  
  // Salva JSON estruturado
  const arquivoJson = path.join(OUTPUT_DIR, `${timestamp}_${uuid}_estruturado.json`);
  fs.writeFileSync(arquivoJson, JSON.stringify({
    metadata: {
      link: GROK_LINK,
      uuid: uuid,
      captadoEm: new Date().toISOString(),
      metodo: resultado.metodo,
      totalMensagens: resultado.mensagens.length,
      totalCaracteres: resultado.totalCaracteres
    },
    mensagens: resultado.mensagens
  }, null, 2), 'utf-8');
  
  console.log(`\n✅ Arquivos salvos:`);
  console.log(`   RAW: ${arquivoRaw}`);
  console.log(`   JSON: ${arquivoJson}`);
  console.log(`   Tamanho: ${(textoCompleto.length / 1024).toFixed(2)} KB`);
  
  console.log('\n⏸️ Navegador permanece aberto para inspeção.');
  console.log('   Pressione Ctrl+C para fechar.\n');
  
  // Mantém aberto para debug
  await new Promise(() => {});
  
})();
