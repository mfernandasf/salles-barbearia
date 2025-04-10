from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models import Cliente
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.login import LoginSchema
from app.utils.hash import verificar_senha
from app.auth.auth import criar_token
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.repositories.cliente_repository import ClienteRepository
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


router = APIRouter()

def get_usuario_logado(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return email
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

@router.post("/login")
def login(dados: LoginSchema, db: Session = Depends(get_db)):
    cliente_repository = ClienteRepository(db)

    cliente = cliente_repository.autenticar_cliente( email=dados.email, senha=dados.senha)
    
    if not cliente:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")

    token = criar_token({"sub": str(cliente.id)})
    return {"access_token": token, "token_type": "bearer"}