from sqlalchemy.orm import Session
from app.models.agendamento import Agendamento
from app.schemas.agendamento import AgendamentoCreate, AgendamentoUpdate

class AgendamentoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_agendamento(self, agendamento_id: int):
        return self.db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()

    def get_agendamentos(self, skip: int = 0, limit: int = 100):
        return self.db.query(Agendamento).offset(skip).limit(limit).all()
    
    def get_agendamento_por_cliente(self, cliente_id: int):
        return self.db.query(Agendamento).filter(Agendamento.cliente_id == cliente_id).all()

    def create_agendamento(self, agendamento: AgendamentoCreate):
        db_agendamento = Agendamento(**agendamento.dict())
        self.db.add(db_agendamento)
        self.db.commit()
        self.db.refresh(db_agendamento)
        return db_agendamento

    def update_agendamento(self, agendamento_id: int, agendamento: AgendamentoUpdate):
        db_agendamento = self.get_agendamento(agendamento_id)
        if not db_agendamento:
            return None
        
        update_data = agendamento.dict(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(db_agendamento, key, value)
        
        self.db.commit()
        self.db.refresh(db_agendamento)
        return db_agendamento

    def delete_agendamento(self, agendamento_id: int):
        db_agendamento = self.get_agendamento(agendamento_id)
        if not db_agendamento:
            return False
        
        self.db.delete(db_agendamento)
        self.db.commit()
        return True