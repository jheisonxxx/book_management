from django.test import TestCase
from settings import db

class BookTestCase(TestCase):
    def setUp(self):
        book ={"title": "Test Book", "author": "Test Author", "published_date": "2022-01-01", "genre": "Fiction",
             "price": 10.00}
        db.books.insert_one(book)

    def test_book_creation(self):
        book = {"title": "Test Book", "author": "Test Author", "published_date": "2022-01-01", "genre": "Fiction",
             "price": 10.00}
        db.books.insert_one(book)
        self.assertEqual(book.author, 'Test Author')

    def test_average_price(self):
        response = self.client.get('/books/average_price/', {'year': '2022'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['average_price'], 10.00)