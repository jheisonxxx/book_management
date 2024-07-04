from books.config_mongo import db

books = [
    {"title": "Book One", "author": "Author One", "published_date": "2021-01-01", "genre": "Fiction", "price": 10.99},
    {"title": "Book Two", "author": "Author Two", "published_date": "2022-01-01", "genre": "Non-Fiction", "price": 15.99},
    {"title": "Book Three", "author": "Author Three", "published_date": "2021-01-01", "genre": "Fiction", "price": 8.99},
    {"title": "Book Four", "author": "Author Four", "published_date": "2022-01-01", "genre": "Fiction", "price": 12.99},
    {"title": "Book Five", "author": "Author Five", "published_date": "2021-01-01", "genre": "Non-Fiction", "price": 14.99},
]


db.books.insert_many(books)