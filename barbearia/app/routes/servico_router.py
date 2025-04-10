from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.servico import Servico, ServicoCreate, ServicoUpdate
from app.services.servico_service import ServicoService
from app.repositories.servico_repository import ServicoRepository
from app.database.session import get_db

router = APIRouter()

@router.get("/", response_model=list[Servico])
def listar_servicos(db: Session = Depends(get_db)):
    repo = ServicoRepository(db)
    service = ServicoService(repo)
    return service.get_servicos()

@router.get("/{servico_id}", response_model=Servico)
def obter_servico(servico_id: int, db: Session = Depends(get_db)):
    repo = ServicoRepository(db)
    service = ServicoService(repo)
    servico = service.get_servico(servico_id)
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return servico

@router.post("/", response_model=Servico, status_code=status.HTTP_201_CREATED)
def create_servico(servico: ServicoCreate, db: Session = Depends(get_db)):
    servico_repository = ServicoRepository(db)
    servico_service = ServicoService(servico_repository)
    return servico_service.create_servico(servico)

@router.put("/{servico_id}", response_model=Servico)
def update_servico(
    servico_id: int, 
    servico: ServicoUpdate, 
    db: Session = Depends(get_db)
):
    servico_repository = ServicoRepository(db)
    servico_service = ServicoService(servico_repository)
    db_servico = servico_service.update_servico(servico_id, servico)
    if db_servico is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Servico não encontrado"
        )
    return db_servico

@router.delete("/{servico_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_servico(servico_id: int, db: Session = Depends(get_db)):
    servico_repository = ServicoRepository(db)
    servico_service = ServicoService(servico_repository)
    success = servico_service.delete_servico(servico_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Servico não encontrado"
        )
    
    return JSONResponse(content={"message": "Servico deletado com sucesso"}, status_code=200)