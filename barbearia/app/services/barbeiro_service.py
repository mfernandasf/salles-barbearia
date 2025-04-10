from app.repositories.barbeiro_repository import BarbeiroRepository
from app.schemas.barbeiro import Barbeiro, BarbeiroCreate, BarbeiroUpdate
from app.repositories.horario_barbeiro_repository import HorarioBarbeiroRepository
from app.schemas.horario_barbeiro import HorarioBarbeiro

class BarbeiroService:
    def __init__(self, barbeiro_repository: BarbeiroRepository, horario_barbeiro_repository: HorarioBarbeiroRepository = None):
        self.barbeiro_repository = barbeiro_repository
        self.horario_barbeiro_repository = horario_barbeiro_repository

    def get_barbeiro(self, barbeiro_id: int) -> Barbeiro:
        return self.barbeiro_repository.get_barbeiro(barbeiro_id)

    def get_barbeiros(self, skip: int = 0, limit: int = 100):
        return self.barbeiro_repository.get_barbeiros(skip, limit)

    def get_horarios_por_barbeiro(self, barbeiro_id: int, skip: int = 0, limit: int = 100) -> list[HorarioBarbeiro]:
        return self.horario_barbeiro_repository.get_horarios_por_barbeiro(barbeiro_id, skip, limit)

    def create_barbeiro(self, barbeiro: BarbeiroCreate) -> Barbeiro:
        return self.barbeiro_repository.create_barbeiro(barbeiro)

    def update_barbeiro(self, barbeiro_id: int, barbeiro: BarbeiroUpdate) -> Barbeiro:
        return self.barbeiro_repository.update_barbeiro(barbeiro_id, barbeiro)

    def delete_barbeiro(self, barbeiro_id: int) -> bool:
        return self.barbeiro_repository.delete_barbeiro(barbeiro_id)