from pydantic import BaseModel
from typing import List, Optional
from app.schemas.horario_barbeiro import HorarioBarbeiro, HorarioBarbeiroCreate

class BarbeiroBase(BaseModel):
    nome: str
    especialidade: Optional[str] = None
    telefone: Optional[str]

class BarbeiroCreate(BarbeiroBase):
    horarios: List[HorarioBarbeiroCreate]

class BarbeiroUpdate(BaseModel):
    nome: Optional[str] = None
    especialidade: Optional[str] = None
    telefone: Optional[str] = None

    horarios: Optional[List[HorarioBarbeiroCreate]] = None

class Barbeiro(BarbeiroBase):
    id: int
    horarios: List[HorarioBarbeiro] = []

    class Config:
        orm_mode = True