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