from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from bson import ObjectId
from .config_mongo import db
import logging

class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            paginator = PageNumberPagination()
            books = list(db.books.find())
            for book in books:
                book['_id'] = str(book['_id'])  # Convert ObjectId to string
            result_page = paginator.paginate_queryset(books, request)
            serializer = BookSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({"error": f"Error fetching book list: {str(e)}"}, status=500)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            db.books.insert_one(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=500)

    def retrieve(self, request, pk=None):
        book = db.books.find_one({"_id": ObjectId(pk)})
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = BookSerializer(existing_book, data=request.data, partial=True)
        if serializer.is_valid():
            db.books.update_one({"_id": ObjectId(pk)}, {"$set": serializer.data})
            return Response(serializer.data)
        return Response(serializer.errors, status=500)

    def destroy(self, request, pk=None):
        db.books.delete_one({"_id": ObjectId(pk)})
        return Response(status=204)

@api_view(['GET'])
def average_price_by_year(request, year):
    collection = db.books
    pipeline = [
        {'$match': {'published_date': {'$regex': f'^{year}'}}},
        {'$group': {'_id': None, 'average_price': {'$avg': '$price'}}}
    ]
    result = list(collection.aggregate(pipeline))
    average_price = result[0]['average_price'] if result else 0
    return Response({'year': year, 'average_price': average_price})
