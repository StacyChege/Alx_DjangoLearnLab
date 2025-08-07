from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@permission_required('bookshelf.can_create_Book', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()

        # Basic manual validation
        if not title or not author:
            return HttpResponse("Invalid input", status=400)

        Book.objects.create(title=title, author=author)
        return redirect("book_list")

    return render(request, 'bookshelf/create_book.html')


@permission_required('bookshelf.can_view_Book', raise_exception=True)
def view_books(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/view_books.html', {'book': book})

@permission_required('bookshelf.can_edit_Book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete_Book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')


def home(request):
    return HttpResponse("Welcome to the Bookshelf App!")
