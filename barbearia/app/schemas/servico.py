from pydantic import BaseModel, Field, AnyUrl
from typing import Optional

class ServicoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float 
    duracao: Optional[int] = None
    imagem_url: Optional[AnyUrl] = None
    
class ServicoCreate(ServicoBase):
    pass  # mesmo que ServicoBase, mas pode ser separado se quiser validar criação especificamente

class ServicoUpdate(ServicoBase):
    nome : str = None
    descricao : Optional[str] = None
    preco : float = None
    duracao : Optional[int] = None 
    imagem_url : Optional[AnyUrl] = None

class Servico(ServicoBase):
    id: int

    class Config:
        orm_mode = True
