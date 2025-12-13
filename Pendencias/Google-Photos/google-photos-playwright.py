# google-photos-playwright.py

from playwright.sync_api import sync_playwright
import time

def setup_session():
    """Login manual primeira vez"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://photos.google.com')

        input("Faça login e pressione Enter...")

        # Salvar sessão
        context.storage_state(path='photos-session.json')
        print("✅ Sessão salva")

        browser.close()

def organize_photos():
    """Organiza fotos em álbuns"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state='photos-session.json')
        page = context.new_page()

        page.goto('https://photos.google.com')
        time.sleep(2)

        # Criar álbum "Ambiente Dev"
        page.click('[aria-label="Álbuns"]')
        page.click('text=Criar álbum')
        page.fill('input[placeholder="Adicionar título"]', 'Ambiente Dev')
        page.click('text=Concluir')

        print("✅ Álbum 'Ambiente Dev' criado")

        # Buscar fotos por data (exemplo: novembro 2025)
        page.goto('https://photos.google.com/search')
        page.fill('input[placeholder="Pesquisar fotos"]', 'novembro 2025')
        page.press('input[placeholder="Pesquisar fotos"]', 'Enter')
        time.sleep(2)

        # Selecionar primeiras 20 fotos
        for i in range(20):
            try:
                page.click(f'[data-index="{i}"]', timeout=1000)
            except:
                break

        # Adicionar ao álbum
        page.click('[aria-label="Mais opções"]')
        page.click('text=Adicionar ao álbum')
        page.click('text=Ambiente Dev')

        print("✅ Fotos adicionadas ao álbum")

        browser.close()

# Rodar
# setup_session()  # Uma vez
# organize_photos()