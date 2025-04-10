from pydantic import BaseModel
from datetime import time

class HorarioBarbeiroBase(BaseModel):
    dia_semana: str 
    horario_inicio: time
    horario_fim: time

class HorarioBarbeiroCreate(HorarioBarbeiroBase):
    pass

class HorarioBarbeiro(HorarioBarbeiroBase):
    id: int

    class Config:
        orm_mode = True