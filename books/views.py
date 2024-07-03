
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from pymongo import MongoClient
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def average_price_by_year(request, year):
    client = MongoClient('mongo', 27017)
    db = client[settings.DATABASES['default']['NAME']]
    collection = db.book
    pipeline = [
        {'$match': {'published_date': {'$regex': f'^{year}'}}},
        {'$group': {'_id': None, 'average_price': {'$avg': '$price'}}}
    ]
    result = list(collection.aggregate(pipeline))
    average_price = result[0]['average_price'] if result else 0
    return Response({'year': year, 'average_price': average_price})


