/**
 * Script para atualizar timestamps automaticamente
 * Uso: node scripts/update-timestamps.js
 * 
 * Atualiza:
 * - Vida-Deivison.json (ultima_atualizacao)
 * - README.md (última atualização)
 * - Qualquer arquivo com padrão "Última atualização:"
 */

const fs = require('fs');
const path = require('path');

// Data atual formatada
const now = new Date();
const isoDate = now.toISOString();
const brDate = now.toLocaleDateString('pt-BR', {
  day: '2-digit',
  month: '2-digit',
  year: 'numeric'
});
const brDateTime = `${brDate} ${now.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })}`;

console.log(`📅 Atualizando timestamps para: ${brDateTime}`);

// 1. Atualizar Vida-Deivison.json
const vidaPath = 'Vida-Deivison.json';
if (fs.existsSync(vidaPath)) {
  try {
    const vida = JSON.parse(fs.readFileSync(vidaPath, 'utf-8'));
    vida.meta.ultima_atualizacao = isoDate;
    fs.writeFileSync(vidaPath, JSON.stringify(vida, null, 2), 'utf-8');
    console.log(`✅ ${vidaPath} atualizado`);
  } catch (e) {
    console.error(`❌ Erro em ${vidaPath}:`, e.message);
  }
}

// 2. Atualizar arquivos Markdown com padrão "Última atualização:"
const mdFiles = [
  'README.md',
  'Mini-Sistemas/Ativos/README.md',
  'Mini-Sistemas/Ativos/SAUDE-MENTAL-ATIVO.md',
  'Mini-Sistemas/Ativos/SLEEP-TRACKING-ATIVO.md',
  'Pendencias/PENDENCIAS-ATIVAS-09DEZ2025.md'
];

mdFiles.forEach(file => {
  if (fs.existsSync(file)) {
    try {
      let content = fs.readFileSync(file, 'utf-8');
      
      // Padrão 1: *Última atualização: DD/MM/YYYY*
      content = content.replace(
        /\*Última atualização:.*\*/g,
        `*Última atualização: ${brDate}*`
      );
      
      // Padrão 2: **Última Atualização:** DD/MM/YYYY
      content = content.replace(
        /\*\*Última Atualização:\*\*.*$/gm,
        `**Última Atualização:** ${brDate}`
      );
      
      fs.writeFileSync(file, content, 'utf-8');
      console.log(`✅ ${file} atualizado`);
    } catch (e) {
      console.error(`❌ Erro em ${file}:`, e.message);
    }
  }
});

console.log(`\n🎉 Timestamps atualizados com sucesso!`);
console.log(`   ISO: ${isoDate}`);
console.log(`   BR:  ${brDateTime}`);
