from sqlalchemy import Column, Integer, String, Time
from sqlalchemy.orm import relationship
from app.database.base import Base

class Barbeiro(Base):
  __tablename__ = "barbeiros"

  id = Column(Integer, primary_key = True, index=True)
  nome = Column(String(100), nullable=False)
  telefone = Column(String(20), nullable=False)
  especialidade = Column(String(100))
  
  horarios = relationship("HorarioBarbeiro", back_populates="barbeiro", cascade="all, delete-orphan")