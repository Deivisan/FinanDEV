# 💰 Finanças Automatizadas - Pix + Blockchain

> **Ideia:** Sistema financeiro centralizado com pagamentos automatizados  
> **Tecnologias:** Pix Automático + Blockchain (USDC/stablecoins)  
> **Status:** Brainstorm futuro  
> **Criado:** 16/11/2025

---

## 🎯 Conceito

Criar um sistema que automatize pagamentos recorrentes usando **Pix** como interface principal, mas com **blockchain** como camada de registro/auditoria descentralizada.

**Por quê?**
- Pix é instantâneo e universal no Brasil
- Blockchain permite auditoria transparente sem banco intermediário
- Automação elimina esquecimentos (TDAH-friendly)
- Centralização de controle (um dashboard para tudo)

---

## 🔧 Componentes Técnicos

### 1. Pix Automático (Lançado Junho 2025)
- **Débitos recorrentes:** Autoriza uma vez, roda sozinho
- **Casos de uso:** Contas fixas, assinaturas, compras mensais
- **Integração:** API Banco Central ou fintechs (Stripe, Volt.io)

### 2. Blockchain Layer
- **Stablecoins:** USDC, USDT (evita volatilidade crypto)
- **Chains:** Ethereum (segura), Solana (fees baixos), Polygon (rápida)
- **Apps bridge:** AEON Pay, Zypto (convertem crypto → Pix instantâneo)

**Fluxo:**
```
Saldo conta → Converte USDC (via API) → Agenda Pix Automático → Pagamento recorrente
```

### 3. Dashboard FinanDEV
- **Frontend:** Next.js + Tailwind CSS
- **Backend:** Python API (Flask/FastAPI)
- **Database:** JSON local + blockchain (auditoria)
- **Features:**
  - Visualizar saldo Pix + crypto
  - Agendar pagamentos recorrentes
  - Histórico transparente (blockchain explorer)
  - Alertas (vencimentos, saldo baixo)

---

## 🛠️ Stack Sugerido

### APIs a Integrar
| Serviço | Função | Custo |
|---------|--------|-------|
| **Pix API (Bacen)** | Débitos automáticos | Grátis via banco |
| **Stripe Pix** | Gateway pagamentos | Taxa 2.9% + R$0.50 |
| **Volt.io** | Automação Pix empresarial | Freemium |
| **AEON Pay** | Crypto → Pix bridge | Tx fees crypto |
| **Zypto** | USDC QR Pix converter | Taxa 1.5% |
| **Web3.py** | Gerenciar wallet blockchain | Open-source |

### Bibliotecas Python
```python
# Exemplo de integração básica
from web3 import Web3
import requests

# Conectar wallet Ethereum
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io'))
account = w3.eth.account.privateKeyToAccount('YOUR_KEY')

# Converter USDC → BRL via API
def convert_usdc_to_brl(amount_usdc):
    rate = requests.get('https://api.coinbase.com/v2/prices/USDC-BRL/spot').json()
    return amount_usdc * float(rate['data']['amount'])

# Agendar Pix via Stripe
def schedule_pix_payment(amount_brl, description):
    stripe.PaymentIntent.create(
        amount=int(amount_brl * 100),  # centavos
        currency='brl',
        payment_method_types=['pix'],
        description=description,
        metadata={'recorrente': 'mensal'}
    )
```

---

## 💡 Casos de Uso Reais

### 1. Suplementos Pro Ganho de Massa
- **Meta:** 60kg → 70kg (maio 2026)
- **Compras mensais:** Whey, creatina, vitaminas (~R$300/mês)
- **Automação:** Pix Automático agenda compra todo dia 1
- **Blockchain:** Registra cada compra (auditoria transparente)

### 2. Backup Mental (Cloud Storage)
- **Serviço:** Google Drive 200GB (R$6.99/mês)
- **Automação:** Pix recorrente
- **Dashboard:** Alerta se armazenamento >80%

### 3. Doações/Rifas Grupo Amigos
- **Conceito:** Contribuição R$10/pessoa para almoço coletivo
- **Automação:** Pix agendado quinzenal
- **Blockchain:** Registro transparente (quem pagou, quanto)

---

## 🚧 Limitações & Desafios

### Técnicas
- **Google Cloud API:** Precisa cartão cadastrado (mesmo tier free)
- **Fees crypto:** Conversão USDC → BRL tem taxa (~1-3%)
- **Volatilidade:** Stablecoins são mais estáveis, mas não 100%

### Legais
- **Regulação crypto Brasil:** Incerta, Bacen pode mudar regras
- **KYC:** Apps bridge (AEON, Zypto) exigem verificação identidade

### Alternativas Sem Blockchain
- Playwright automation: Script automatiza Pix no browser (sem API)
- Menos elegante, mas **zero custo** e funciona hoje

---

## 🎯 Roadmap de Implementação

### Fase 1: MVP Simples (Sem Blockchain)
- [ ] Script Python que agenda Pix via Stripe API
- [ ] Dashboard básico (Flask + JSON local)
- [ ] Testar com 1 pagamento recorrente (suplementos)

### Fase 2: Integração Blockchain
- [ ] Criar wallet Ethereum/Polygon
- [ ] Converter pequena quantia → USDC
- [ ] Testar bridge AEON Pay (USDC → Pix)

### Fase 3: Dashboard Completo
- [ ] Frontend Next.js responsivo
- [ ] Visualização gráficos (histórico, previsões)
- [ ] Alertas automáticos (vencimentos, saldo)

### Fase 4: Auditoria Transparente
- [ ] Cada pagamento → registro blockchain
- [ ] Explorer público (ver histórico financeiro)

---

## 📚 Referências

### Pix Automático
- Banco Central: Regulamentação débitos recorrentes (Jun 2025)
- Stripe Docs: stripe.com/docs/payments/pix

### Blockchain Bridges
- AEON Pay: aeonpay.io (crypto → Pix)
- Zypto: zypto.com (QR Pix + USDC)

### Web3 Python
- web3.py docs: web3py.readthedocs.io
- Infura: API Ethereum grátis tier

---

## 🔮 Visão Futuro

**2026:** Sistema completo com:
- IA que prevê gastos mensais (ML sobre histórico)
- Auto-ajuste orçamento (se sobra ↓, cancela assinaturas)
- Integração Grupo-Amigos-Bot (rifas automáticas)
- Dashboard web público (para amigos verem transparência)

---

*Ideia em desenvolvimento | Pode virar repositório standalone futuro*
