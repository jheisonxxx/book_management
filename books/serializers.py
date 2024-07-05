
from rest_framework import serializers
from datetime import datetime
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    published_year = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'published_date','published_year', 'genre', 'price')

    def get_published_year(self, obj):
        date = datetime.strptime(str(obj['published_date']),"%Y-%m-%d")
        return str(date.year)
