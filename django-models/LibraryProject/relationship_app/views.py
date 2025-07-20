# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView # For class-based view
from .models import  Library # <--- ENSURE THIS LINE IS EXACTLY AS SHOWN (importing Library)

# Function-based view to list all books
def book_list_view(request):
    books = Book.objects.all() # Retrieve all books from the database
    context = {
        'books': books
    }
    # Render the 'relationship_app/list_books.html' template, passing the books data
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library # Specify the model this view will work with
    template_name = 'relationship_app/library_detail.html' # <--- CHANGE THIS LINE
    context_object_name = 'library' # The variable name to use in the template (e.g., {{ library.name }})