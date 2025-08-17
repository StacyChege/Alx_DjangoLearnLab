# api/urls.py
from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    # Endpoint to list all books or create a new book
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    
    # Endpoint to retrieve, update, or delete a single book by its primary key (pk)
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]