from app.repositories.agendamento_repository import AgendamentoRepository
from app.schemas.agendamento import Agendamento, AgendamentoCreate, AgendamentoUpdate

class AgendamentoService:
    def __init__(self, agendamento_repository: AgendamentoRepository):
        self.agendamento_repository = agendamento_repository

    def get_agendamento(self, agendamento_id: int) -> Agendamento:
        return self.agendamento_repository.get_agendamento(agendamento_id)
    
    def get_agendamento_por_cliente(self, cliente_id: int) -> Agendamento:
        return self.agendamento_repository.get_agendamento_por_cliente(cliente_id)
    def get_agendamentos(self, skip: int = 0, limit: int = 100) -> list[Agendamento]:
        return self.agendamento_repository.get_agendamentos(skip, limit)

    def create_agendamento(self, agendamento: AgendamentoCreate) -> Agendamento:
        return self.agendamento_repository.create_agendamento(agendamento)

    def update_agendamento(self, agendamento_id: int, agendamento: AgendamentoUpdate) -> Agendamento:
        return self.agendamento_repository.update_agendamento(agendamento_id, agendamento)

    def delete_agendamento(self, agendamento_id: int) -> bool:
        return self.agendamento_repository.delete_agendamento(agendamento_id) 