
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, average_price_by_year


router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/average_price/<int:year>/', average_price_by_year),
]
