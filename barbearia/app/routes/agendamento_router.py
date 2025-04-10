from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.agendamento import Agendamento, AgendamentoCreate, AgendamentoUpdate
from app.services.agendamento_service import AgendamentoService
from fastapi import Request
from app.repositories.agendamento_repository import AgendamentoRepository
from app.database.session import get_db
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="/app/templates")

@router.get("/", include_in_schema=False)
async def list_agendamentos(request: Request, db: Session = Depends(get_db)):
    agendamento_repository = AgendamentoRepository(db)
    agendamento_service = AgendamentoService(agendamento_repository)
    agendamentos = agendamento_service.get_agendamentos()
    return agendamentos
    # return templates.TemplateResponse("agendamentos.html", {"request": request, "agendamentos": agendamentos})

@router.get("/", response_model=list[Agendamento])
def read_agendamentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    agendamento_repository = AgendamentoRepository(db)
    agendamento_service = AgendamentoService(agendamento_repository)
    return agendamento_service.get_agendamentos(skip, limit)

@router.get("/{agendamento_id}", response_model=Agendamento)
def read_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    agendamento_repository = AgendamentoRepository(db)
    agendamento_service = AgendamentoService(agendamento_repository)
    db_agendamento = agendamento_service.get_agendamento(agendamento_id)
    if db_agendamento is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agendamento não encontrado"
        )
    return db_agendamento

@router.get("/agendamento/cliente/{cliente_id}", response_model=list[Agendamento])
def get_agendamento_por_cliente(cliente_id: int, db: Session = Depends(get_db)):
    agendamento_repository = AgendamentoRepository(db)
    agendamento_service = AgendamentoService(agendamento_repository)
    db_agendamentos = agendamento_service.get_agendamento_por_cliente(cliente_id)
    return db_agendamentos

@router.post("/", response_model=Agendamento, status_code=status.HTTP_201_CREATED)
def create_agendamento(agendamento: AgendamentoCreate, db: Session = Depends(get_db)):
    agendamento_repository = AgendamentoRepository(db)
    agendamento_service = AgendamentoService(agendamento_repository)
    return agendamento_service.create_agendamento(agendamento)

@router.put("/{agendamento_id}", response_model=Agendamento)
def update_agendamento(
    agendamento_id: int, 
    agendamento: AgendamentoUpdate, 
    db: Session = Depends(get_db)
):
    agendamento_repository = AgendamentoRepository(db)
    agendamento_service = AgendamentoService(agendamento_repository)
    db_agendamento = agendamento_service.update_agendamento(agendamento_id, agendamento)
    if db_agendamento is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agendamento não encontrado"
        )
    return db_agendamento

@router.delete("/{agendamento_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    agendamento_repository = AgendamentoRepository(db)
    agendamento_service = AgendamentoService(agendamento_repository)
    success = agendamento_service.delete_agendamento(agendamento_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agendamento não encontrado"
        )
    
    return JSONResponse(content={"message": "Agendamento deletado com sucesso"}, status_code=200)
    