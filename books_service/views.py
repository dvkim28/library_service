from rest_framework import viewsets

from books_service.models import Book
from books_service.serializers import BookSerializer


class BookModelView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
