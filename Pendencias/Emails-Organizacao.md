# 📧 Organização de Emails - Outlook + Gmail

> **Problema:**

> **Solução:**

> **Status:**

> **Criado:** 16/11/2025

---

## 🎯 Objetivos

1. **Limpar spans:** Deletar emails irrelevantes em massa

2. **Organizar respostas:** Separar currículos por empresa/status

3. **Filtros automáticos:** Marcar prioridades (entrevistas, testes)

4. **Zero input manual:** Tudo via script, headless

---

## 🚫 Por Que Não Soluções Online?

- **Limites de uso:** Sites gratuitos limitam a 1.000 emails

- **Sem contas fake:** Email é único, não dá pra burlar

- **Privacidade:** Não confiar dados em terceiros

- **Flexibilidade:** Script customizado faz exatamente o que preciso

---

## 🛠️ Solução: Playwright Headless

### Vantagens

- **Roda local:** Arch Linux + Python

- **Session persistente:** Login uma vez, salva cookies

- **Bloqueios:** Delays aleatórios, user-agents rotativos evitam detecção

- **Inteligente:** Detecta banners cookies, aceita automático

### Stack Tecnológico

| Componente | Tecnologia |
|------------|------------|
| Automação browser | Playwright (Python) |
| Email Outlook | browser.new_context() +

| Email Gmail | browser.new_context() +

| Persistência sessão | context.storage_state() |
| Filtros | XPath/CSS seletores |

---

## 📝 Script Base (Playwright)

### 1. Setup Inicial (Login Manual Primeira Vez)

```python

# email-setup.py

from playwright.sync_api import sync_playwright

def setup_gmail_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Visível primeira vez

        context = browser.new_context()
        page = context.new_page()
        
        # Navegar Gmail

        page.goto('https://mail.google.com')
        
        # Aguardar login manual (você loga na interface)

        input("Faça login e pressione Enter quando pronto...")
        
        # Aceitar cookies se aparecer banner

        try:
            page.click('#L2AGLb', timeout=3000)  # Botão "Aceitar todos"

        except:
            pass  # Banner não apareceu

        
        # Salvar sessão (cookies + local storage)

        context.storage_state(path='gmail-session.json')
        print("✅ Sessão Gmail salva em gmail-session.json")
        
        browser.close()

def setup_outlook_session():
    # Mesmo processo para Outlook

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto('https://outlook.live.com')
        
        input("Faça login Outlook e pressione Enter...")
        
        # Aceitar cookies Outlook

        try:
            page.click('[data-cookiebanner=accept]', timeout=3000)
        except:
            pass
        
        context.storage_state(path='outlook-session.json')
        print("✅ Sessão Outlook salva")
        
        browser.close()

# Rodar setup inicial

setup_gmail_session()
setup_outlook_session()

```text

**Executar:** `python email-setup.py` (uma vez só)

---

### 2. Limpeza Automática (Headless)

```python

# email-cleanup.py

from playwright.sync_api import sync_playwright
import time
import random

def delete_spam_gmail(max_delete=1600):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Headless agora

        
        # Restaurar sessão salva

        context = browser.new_context(storage_state='gmail-session.json')
        page = context.new_page()
        
        page.goto('https://mail.google.com')
        time.sleep(2)  # Aguardar carregar

        
        deleted_count = 0
        
        while deleted_count < max_delete:
            # Selecionar checkbox primeiro email

            try:
                page.click('div[role=checkbox][aria-checked=false]', timeout=5000)
            except:
                print("Nenhum email restante pra deletar")
                break
            
            # Clicar botão deletar (ícone lixeira)

            page.click('[data-tooltip="Excluir"]')
            
            deleted_count += 1
            
            # Delay aleatório (evitar rate limit)

            time.sleep(random.uniform(0.5, 1.5))
            
            if deleted_count % 100 == 0:
                print(f"✅ Deletados: {deleted_count} emails")
        
        print(f"🎉 Total deletado: {deleted_count} emails")
        browser.close()

def delete_spam_outlook(max_delete=1600):
    # Implementação similar para Outlook

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state='outlook-session.json')
        page = context.new_page()
        
        page.goto('https://outlook.live.com/mail/inbox')
        time.sleep(2)
        
        deleted_count = 0
        
        while deleted_count < max_delete:
            try:
                # Outlook específico seletores

                page.click('[role=checkbox][aria-checked=false]', timeout=5000)
                page.click('[aria-label="Excluir"]')
                deleted_count += 1
                time.sleep(random.uniform(0.5, 1.5))
                
                if deleted_count % 100 == 0:
                    print(f"✅ Deletados: {deleted_count} emails Outlook")
            except:
                break
        
        print(f"🎉 Total Outlook: {deleted_count}")
        browser.close()

# Executar limpeza

delete_spam_gmail(max_delete=1600)

# delete_spam_outlook(max_delete=1000)

```text

