from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base

class Servico(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(500))
    preco = Column(Float, nullable=False)
    duracao = Column(Integer) 
    imagem_url = Column(String(255))