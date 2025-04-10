from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AgendamentoBase(BaseModel):
    data_hora: datetime
    servico: str
    cliente_id: int

class AgendamentoCreate(AgendamentoBase):
    pass

class AgendamentoUpdate(BaseModel):
    data_hora: Optional[datetime] = None
    servico: Optional[str] = None
    cliente_id: Optional[int] = None  

class Agendamento(AgendamentoBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True