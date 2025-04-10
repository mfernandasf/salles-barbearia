from fastapi import APIRouter, Depends, HTTPException, status, Form, File, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.produto import Produto, ProdutoCreate, ProdutoUpdate
from app.services.produto_service import ProdutoService
from fastapi import Request
from app.repositories.produto_repository import ProdutoRepository
from app.database.session import get_db
from fastapi.templating import Jinja2Templates
import shutil
import os
from uuid import uuid4


router = APIRouter()
templates = Jinja2Templates(directory="app/frontend")

@router.get("/view", include_in_schema=False)
async def list_produtos(request: Request, db: Session = Depends(get_db)):
    produto_repository = ProdutoRepository(db)
    produto_service = ProdutoService(produto_repository)
    produtos = produto_service.get_produtos(limit=3)
 
    return templates.TemplateResponse("index.html", {"request": request, "produtos": produtos})

@router.get("/", response_model=list[Produto])
def read_produtos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    produto_repository = ProdutoRepository(db)
    produto_service = ProdutoService(produto_repository)
    return produto_service.get_produtos(skip, limit)

@router.get("/{produto_id}", response_model=Produto)
def read_produto(produto_id: int, db: Session = Depends(get_db)):
    produto_repository = ProdutoRepository(db)
    produto_service = ProdutoService(produto_repository)
    db_produto = produto_service.get_produto(produto_id)
    if db_produto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    return db_produto

@router.post("/", response_model=Produto, status_code=status.HTTP_201_CREATED)
def create_produto( 
    nome: str = Form(...),
    categoria: str = Form(...),
    preco: float = Form(...),
    quantidade_estoque: int = Form(...),
    desconto: int = Form(0),
    descricao: str = Form(""),
    image: UploadFile = File(None), 
    db: Session = Depends(get_db)):

    produto_repository = ProdutoRepository(db)
    produto_service = ProdutoService(produto_repository)

    return produto_service.create_produto(
        nome=nome,
        categoria=categoria,
        preco=preco,
        quantidade_estoque=quantidade_estoque,
        desconto=desconto,
        descricao=descricao,
        image=image)
    
@router.put("/{produto_id}", response_model=Produto)
def update_produto(
    produto_id: int,
    nome: str = Form(...),
    categoria: str = Form(...),
    preco: float = Form(...),
    quantidade_estoque: int = Form(...),
    desconto: float = Form(0),
    descricao: str = Form(""),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):

    produto ={
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade_estoque": quantidade_estoque,
        "desconto": desconto,
        "descricao": descricao,
    }


    produto_repository = ProdutoRepository(db)
    produto_service = ProdutoService(produto_repository)
    db_produto = produto_service.update_produto(produto_id, produto, image)

    if db_produto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    return db_produto

@router.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_produto(produto_id: int, db: Session = Depends(get_db)):
    produto_repository = ProdutoRepository(db)
    produto_service = ProdutoService(produto_repository)
    success = produto_service.delete_produto(produto_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    
    return JSONResponse(content={"message": "Produto deletado com sucesso"}, status_code=200)
    