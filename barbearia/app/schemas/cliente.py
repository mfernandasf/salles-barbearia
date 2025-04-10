from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class ClienteBase(BaseModel):
    nome: str
    telefone: str
    email: EmailStr
    data_nascimento: Optional[date] = None
    senha: str
    cpf: str

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None
    data_nascimento: Optional[date] = None
    senha: Optional[str] = None
    cpf: Optional[str] = None

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True