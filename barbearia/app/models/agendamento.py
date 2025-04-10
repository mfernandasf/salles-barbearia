from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, nullable=False)
    servico = Column(String(100), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    
    # cliente = relationship("Cliente", back_populates="agendamentos") 