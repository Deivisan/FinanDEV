# 📸 Google Photos - Organização Automática

> **Problema:**

> **Solução:**

> **Status:**

> **Criado:** 16/11/2025

---

## 🎯 Objetivos

1. **Limpar fotos aleatórias:** Mover para lixeira fotos duplicadas/sem valor

2. **Organizar álbuns:** Criar categorias (Físico 2025, Ambiente Dev, Treinos)

3. **Automação:** Script roda periodicamente, mantém tudo organizado

4. **Filtros inteligentes:** Por data, tags, reconhecimento facial

---

## 🛠️ Duas Abordagens

### Opção 1: Aceitar a Desorganização Atual

#### Vantagens (Opção 1)

- Zero esforço

- Nenhuma mudança necessária

- Fotos preservadas como estão

#### Desvantagens (Opção 1)

### Opção 2: Playwright Automation (Sem API)

#### Vantagens

- **Zero custo:** Não precisa Google Cloud

- **Zero setup:** Usa browser direto

- **Funciona hoje:** Sem burocracia

#### Desvantagens

- **Mais lento:** Browser automation é mais pesado

- **Menos preciso:** Seletores podem mudar se Google atualizar

---

## 📝 Solução 1: Google Photos API

### Setup Inicial (Google Cloud)

1. **Criar projeto:** console.cloud.google.com

2. **Ativar API:** Google Photos Library API

3. **Credentials:** OAuth 2.0 Client ID (Desktop app)

4. **Scopes:** `photoslibrary.readonly`, `photoslibrary.appendonly`

5. **Baixar:** `credentials.json`

### Script Python (google-photos-api.py)

```python

# google-photos-organize.py

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle
import os

SCOPES = ['https://www.googleapis.com/auth/photoslibrary']

def authenticate():
    """Autentica via OAuth (uma vez)"""
    creds = None
    
    # Token salvo

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Se inválido, re-autentica

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Salva token

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return build('photoslibrary', 'v1', credentials=creds)

def list_all_photos(service):
    """Lista todas as fotos"""
    results = service.mediaItems().list(pageSize=100).execute()
    items = results.get('mediaItems', [])
    
    print(f"✅ Total fotos: {len(items)}")
    for item in items[:10]:  # Mostra primeiras 10

        print(f"  -

    
    return items

def create_album(service, title):
    """Cria álbum novo"""
    album = service.albums().create(
        body={'album': {'title': title}}
    ).execute()
    
    print(f"✅ Álbum criado: {title}")
    return album['id']

def add_photos_to_album(service, album_id, media_items):
    """Adiciona fotos a um álbum"""
    service.albums().batchAddMediaItems(
        albumId=album_id,
        body={'mediaItemIds': [item['id'] for item in media_items]}
    ).execute()
    
    print(f"✅ {len(media_items)} fotos adicionadas ao álbum")

# Uso

service = authenticate()
photos = list_all_photos(service)

# Criar álbum "Físico 2025"

album_id = create_album(service, 'Físico 2025')

# Filtrar fotos por data (exemplo: últimos 30 dias)

recent_photos = [p for p in photos if '2025-11' in p.get('mediaMetadata', {}).get('creationTime', '')]

add_photos_to_album(service, album_id, recent_photos)

```text

**Instalar deps:** `pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client`

---

## 📝 Solução 2: Playwright (Sem API)

### Script Python (Headless)

```python

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

setup_session()  # Uma vez

organize_photos()

```text

---

## 🎯 Casos de Uso

### 1. Álbum "Físico 2025" (Meta +10kg)

- **Filtro:** Fotos com tag "corpo" ou data específica (quinzenal)

- **Automação:** Script roda dia 1 e 15 de cada mês

- **Integração:** ROTINA-FISICA.md referencia álbum

### 2. Álbum "Ambiente Dev" (Backup Visual)

- **Filtro:** Fotos 360° do setup (panoramas)

- **Uso futuro:** Comparar workspace ao longo dos anos

### 3. Álbum "Treinos"

- **Filtro:** Vídeos 4K de exercícios

- **Análise:** Revisar forma, contar reps

---

## 🧠 Filtros Inteligentes

### Por Data

```python

# Fotos últimos 30 dias

recent = [p for p in photos if datetime.fromisoformat(p['mediaMetadata']['creationTime']) > (datetime.now() -

```text

### Por Local (GPS)

```python

# Fotos tiradas em casa (lat/lon aproximado)

home_photos = [p for p in photos if 'location' in p['mediaMetadata'] and is_near_home(p['mediaMetadata']['location'])]

```text

### Por Reconhecimento Facial

```python

# Fotos com seu rosto (Google detecta automático)

my_face_photos = [p for p in photos if 'photo' in p['mediaMetadata'] and any(face['personId'] == 'YOUR_ID' for face in p.get('faces', []))]

```text

---

## ⚠️ Limitações

### API (Google Cloud)

- **Cartão obrigatório:** Mesmo tier free precisa cadastrar

- **Quotas:** 10.000 requests/dia (suficiente para uso pessoal)

- **Leitura only:** API não deleta fotos (só adiciona a álbuns)

### Playwright

- **Seletores frágeis:** Google pode mudar HTML a qualquer momento

- **Mais lento:** Browser automation é pesado

- **Rate limits:** Ações muito rápidas podem travar

---

## 🎯 Checklist Execução

### Opção API

- [ ] Criar projeto Google Cloud

- [ ] Ativar Google Photos Library API

- [ ] Baixar credentials.json

- [ ] Rodar `google-photos-organize.py`

- [ ] Autenticar OAuth (primeira vez)

- [ ] Criar álbuns necessários

- [ ] Filtrar e organizar fotos

### Opção Playwright

- [ ] Instalar Playwright: `pip install playwright && playwright install`

- [ ] Rodar `google-photos-playwright.py` (login manual)

- [ ] Salvar sessão (`photos-session.json`)

- [ ] Organizar fotos headless

---

## 🔮 Melhorias Futuras

### IA para Categorização

```python

# Usar vision API pra detectar conteúdo

def classify_photo(image_path):
    # Google Vision API: detecta objetos, cenas

    # "Setup dev" → move pra álbum Ambiente Dev

    # "Corpo" → move pra Físico 2025

    pass

```text

### Automação Cron

```bash

# Rodar todo domingo às 20:00

0 20 *

```text

---

*Pendência ativa | Duas soluções prontas | Escolher conforme preferência*
