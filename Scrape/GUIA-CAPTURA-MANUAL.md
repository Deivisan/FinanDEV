# 📋 Guia Captura Manual - Grok Share

> **Problema:** Links Grok Share protegidos por Cloudflare (403/captcha)
> **Solução:** Captura manual + processamento automático

---

## 🎯 Método 1: Copiar Texto Direto (Mais Rápido)

### Passo 1: Abrir Link no Navegador
```
https://grok.com/share/c2hhcmQtMg_79a4bade-ac65-4501-ad78-df8838368520
```

### Passo 2: Selecionar Todo Conteúdo
- **Windows:** `Ctrl + A`
- **Mac:** `Cmd + A`

### Passo 3: Copiar
- **Windows:** `Ctrl + C`
- **Mac:** `Cmd + C`

### Passo 4: Colar em Arquivo
Criar arquivo: `Transcricoes/2025-12-09_conversa-manual.txt`

---

## 🤖 Método 2: DevTools Console (Mais Preciso)

### Passo 1: Abrir DevTools
- **Windows:** `F12` ou `Ctrl + Shift + I`
- **Mac:** `Cmd + Option + I`

### Passo 2: Ir para Console

### Passo 3: Executar Script
```javascript
// Extrai todo texto da conversa
const texto = document.body.innerText;
console.log(texto);

// Ou copiar direto para clipboard
copy(document.body.innerText);
```

### Passo 4: Colar Resultado
Criar arquivo: `Transcricoes/2025-12-09_conversa-devtools.txt`

---

## 🔄 Método 3: Extensão Browser (Automático)

### Opção A: SingleFile
1. Instalar: [SingleFile Extension](https://github.com/gildas-lormeau/SingleFile)
2. Abrir link Grok
3. Clicar ícone SingleFile
4. Salvar HTML completo
5. Extrair texto depois

### Opção B: Copy as Markdown
1. Instalar: Copy as Markdown (Chrome/Firefox)
2. Selecionar conversa
3. Botão direito → "Copy as Markdown"
4. Colar em arquivo

---

## 📝 Processamento Automático

Depois de ter o arquivo `.txt` com conteúdo:

```bash
# Processar e estruturar
node Scrape/processar-manual.js Transcricoes/2025-12-09_conversa-manual.txt
```

Isso vai:
- ✅ Detectar speakers (Deivison vs Grok)
- ✅ Estruturar em Markdown
- ✅ Extrair metadados
- ✅ Gerar análise contextual
- ✅ Atualizar workspace dinamicamente

---

## 🚀 Alternativa: Playwright com Login

Se você tiver conta Grok logada:

```javascript
// scrape-com-login.js
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({
    storageState: 'grok-auth.json' // Salvar sessão
  });
  
  const page = await context.newPage();
  await page.goto('https://grok.com/share/...');
  
  // Aguardar carregar
  await page.waitForTimeout(10000);
  
  // Extrair
  const texto = await page.innerText('body');
  console.log(texto);
  
  await browser.close();
})();
```

---

## ✅ Checklist

- [ ] Abrir link no navegador
- [ ] Verificar se carregou completo
- [ ] Copiar texto (Método 1, 2 ou 3)
- [ ] Salvar em `Transcricoes/2025-12-09_conversa-manual.txt`
- [ ] Executar processamento automático
- [ ] Verificar Markdown gerado
- [ ] Atualizar workspace

---

**Próximo passo:** Escolher método e capturar conteúdo manualmente.
