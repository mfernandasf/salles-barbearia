from sqlalchemy.orm import Session
from app.models.venda import Venda
from app.schemas.venda import VendaCreate, VendaUpdate
from app.models.produto import Produto

class VendaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_venda(self, venda_id: int):
        return self.db.query(Venda).filter(Venda.id == venda_id).first()

    def get_vendas(self, skip: int = 0, limit: int = 100):
        return self.db.query(Venda).offset(skip).limit(limit).all()
    
    def get_venda_por_cliente(self, cliente_id: int):
        return self.db.query(Venda).filter(Venda.cliente_id == cliente_id).all()

    def create_venda(self, venda: VendaCreate):
        db_venda = Venda(**venda.dict())

        self.db.add(db_venda)

        db_produto = self.db.query(Produto).filter(Produto.id == db_venda.produto_id).first()

        if not db_produto:
            return None
        
        if db_produto.quantidade_estoque <= 0:
            return None
        
        setattr(db_produto, "quantidade_estoque", db_produto.quantidade_estoque - db_venda.qtd_comprada)

        self.db.commit()
        self.db.refresh(db_venda)
        return db_venda

    # Update talvez não seja usado mas criei por padrão
    def update_venda(self, venda_id: int, venda: VendaUpdate):
        db_venda = self.get_venda(venda_id)
        if not db_venda:
            return None
        
        update_data = venda.dict(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(db_venda, key, value)
        
        self.db.commit()
        self.db.refresh(db_venda)
        return db_venda

    def delete_venda(self, venda_id: int):
        db_venda = self.get_venda(venda_id)
        if not db_venda:
            return False
        
        self.db.delete(db_venda)
        self.db.commit()
        return True