from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from src.utils.forms import DeleteConfirmForm

from .forms import BookForm
from .models import Book


# Create your views here.
# @login_required
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


# @login_required
def show(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/show.html', {'book': book})


@permission_required('books.add_book', raise_exception=True)
def add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('books:index')

    return render(request, 'books/add.html', {'form': form})


@permission_required('books.edit_book', raise_exception=True)
def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, '更新成功')
        return redirect('books:index')

    return render(request, 'books/edit.html', {'form': form})


@permission_required('books.delete_book', raise_exception=True)
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        book.delete()
        messages.success(request, '刪除成功')
        return redirect('books:index')

    return render(request, 'books/delete.html', {'form': form})
