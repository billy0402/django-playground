from rest_framework.viewsets import ModelViewSet

from src.app.books.models import Author, Book, Classification, Publisher, Tag

from .serializers import (
    AuthorSerializer, BookSerializer, ClassificationSerializer,
    PublisherSerializer, TagSerializer
)


# Create your views here.
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class ClassificationViewSet(ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
