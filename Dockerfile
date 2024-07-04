FROM python:3.9-slim

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

ENV PYTHONPATH=/usr/src/app

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]

COPY . .

EXPOSE 8000

# Comando para ejecutar la aplicación
ENTRYPOINT ["sh","/usr/src/app/entrypoint.sh"]
