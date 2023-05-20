from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.app.books.models import Book

from .serializers import BookSerializer


# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
