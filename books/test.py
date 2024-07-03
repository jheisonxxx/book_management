from django.test import TestCase
from .models import Book

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title='Test Book', author='Test Author', published_date='2022-01-01', genre='Fiction', price=10.00)

    def test_book_creation(self):
        book = Book.objects.get(title='Test Book')
        self.assertEqual(book.author, 'Test Author')

    def test_average_price(self):
        response = self.client.get('/books/average_price/', {'year': '2022'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['average_price'], 10.00)