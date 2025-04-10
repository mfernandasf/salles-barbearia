# Use uma imagem base oficial do Python
FROM python:3.12-slim

# Instalar dependências necessárias para o psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar o código e instalar as dependências do projeto
WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

# Expôe a porta 8000, caso você esteja usando o FastAPI
EXPOSE 8000

# Comando para rodar o aplicativo
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]