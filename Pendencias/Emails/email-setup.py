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