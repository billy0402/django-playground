import json

from django.forms import model_to_dict
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotAllowed,
    JsonResponse,
)
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from app.books.forms import BookForm
from app.books.models import Book


# Create your views here.
def parse_request(request: HttpRequest) -> None:
    if request.method == 'GET':
        request.data = dict(request.GET)
        return None

    request.data = json.loads(request.body.decode('utf-8'))


@csrf_exempt
def index(request: HttpRequest) -> HttpResponse:
    parse_request(request)
    if request.method == 'GET':
        return list_all(request)

    if request.method == 'POST':
        return add(request)

    return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def detail(request: HttpRequest, book_id: str) -> HttpResponse:
    parse_request(request)
    if request.method == 'GET':
        return show(request, book_id)

    if request.method == 'PUT' or request.method == 'PATCH':
        return edit(request, book_id)

    if request.method == 'DELETE':
        return delete(request, book_id)

    return HttpResponseNotAllowed(['GET', 'PUT', 'PATCH', 'DELETE'])


def list_all(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return JsonResponse([model_to_dict(book) for book in books], safe=False)


def show(request: HttpRequest, book_id: str) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    return JsonResponse(model_to_dict(book))


def add(request: HttpRequest) -> HttpResponse:
    form = BookForm(request.data)
    if form.is_valid():
        book = form.save()
        return JsonResponse(model_to_dict(book))

    return JsonResponse(form.errors.get_json_data(), status=400)


def edit(request: HttpRequest, book_id: str) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    form = BookForm(request.data, instance=book)
    if form.is_valid():
        form.save()
        return JsonResponse(model_to_dict(book))

    return JsonResponse(form.errors.get_json_data(), status=400)


def delete(request: HttpRequest, book_id: str) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return JsonResponse({})
