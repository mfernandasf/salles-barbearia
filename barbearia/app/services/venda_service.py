from app.repositories.venda_repository import VendaRepository
from app.schemas.venda import Venda, VendaCreate, VendaUpdate

class VendaService:
    def __init__(self, venda_repository: VendaRepository):
        self.venda_repository = venda_repository

    def get_venda(self, venda_id: int) -> Venda:
        return self.venda_repository.get_venda(venda_id)
    
    def get_vendas(self, skip: int = 0, limit: int = 100) -> list[Venda]:
        return self.venda_repository.get_vendas(skip, limit)

    def create_venda(self, venda: VendaCreate) -> Venda:
        return self.venda_repository.create_venda(venda)

    def update_venda(self, venda_id: int, venda: VendaUpdate) -> Venda:
        return self.venda_repository.update_venda(venda_id, venda)

    def delete_venda(self, venda_id: int) -> bool:
        return self.venda_repository.delete_venda(venda_id)