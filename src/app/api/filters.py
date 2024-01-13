import django_filters

from src.app.books.models import Book


class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ()
