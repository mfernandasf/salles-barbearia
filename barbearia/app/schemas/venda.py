from pydantic import BaseModel
from datetime import date
from typing import Optional

class VendaBase(BaseModel):
    data: Optional[date]
    qtd_comprada: int
    cliente_id: int
    produto_id: int

class VendaCreate(VendaBase):
    pass

class Venda(VendaBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True

class VendaUpdate(BaseModel):
    data: Optional[date] = None
    qtd_comprada: Optional[int] = None
    cliente_id: Optional[int] = None
    produto_id: Optional[int] = None

