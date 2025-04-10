from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255))
    preco = Column(Float, nullable=False)
    quantidade_estoque = Column(Integer, nullable=False)
    desconto = Column(Float)
    categoria = Column(String(20), nullable=False)
    image = Column(String(100))