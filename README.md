# Book Management System

This project is a book management system that provides a REST API for performing CRUD operations on a MongoDB database using Django and Django Rest Framework. It also implements a MongoDB aggregation pipeline to get the average price of books published in a specific year.

## Requirements

- Docker
- Docker Compose

## Setup

1. Clone this repository or download the zip file and extract it.

    ```bash
    git clone https://github.com/jheisonxxx/book_management.git
    cd book_management
    ```

2. Build and run the Docker containers.

    ```bash
    docker-compose up --build
    ```

    This command will perform the following actions:
    - Build the Docker image for the Django application.
    - Start the Django server on port 8000.

## Endpoints

The API will be available at `http://localhost:8000`.

### CRUD for Books

- **GET** `/api/books/`: List all books.
- **POST** `/api/books/`: Create a new book.
- **GET** `/api/books/{id}/`: Get details of a specific book.
- **PUT** `/api/books/{id}/`: Update a specific book.
- **DELETE** `/api/books/{id}/`: Delete a specific book.

### MongoDB Aggregation

- **GET** `/api/books/average_price/{year}/`: Get the average price of books published in a specific year.

### Authentication

- **POST** `/api/token/`: Obtain a JWT access token.
- **POST** `/api/token/refresh/`: Refresh the JWT access token.

## Pagination

The API is configured to support pagination. You can use the `page` and `page_size` parameters in requests to control pagination.

## Testing

To run the unit tests, use the following command:

```bash