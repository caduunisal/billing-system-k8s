FROM python:3.11-slim

WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta da API Flask
EXPOSE 5000

# Comando de inicialização
CMD ["python", "app.py"]

