# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView


app_name = 'relationship_app' # Namespace for this app's URLs

urlpatterns = [
    # URL for the function-based view (lists all books)
    # Example: /relationship/books/
    path('books/', views.book_list_view, name='book_list'),

    # URL for the class-based view (details for a specific library)
    # The <int:pk> captures the primary key from the URL (e.g., /relationship/libraries/1/)
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]