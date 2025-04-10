import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import (
    cliente_router,
    agendamento_router,
    servico_router,
    produto_router,
    barbeiro_router,
    venda_route,
    auth_router
    # contato_router
    
)

app = FastAPI(title="Salles Barbearia API", version="1.0.0")

# Configuração CORS para permitir seu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

# Caminho da pasta frontend
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "app", "frontend")

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Página inicial
@app.get("/", response_class=HTMLResponse)
async def get_home():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

# Sobercarga para a pãgina inicial para casos onde é acessada de pãginas internas
@app.get("/index.html", response_class=HTMLResponse)
async def get_home():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/produtos-detalhe.html")
async def get_produtos_detalhe():
    return FileResponse(os.path.join(FRONTEND_DIR, "produtos-detalhe.html"))

@app.get("/produtos.html")
async def get_produtos():
    return FileResponse(os.path.join(FRONTEND_DIR, "produtos.html"))

@app.get("/agendamento.html")
async def get_agendamentos():
    return FileResponse(os.path.join(FRONTEND_DIR, "agendamento.html"))

@app.get("/cadastro.html")
async def get_agendamentos():
    return FileResponse(os.path.join(FRONTEND_DIR, "cadastro.html"))

@app.get("/login.html")
async def get_agendamentos():
    return FileResponse(os.path.join(FRONTEND_DIR, "login.html"))

@app.get("/clientes.html")
async def get_agendamentos():
    return FileResponse(os.path.join(FRONTEND_DIR, "clientes.html"))

@app.get("/barbeiros.html")
async def get_agendamentos():
    return FileResponse(os.path.join(FRONTEND_DIR, "barbeiros.html"))

@app.get("/admin/cadastro-barbeiro.html")
def get_cadastro_produto():
    caminho = os.path.join(FRONTEND_DIR, "admin", "cadastro-barbeiro.html")
    return FileResponse(caminho, media_type='text/html')

@app.get("/admin/cadastro-produto.html")
def get_cadastro_produto():
    caminho = os.path.join(FRONTEND_DIR, "admin", "cadastro-produto.html")
    return FileResponse(caminho, media_type='text/html')


# Incluir rotas
app.include_router(cliente_router.router, prefix="/api/clientes", tags=["clientes"])
app.include_router(agendamento_router.router, prefix="/api/agendamentos", tags=["agendamentos"])
app.include_router(venda_route.router, prefix="/api/vendas", tags=["vendas"])
app.include_router(servico_router.router, prefix="/api/servicos", tags=["servicos"])
app.include_router(auth_router.router, prefix="/api/auth", tags=["auth"])
app.include_router(produto_router.router, prefix="/api/produtos", tags=["produtos"])
app.include_router(barbeiro_router.router, prefix="/api/barbeiros", tags=["barbeiros"])
# app.include_router(contato_router.router, prefix="/api/contato", tags=["contato"])

