from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book


@permission_required('bookshelf.can_create_Book', raise_exception=True)
def create_book(request):
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_view_Book', raise_exception=True)
def view_books(request, book_id):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_edit_Book', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete_Book', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return redirect('book_list')

def home(request):
    return HttpResponse("Welcome to the Bookshelf App!")
