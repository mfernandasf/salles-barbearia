from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.cliente import Cliente, ClienteCreate, ClienteUpdate
from app.services.cliente_service import ClienteService
from fastapi import Request
from app.repositories.cliente_repository import ClienteRepository
from app.database.session import get_db
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="/app/templates")

# @router.get("/", include_in_schema=False)
# async def list_clientes(request: Request, db: Session = Depends(get_db)):
#     cliente_repository = ClienteRepository(db)
#     cliente_service = ClienteService(cliente_repository)
#     clientes = cliente_service.get_clientes()
#     # return clientes
#     return templates.TemplateResponse("clientes.html", {"request": request, "clientes": clientes})

@router.get("/", response_model=list[Cliente])
def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cliente_repository = ClienteRepository(db)
    cliente_service = ClienteService(cliente_repository)
    return cliente_service.get_clientes(skip, limit)

@router.get("/{cliente_id}", response_model=Cliente)
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente_repository = ClienteRepository(db)
    cliente_service = ClienteService(cliente_repository)
    db_cliente = cliente_service.get_cliente(cliente_id)
    if db_cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    return db_cliente

@router.post("/", response_model=Cliente, status_code=status.HTTP_201_CREATED)
def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    print("Recebendo cliente:", cliente.dict())
    cliente_repository = ClienteRepository(db)
    cliente_service = ClienteService(cliente_repository)
    return cliente_service.create_cliente(cliente)

@router.put("/{cliente_id}", response_model=Cliente)
def update_cliente(
    cliente_id: int, 
    cliente: ClienteUpdate, 
    db: Session = Depends(get_db)
):
    cliente_repository = ClienteRepository(db)
    cliente_service = ClienteService(cliente_repository)
    db_cliente = cliente_service.update_cliente(cliente_id, cliente)
    if db_cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    return db_cliente

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente_repository = ClienteRepository(db)
    cliente_service = ClienteService(cliente_repository)
    success = cliente_service.delete_cliente(cliente_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    
    return JSONResponse(content={"message": "Cliente deletado com sucesso"}, status_code=200)
    