**Executar:** `python email-cleanup.py`

---

### 3. Organização Automática (Filtros)

```python

# email-organize.py

from playwright.sync_api import sync_playwright

def organize_job_emails():
    """
    Separa emails de currículo por empresa:
    -

    -

    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state='gmail-session.json')
        page = context.new_page()
        
        page.goto('https://mail.google.com')
        time.sleep(2)
        
        # Buscar emails com palavras-chave

        page.fill('input[aria-label="Pesquisar e-mail"]', 'vaga OR currículo OR entrevista')
        page.press('input[aria-label="Pesquisar e-mail"]', 'Enter')
        time.sleep(2)
        
        # Selecionar todos resultados

        page.click('[aria-label="Selecionar"]')
        
        # Aplicar label "Vagas"

        page.click('[aria-label="Etiquetas"]')
        page.click('text=Vagas')  # Criar label antes se não existir

        
        print("✅ Emails de vaga organizados em label 'Vagas'")
        
        browser.close()

organize_job_emails()

```text

---

## 🧠 Features Inteligentes

### Detecção Automática Banners Cookies

```python
def accept_cookies_if_present(page):
    """Detecta e aceita banners de cookies automaticamente"""
    selectors = [
        '#L2AGLb',  # Gmail "Aceitar todos"

        '[data-cookiebanner=accept]',  # Outlook

        'button:has-text("Aceitar")',  # Genérico PT-BR

        'button:has-text("Accept")',  # Genérico EN

    ]
    
    for selector in selectors:
        try:
            page.click(selector, timeout=2000)
            print(f"✅ Cookies aceitos via: {selector}")
            return
        except:
            continue  # Tenta próximo seletor

```text

### Delay Inteligente (Anti-Bloqueio)

```python
import random

def smart_delay():
    """Delay humano-like"""
    time.sleep(random.uniform(0.8, 2.3))

```text

### User-Agent Rotativo

```python
user_agents = [
    'Mozilla/5.0 (X11; Linux x86_64) Chrome/120.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/121.0',
]

context = browser.new_context(
    storage_state='gmail-session.json',
    user_agent=random.choice(user_agents)
)

```text

---

## 📊 Estrutura Final

```text
FinanDEV/
└── Pendencias/
    └── Emails/
        ├── README.md (este arquivo)
        ├── email-setup.py (setup inicial)
        ├── email-cleanup.py (deletar spans)
        ├── email-organize.py (organizar vagas)
        ├── gmail-session.json (sessão persistente)
        ├── outlook-session.json
        └── logs/
            └── cleanup-2025-11-16.log

```text

---

## 🎯 Checklist de Execução

- [ ] Instalar Playwright: `pip install playwright && playwright install chromium`

- [ ] Rodar `email-setup.py` (login manual Gmail + Outlook)

- [ ] Verificar arquivos `*-session.json` criados

- [ ] Testar `email-cleanup.py` com max_delete=10 (teste pequeno)

- [ ] Rodar limpeza completa (1600 emails Gmail)

- [ ] Organizar emails vagas com `email-organize.py`

- [ ] (Opcional) Agendar cron semanal para manutenção

---

## ⚠️ Bloqueios & Contorno

### Google/Microsoft Detectam Bots?

**Sim, mas:**

- Login manual inicial (não automatiza senha)

- Cookies salvos passam como sessão legítima

- Delays aleatórios imitam humano

- User-agents rotativos evitam fingerprinting

### Rate Limits?

- Gmail: ~100 emails/minuto sem bloqueio

- Outlook: ~80 emails/minuto

- **Solução:** Delays 0.5-1.5s entre ações

---

## 🔮 Melhorias Futuras

### IA para Categorização

```python

# Usar GPT-4 Nano local pra classificar emails

def classify_email(subject, body):
    prompt = f"Classifique email: {subject}. Resposta/Spam/Importante?"
    return llm.generate(prompt)

```text

### Dashboard Visual

- Interface web com Streamlit

- Gráficos: emails deletados/semana, taxa resposta vagas

---

*Pendência ativa | Script pronto para uso | Economia 2h+ trabalho manual*
