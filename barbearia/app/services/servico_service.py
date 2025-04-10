from app.repositories.servico_repository import ServicoRepository
from app.schemas.servico import Servico, ServicoCreate, ServicoUpdate

class ServicoService:
    def __init__(self, servico_repository: ServicoRepository):
        self.servico_repository = servico_repository

    def get_servico(self, servico_id: int) -> Servico:
        return self.servico_repository.get_servico(servico_id)

    def get_servicos(self, skip: int = 0, limit: int = 100) -> list[Servico]:
        return self.servico_repository.get_servicos(skip, limit)

    def create_servico(self, servico: ServicoCreate) -> Servico:
        return self.servico_repository.create_servico(servico)

    def update_servico(self, servico_id: int, servico: ServicoUpdate) -> Servico:
        return self.servico_repository.update_servico(servico_id, servico)

    def delete_servico(self, servico_id: int) -> bool:
        return self.servico_repository.delete_servico(servico_id)  