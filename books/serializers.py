
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    #published_year = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'published_date', 'genre', 'price')
        #Agregar published year

    #def get_published_year(self, obj):
    #    return obj.published_date.year