from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from library.models.book import Book
from library.serializers.book import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
