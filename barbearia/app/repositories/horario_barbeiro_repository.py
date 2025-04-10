from sqlalchemy.orm import Session
from app.models.horario_barbeiro import HorarioBarbeiro

class HorarioBarbeiroRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_horarios_por_barbeiro(self, barbeiro_id: int, skip: int = 0, limit: int = 100):
        return self.db.query(HorarioBarbeiro).filter(HorarioBarbeiro.barbeiro_id == barbeiro_id).offset(skip).limit(limit).all()