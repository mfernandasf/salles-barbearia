from sqlalchemy.orm import Session, joinedload
from app.models.barbeiro import Barbeiro
from app.models.horario_barbeiro import HorarioBarbeiro
from app.schemas.barbeiro import BarbeiroCreate, BarbeiroUpdate

class BarbeiroRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_barbeiro(self, barbeiro_data: BarbeiroCreate) -> Barbeiro:
        barbeiro = Barbeiro(
            nome=barbeiro_data.nome,
            especialidade=barbeiro_data.especialidade,
            telefone=barbeiro_data.telefone
        ) 

        self.db.add(barbeiro)
        self.db.flush()  
        
        for horario in barbeiro_data.horarios:
            horario_model = HorarioBarbeiro(
                barbeiro_id=barbeiro.id,
                dia_semana=horario.dia_semana,
                horario_inicio=horario.horario_inicio,
                horario_fim=horario.horario_fim
            )
            self.db.add(horario_model)

        self.db.commit()
        self.db.refresh(barbeiro)
        return barbeiro


 

    def get_barbeiros(self, skip: int = 0, limit: int = 100):
        return  (
            self.db.query(Barbeiro)
            .options(joinedload(Barbeiro.horarios))
            .offset(skip)
            .limit(limit)
            .all()
        
        )
    def get_barbeiro(self, barbeiro_id: int):
        return self.db.query(Barbeiro).filter(Barbeiro.id == barbeiro_id).first()


    
    def update_barbeiro(self, barbeiro_id: int, barbeiro: BarbeiroUpdate):
        db_barbeiro = self.get_barbeiro(barbeiro_id)
        
        if not db_barbeiro:
            return None

        if barbeiro.nome is not None:
            db_barbeiro.nome = barbeiro.nome
        if barbeiro.especialidade is not None:
            db_barbeiro.especialidade = barbeiro.especialidade
        if barbeiro.telefone is not None:
            db_barbeiro.telefone = barbeiro.telefone

        if barbeiro.horarios is not None:
            self.db.query(HorarioBarbeiro).filter(HorarioBarbeiro.barbeiro_id == db_barbeiro.id).delete()

            for horario in barbeiro.horarios:
                novo_horario = HorarioBarbeiro(
                    barbeiro_id=db_barbeiro.id,
                    dia_semana=horario.dia_semana,
                    horario_inicio=horario.horario_inicio,
                    horario_fim=horario.horario_fim
                )
                self.db.add(novo_horario)

        self.db.commit()
        self.db.refresh(db_barbeiro)
        return db_barbeiro

    def delete_barbeiro(self, barbeiro_id: int):
        db_barbeiro = self.get_barbeiro(barbeiro_id)
        
        if not db_barbeiro:        
            return False
        
        self.db.delete(db_barbeiro)
        self.db.commit()
        return True
    