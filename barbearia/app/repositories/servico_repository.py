from sqlalchemy.orm import Session
from app.models.servico import Servico
from app.schemas.servico import ServicoCreate, ServicoUpdate

class ServicoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_servico(self, servico_id: int):
        return self.db.query(Servico).filter(Servico.id == servico_id).first()

    def get_servicos(self, skip: int = 0, limit: int = 100):
        return self.db.query(Servico).offset(skip).limit(limit).all()

    def create_servico(self, servico: ServicoCreate):
        db_servico = Servico(**servico.dict())
        self.db.add(db_servico)
        self.db.commit()
        self.db.refresh(db_servico)
        return db_servico

    def update_servico(self, servico_id: int, servico: ServicoUpdate):
        db_servico = self.get_servico(servico_id) 
        if not db_servico:
            return None
        
        update_data = servico.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_servico, key, value)
        
        self.db.commit()
        self.db.refresh(db_servico) 
        return db_servico

    def delete_servico(self, servico_id: int):
        db_servico = self.get_servico(servico_id)
        if not db_servico:
            return False
        
        self.db.delete(db_servico)
        self.db.commit()
        return True