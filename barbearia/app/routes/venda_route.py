from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.venda import Venda, VendaCreate, VendaUpdate
from app.services.venda_service import VendaService
from fastapi import Request
from app.repositories.venda_repository import VendaRepository
from app.database.session import get_db
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="/app/templates")

@router.get("/", include_in_schema=False)
async def list_vendas(request: Request, db: Session = Depends(get_db)):
    venda_repository = VendaRepository(db)
    venda_service = VendaService(venda_repository)
    vendas = venda_service.get_vendas()
    return vendas
    # return templates.TemplateResponse("vendas.html", {"request": request, "vendas": vendas})

@router.get("/", response_model=list[Venda])
def read_vendas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    venda_repository = VendaRepository(db)
    venda_service = VendaService(venda_repository)
    return venda_service.get_vendas(skip, limit)

@router.get("/{venda_id}", response_model=Venda)
def read_venda(venda_id: int, db: Session = Depends(get_db)):
    venda_repository = VendaRepository(db)
    venda_service = VendaService(venda_repository)
    db_venda = venda_service.get_venda(venda_id)
    if db_venda is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Venda não encontrado"
        )
    return db_venda

@router.post("/", response_model=Venda, status_code=status.HTTP_201_CREATED)
def create_venda(venda: VendaCreate, db: Session = Depends(get_db)):
    venda_repository = VendaRepository(db)
    venda_service = VendaService(venda_repository)
    db_venda =  venda_service.create_venda(venda)

    if db_venda is None:
         raise HTTPException(
            status_code=status.HTTP_422_NOT_FOUND,
            detail="O produto que deseja comprar não está cadastrado no sistema ou não possui exemplares em estoque"
        )
    
    return db_venda


@router.put("/{venda_id}", response_model=Venda)
def update_venda(
    venda_id: int, 
    venda: VendaUpdate, 
    db: Session = Depends(get_db)
):
    venda_repository = VendaRepository(db)
    venda_service = VendaService(venda_repository)
    db_venda = venda_service.update_venda(venda_id, venda)
    if db_venda is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Venda não encontrado"
        )
    return JSONResponse(content={"message": "Venda concluída com sucesso"}, status_code=200)

@router.delete("/{venda_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_venda(venda_id: int, db: Session = Depends(get_db)):
    venda_repository = VendaRepository(db)
    venda_service = VendaService(venda_repository)
    success = venda_service.delete_venda(venda_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Venda não encontrado"
        )
    
    return JSONResponse(content={"message": "Venda deletado com sucesso"}, status_code=200)
    