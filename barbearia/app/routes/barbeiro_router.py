from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.barbeiro import Barbeiro, BarbeiroCreate, BarbeiroUpdate
from app.services.barbeiro_service import BarbeiroService
from fastapi import Request
from app.repositories.barbeiro_repository import BarbeiroRepository
from app.repositories.horario_barbeiro_repository import HorarioBarbeiroRepository
from app.database.session import get_db
from fastapi.templating import Jinja2Templates
from app.schemas.horario_barbeiro import HorarioBarbeiro

router = APIRouter()
templates = Jinja2Templates(directory="/app/templates")

@router.get("/", include_in_schema=False)
async def list_barbeiros(request: Request, db: Session = Depends(get_db)):
    barbeiro_repository = BarbeiroRepository(db)
    barbeiro_service = BarbeiroService(barbeiro_repository)
    barbeiros = barbeiro_service.get_barbeiros()
    return barbeiros
    # return templates.TemplateResponse("barbeiros.html", {"request": request, "barbeiros": barbeiros})

@router.get("/", response_model=list[Barbeiro])
def read_barbeiros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    barbeiro_repository = BarbeiroRepository(db)
    barbeiro_service = BarbeiroService(barbeiro_repository)
    return barbeiro_service.get_barbeiros(skip, limit)

@router.get("/{barbeiro_id}", response_model=Barbeiro)
def read_barbeiro(barbeiro_id: int, db: Session = Depends(get_db)):
    barbeiro_repository = BarbeiroRepository(db)
    barbeiro_service = BarbeiroService(barbeiro_repository)
    db_barbeiro = barbeiro_service.get_barbeiro(barbeiro_id)
    if db_barbeiro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Barbeiro não encontrado"
        )
    return db_barbeiro

@router.get("/horarios/{barbeiro_id}", response_model=list[HorarioBarbeiro])
def read_horarios( barbeiro_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db),):
    barbeiro_repository = BarbeiroRepository(db)
    horario_reapository = HorarioBarbeiroRepository(db)
    barbeiro_service = BarbeiroService(barbeiro_repository, horario_reapository)
    return barbeiro_service.get_horarios_por_barbeiro(barbeiro_id, skip, limit)


@router.post("/", response_model=Barbeiro, status_code=status.HTTP_201_CREATED)
def create_barbeiro(barbeiro: BarbeiroCreate, db: Session = Depends(get_db)):
    barbeiro_repository = BarbeiroRepository(db)
    barbeiro_service = BarbeiroService(barbeiro_repository)
    return barbeiro_service.create_barbeiro(barbeiro)

@router.put("/{barbeiro_id}", response_model=Barbeiro)
def update_barbeiro(
    barbeiro_id: int, 
    barbeiro: BarbeiroUpdate, 
    db: Session = Depends(get_db)
):
    barbeiro_repository = BarbeiroRepository(db)
    barbeiro_service = BarbeiroService(barbeiro_repository)
    db_barbeiro = barbeiro_service.update_barbeiro(barbeiro_id, barbeiro)
    if db_barbeiro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Barbeiro não encontrado"
        )
    return db_barbeiro

@router.delete("/{barbeiro_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_barbeiro(barbeiro_id: int, db: Session = Depends(get_db)):
    barbeiro_repository = BarbeiroRepository(db)
    barbeiro_service = BarbeiroService(barbeiro_repository)
    success = barbeiro_service.delete_barbeiro(barbeiro_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Barbeiro não encontrado"
        )
    
    return JSONResponse(content={"message": "Barbeiro deletado com sucesso"}, status_code=200)
    