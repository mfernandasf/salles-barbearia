from sqlalchemy import Column, Integer, Time, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class HorarioBarbeiro(Base):
    __tablename__ = "horarios_barbeiro"

    id = Column(Integer, primary_key=True)
    barbeiro_id = Column(Integer, ForeignKey("barbeiros.id"), nullable=False)
    dia_semana = Column(String(25), nullable=False) 
    horario_inicio = Column(Time, nullable=False)
    horario_fim = Column(Time, nullable=False)

    barbeiro = relationship("Barbeiro", back_populates="horarios")