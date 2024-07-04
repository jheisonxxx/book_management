
# Utiliza una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos y el código fuente
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Switch to root to set execute permission

COPY . .

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]
