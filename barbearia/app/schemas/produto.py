from pydantic import BaseModel
from typing import Optional

class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    quantidade_estoque: int
    desconto: Optional[float] = None
    categoria : str
    image: str | None = None

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None 
    preco: Optional[float] = None
    quantidade_estoque: Optional[int] = None 
    desconto: Optional[float] = None
    categoria : Optional[str] = None
    image: Optional[str] = None

class Produto(ProdutoBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True