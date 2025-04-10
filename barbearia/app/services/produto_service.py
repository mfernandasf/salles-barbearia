import os
import shutil
from uuid import uuid4
from fastapi import UploadFile
from app.schemas.produto import ProdutoCreate

from app.repositories.produto_repository import ProdutoRepository
from app.schemas.produto import Produto, ProdutoCreate, ProdutoUpdate

class ProdutoService:
    def __init__(self, produto_repository: ProdutoRepository):
        self.produto_repository = produto_repository

    def salvar_imagem(self, productImage: UploadFile) -> str:
        extension = os.path.splitext(productImage.filename)[-1]

        upload_dir = "assets"
        file_location = os.path.join(upload_dir, f"{uuid4()}.png")

        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(productImage.file, buffer)

        return file_location

    def get_produto(self, produto_id: int) -> Produto:
        return self.produto_repository.get_produto(produto_id)

    def get_produtos(self, skip: int = 0, limit: int = 100) -> list[Produto]:
        return self.produto_repository.get_produtos(skip, limit)

    def create_produto(self, nome: str,
        categoria: str,
        preco: float,
        quantidade_estoque: int,
        desconto: int,
        descricao: str,
        image: UploadFile = None) -> Produto:

        image_path = None
        if image:
            image_path = self.salvar_imagem(image)

        produto = ProdutoCreate(
            nome=nome,
            categoria=categoria,
            preco=preco,
            quantidade_estoque=quantidade_estoque,
            desconto=desconto,
            descricao=descricao,
            image=image_path
        )

        return self.produto_repository.create_produto(produto)

    def update_produto(self, produto_id: int, produto, image: UploadFile) -> Produto:
        if image:
            nome_arquivo = f"{uuid4().hex}_{image.filename}.png"
            caminho = os.path.join("assets", nome_arquivo)
            with open(caminho, "wb") as buffer:
                 shutil.copyfileobj(image.file, buffer)

            produto["image"] = caminho
        
        return self.produto_repository.update_produto(produto_id, produto)

    def delete_produto(self, produto_id: int) -> bool:
        return self.produto_repository.delete_produto(produto_id)  