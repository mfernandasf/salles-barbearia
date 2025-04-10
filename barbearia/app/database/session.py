from sqlalchemy.orm import sessionmaker, Session
from app.database.base import engine

# Cria o sessionmaker com a engine síncrona
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Dependência para FastAPI
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()