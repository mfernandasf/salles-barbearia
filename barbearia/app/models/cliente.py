from sqlalchemy import Column, Integer, String, Date
from app.database.base import Base

class Cliente(Base):
  __tablename__ = "clientes"

  id = Column(Integer, primary_key = True, index=True)
  nome = Column(String(100), nullable=False)
  telefone = Column(String(20), nullable=False)
  email = Column(String(100), unique=True, nullable=False)
  data_nascimento = Column(Date)
  senha = Column(String(100), nullable=False)
  cpf = Column(String(20), unique=True,nullable=False)