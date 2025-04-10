from app.database.base import engine
from app.database.base import get_db, Base, engine
import app.models  # Isso importa todos os modelos definidos em models/__init__.py

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)