from sqlalchemy.orm import Session
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteUpdate
from app.utils.hash import verificar_senha, gerar_hash_senha

class ClienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_cliente(self, cliente_id: int):
        return self.db.query(Cliente).filter(Cliente.id == cliente_id).first()

    def get_clientes(self, skip: int = 0, limit: int = 100):
        return self.db.query(Cliente).offset(skip).limit(limit).all()

    def create_cliente(self, cliente: ClienteCreate):
        cliente.senha = gerar_hash_senha(cliente.senha)
        db_cliente = Cliente(**cliente.dict())
        self.db.add(db_cliente)
        self.db.commit()
        self.db.refresh(db_cliente)
        return db_cliente 

    def update_cliente(self, cliente_id: int, cliente: ClienteUpdate):
        db_cliente = self.get_cliente(cliente_id)
        if not db_cliente:
            return None
        
        update_data = cliente.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_cliente, key, value)
        
        self.db.commit()
        self.db.refresh(db_cliente)
        return db_cliente

    def delete_cliente(self, cliente_id: int):
        db_cliente = self.get_cliente(cliente_id)
        if not db_cliente:
            return False
        
        self.db.delete(db_cliente)
        self.db.commit()
        return True
    
    def autenticar_cliente(self, email: str, senha: str):
        cliente = self.db.query(Cliente).filter(Cliente.email == email).first()
        if not cliente:
            return None
        
        if not verificar_senha(senha, cliente.senha):
            return None
        return cliente