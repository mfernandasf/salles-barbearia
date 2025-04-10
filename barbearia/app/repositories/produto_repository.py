from sqlalchemy.orm import Session
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoUpdate

class ProdutoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_produto(self, produto_id: int):
        return self.db.query(Produto).filter(Produto.id == produto_id).first()

    def get_produtos(self, skip: int = 0, limit: int = 100):
        return self.db.query(Produto).offset(skip).limit(limit).all()

    def create_produto(self, produto: ProdutoCreate):
        db_produto = Produto(**produto.dict())
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def update_produto(self, produto_id: int, produto: ProdutoUpdate):
        db_produto = self.get_produto(produto_id) 
        if not db_produto:
            return None
        
        update_data = produto
        for key, value in update_data.items():
            setattr(db_produto, key, value)
        
        self.db.commit()
        self.db.refresh(db_produto) 
        return db_produto

    def delete_produto(self, produto_id: int):
        db_produto = self.get_produto(produto_id)
        if not db_produto:
            return False
        
        self.db.delete(db_produto)
        self.db.commit()
        return True