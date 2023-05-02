# Escolha uma imagem de base adequada para suas aplicações
FROM python:3.11-slim

# Instale as dependências do sistema necessárias para as aplicações
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Crie um diretório para suas aplicações e copie os arquivos do projeto
WORKDIR /app
COPY . /app

# Instale as dependências do Python usando Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

# Defina as variáveis de ambiente necessárias para cada aplicação
ENV APP_1_PORT=8000
ENV APP_2_PORT=8001

# Inicie as aplicações usando o Poetry run
CMD poetry run uvicorn app1.main:app --host 0.0.0.0 --port $APP_1_PORT & poetry run uvicorn app2.main:app --host 0.0.0.0 --port $APP_2_PORT
