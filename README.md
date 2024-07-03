# Book Management System

Este proyecto es un sistema de gestión de libros que proporciona una API REST para realizar operaciones CRUD en la base de datos MongoDB utilizando Django y Django Rest Framework. Además, implementa un pipeline de agregación de MongoDB para obtener el precio promedio de los libros publicados en un año específico.

## Requisitos

- Docker
- Docker Compose

## Configuración

1. Clona este repositorio o descarga el archivo zip y extráelo.

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd book_management
    ```

2. Construye y ejecuta los contenedores Docker.

    ```bash
    docker-compose up --build
    ```

    Este comando realizará las siguientes acciones:
    - Construirá la imagen de Docker para la aplicación Django.
    - Ejecutará las migraciones de la base de datos.
    - Sembrará la base de datos con datos de prueba iniciales.
    - Iniciará el servidor Django en el puerto 8000.

## Endpoints

La API estará disponible en `http://localhost:8000`.

### CRUD de Libros

- **GET** `/api/books/`: Lista todos los libros.
- **POST** `/api/books/`: Crea un nuevo libro.
- **GET** `/api/books/{id}/`: Obtiene los detalles de un libro específico.
- **PUT** `/api/books/{id}/`: Actualiza un libro específico.
- **DELETE** `/api/books/{id}/`: Elimina un libro específico.

### Agregación de MongoDB

- **GET** `/api/books/average_price/{year}/`: Obtiene el precio promedio de los libros publicados en un año específico.

### Autenticación

- **POST** `/api/token/`: Obtiene un token de acceso JWT.
- **POST** `/api/token/refresh/`: Refresca el token de acceso JWT.

## Paginación

La API está configurada para soportar paginación. Puedes utilizar los parámetros `page` y `page_size` en las solicitudes para controlar la paginación.

## Pruebas

Para ejecutar las pruebas unitarias, utiliza el siguiente comando:

```bash
docker-compose run web python manage.py test
docker-compose run --rm web python manage.py runserver
docker-compose run --rm web python manage.py makemigrations
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py loaddata books/fixtures/books.json
docker-compose run --rm web python manage.py createsuperuser
docker-compose run --rm web pip install -r requirements.txt
