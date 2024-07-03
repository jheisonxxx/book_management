import json
from django.core.management import BaseCommand
from your_app_name.models import Book

class Command(BaseCommand):
    help = 'Load initial data from JSON file'

    def handle(self, *args, **kwargs):
        with open('books.json', 'r') as file:
            books = json.load(file)
            for book in books:
                fields = book['fields']
                Book.objects.update_or_create(
                    id=book['pk'],
                    defaults={
                        'title': fields['title'],
                        'author': fields['author'],
                        'published_date': fields['published_date'],
                        'genre': fields['genre'],
                        'price': fields['price'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded books data'))