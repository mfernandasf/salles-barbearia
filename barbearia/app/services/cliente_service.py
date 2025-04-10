from app.repositories.cliente_repository import ClienteRepository
from app.schemas.cliente import Cliente, ClienteCreate, ClienteUpdate

class ClienteService:
    def __init__(self, cliente_repository: ClienteRepository):
        self.cliente_repository = cliente_repository

    def get_cliente(self, cliente_id: int) -> Cliente:
        return self.cliente_repository.get_cliente(cliente_id)

    def get_clientes(self, skip: int = 0, limit: int = 100) -> list[Cliente]:
        return self.cliente_repository.get_clientes(skip, limit)

    def create_cliente(self, cliente: ClienteCreate) -> Cliente:
        return self.cliente_repository.create_cliente(cliente)

    def update_cliente(self, cliente_id: int, cliente: ClienteUpdate) -> Cliente:
        return self.cliente_repository.update_cliente(cliente_id, cliente)

    def delete_cliente(self, cliente_id: int) -> bool:
        return self.cliente_repository.delete_cliente(cliente_id)