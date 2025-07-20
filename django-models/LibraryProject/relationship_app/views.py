from django.shortcuts import render
from django.views.generic import DetailView 
from .models import Book, Library


# Create your views here.

# Function-based view to list all books
def book_list_view(request):
    books = Book.objects.all() # Retrieve all books from the database
    context = {
        'books': books
    }
    # Render the 'list_books.html' template, passing the books data
    return render(request, 'list_books.html', context)

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library # Specify the model this view will work with
    template_name = 'library_detail.html' # Specify the template to render
    context_object_name = 'library' # The variable name to use in the template (e.g., {{ library.name }})
    # For DetailView, Django automatically looks for an object using the 'pk' (primary key)
    # from the URL pattern.
