from django.shortcuts import render

from .models import Book
from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})
