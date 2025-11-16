#!/usr/bin/env python3
"""
FinanDEV Dashboard - Backend API
Criado: 16/11/2025
Autor: Deivison Santana (@DeiviTech)

Requisitos:
    pip install fastapi uvicorn pandas gitpython

Uso:
    python dashboard.py
    # Acesse: http://localhost:8000
    # Docs: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path
import json
import sys
from typing import Dict, List, Optional
from datetime import datetime

# [A INSTALAR] Deps opcionais
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("⚠️ Pandas não instalado - algumas features desabilitadas")

try:
    import git
    GIT_AVAILABLE = True
except ImportError:
    GIT_AVAILABLE = False
    print("⚠️ GitPython não instalado - stats git desabilitados")

# === Config ===
app = FastAPI(
    title="FinanDEV Dashboard API",
    description="Backend para dashboard FinanDEV - Backup Mental Deivison",
    version="0.1.0"
)

# CORS (permitir frontend acessar)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # [PROD] Trocar para domínio específico
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Paths ===
REPO_ROOT = Path(__file__).parent.parent
VIDA_JSON = REPO_ROOT / "Vida-Deivison.json"
DASHBOARD_DATA = Path(__file__).parent / "data"
DASHBOARD_DATA.mkdir(exist_ok=True)

# === Routes ===

@app.get("/")
def root():
    """Health check"""
    return {
        "status": "ok",
        "message": "FinanDEV Dashboard API rodando",
        "version": "0.1.0",
        "repo": str(REPO_ROOT),
        "pandas": PANDAS_AVAILABLE,
        "git": GIT_AVAILABLE
    }


@app.get("/metrics")
def get_metrics():
    """
    Retorna métricas principais do Vida-Deivison.json
    
    Returns:
        Dict com: weight, nutrition, finance, sleep, etc
    """
    try:
        if not VIDA_JSON.exists():
            raise HTTPException(404, f"Vida-Deivison.json não encontrado em {VIDA_JSON}")
        
        with open(VIDA_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Parse dados relevantes
        metrics = {
            "weight": {
                "current": data.get("peso_atual", "[A EDITAR]"),
                "goal": data.get("meta_peso", 70),
                "lastUpdate": data.get("ultima_atualizacao", "N/A")
            },
            "nutrition": {
                "caloriesGoal": data.get("calorias_dia", 2400),
                "proteinGoal": data.get("proteinas_dia", 100),
                "meals": data.get("refeicoes_dia", 5)
            },
            "finance": {
                "salary": data.get("salario_liquido", 1866.53),
                "fixedExpenses": data.get("gastos_fixos", 780.00),
                "monthlyBalance": data.get("sobra_mensal", 1086.54),
                "biweeklyBudget": data.get("orcamento_quinzenal", 250.00),
                "actualSpending": data.get("gasto_real", "[A EDITAR]"),
                "savings": data.get("economia", "[A EDITAR]")
            },
            "lastUpdate": datetime.now().isoformat()
        }
        
        return metrics
        
    except json.JSONDecodeError as e:
        raise HTTPException(500, f"Erro ao parsear JSON: {e}")
    except Exception as e:
        raise HTTPException(500, f"Erro ao ler métricas: {e}")


@app.get("/commits")
def get_commits_stats():
    """
    Retorna estatísticas Git da semana
    
    Returns:
        Dict com: commits, linesAdded, filesChanged, lastMessage
    """
    if not GIT_AVAILABLE:
        return {
            "error": "GitPython não instalado",
            "install": "pip install gitpython"
        }
    
    try:
        repo = git.Repo(REPO_ROOT)
        
        # Últimos 7 dias
        since = (datetime.now() - pd.Timedelta(days=7)).isoformat() if PANDAS_AVAILABLE else "1.week.ago"
        commits = list(repo.iter_commits('main', max_count=50, since=since))
        
        stats = {
            "commitsWeek": len(commits),
            "linesAdded": 0,  # [A IMPLEMENTAR] Parse git diff
            "filesChanged": 0,  # [A IMPLEMENTAR] Parse git diff
            "lastMessage": commits[0].message.strip() if commits else "N/A",
            "lastAuthor": commits[0].author.name if commits else "N/A",
            "lastDate": commits[0].committed_datetime.isoformat() if commits else "N/A"
        }
        
        return stats
        
    except Exception as e:
        raise HTTPException(500, f"Erro ao ler stats Git: {e}")


@app.get("/tasks")
def get_tasks():
    """
    Retorna lista de tarefas de Pendencias/
    
    Returns:
        List[Dict] com: id, text, done, file
    """
    try:
        pendencias_dir = REPO_ROOT / "Pendencias"
        if not pendencias_dir.exists():
            return {"tasks": [], "message": "Pasta Pendencias/ não encontrada"}
        
        tasks = []
        # [A IMPLEMENTAR] Parse checkboxes MDs em Pendencias/
        # Por enquanto retorna mock
        tasks = [
            {"id": 1, "text": "Testar 5 GCam ports Poco X5", "done": False, "file": "Camerologia"},
            {"id": 2, "text": "Capturar 20-30 fotos rosto", "done": False, "file": "Face-Capture"},
            {"id": 3, "text": "Implementar email-cleanup.py", "done": False, "file": "Emails-Organizacao.md"},
            {"id": 4, "text": "Preencher Ambiente-Dev/PC/", "done": False, "file": "Ambiente-Dev"},
            {"id": 5, "text": "Organizar Google Photos álbuns", "done": False, "file": "Google-Photos-Organizacao.md"}
        ]
        
        return {"tasks": tasks, "count": len(tasks)}
        
    except Exception as e:
        raise HTTPException(500, f"Erro ao ler tarefas: {e}")


@app.post("/weight")
def add_weight(peso: float):
    """
    Adiciona novo registro de peso
    
    Args:
        peso: Peso em kg
    
    Returns:
        Dict confirmação
    """
    # [A IMPLEMENTAR] Salvar em Vida-Deivison.json ou arquivo separado
    return {
        "status": "ok",
        "message": f"Peso {peso}kg registrado (mock - não salvo ainda)",
        "timestamp": datetime.now().isoformat()
    }


@app.post("/mood")
def add_mood(humor: int):
    """
    Adiciona registro de humor (1-5)
    
    Args:
        humor: Escala 1 (péssimo) a 5 (excelente)
    
    Returns:
        Dict confirmação
    """
    if humor < 1 or humor > 5:
        raise HTTPException(400, "Humor deve estar entre 1 e 5")
    
    # [A IMPLEMENTAR] Salvar em Mini-Sistemas/SAUDE-MENTAL.md
    return {
        "status": "ok",
        "message": f"Humor {humor}/5 registrado (mock - não salvo ainda)",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/roadmap")
def get_roadmap():
    """
    Retorna conteúdo do roadmap markdown
    
    Returns:
        Dict com: content (MD bruto), stats
    """
    try:
        roadmap_file = REPO_ROOT / "Roadmaps" / "roadmap-mudancas-novembro.md"
        if not roadmap_file.exists():
            raise HTTPException(404, "Roadmap não encontrado")
        
        with open(roadmap_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse stats simples
        lines = content.split('\n')
        sections = [l for l in lines if l.startswith('## ')]
        
        return {
            "content": content,
            "stats": {
                "lines": len(lines),
                "sections": len(sections),
                "lastUpdate": "16/11/2025"  # [A IMPLEMENTAR] Parse do MD
            }
        }
        
    except Exception as e:
        raise HTTPException(500, f"Erro ao ler roadmap: {e}")


# === Run Server ===
if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Iniciando FinanDEV Dashboard API...")
    print(f"📂 Repo root: {REPO_ROOT}")
    print(f"📊 Vida-Deivison.json: {'✅' if VIDA_JSON.exists() else '❌'}")
    print(f"🐼 Pandas: {'✅' if PANDAS_AVAILABLE else '❌'}")
    print(f"🔧 Git: {'✅' if GIT_AVAILABLE else '❌'}")
    print("\n🌐 Acesse:")
    print("   Frontend: Abrir Dashboard/index.html no navegador")
    print("   API Docs: http://localhost:8000/docs")
    print("   Health: http://localhost:8000/")
    print("\n⚠️ CTRL+C para parar\n")
    
    uvicorn.run(
        "dashboard:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload em dev
        log_level="info"
    )
