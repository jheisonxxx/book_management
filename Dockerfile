FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]

COPY . .

EXPOSE 8000

# Comando para ejecutar la aplicación
ENTRYPOINT ["sh","/usr/src/app/entrypoint.sh"]
