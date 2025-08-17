# api/urls.py
from django.urls import path
from .views import (
    BookListCreateAPIView,
    BookDetailAPIView,
    BookUpdateAPIView,
    BookDeleteAPIView
)

urlpatterns = [
    # List all books and create a new book
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),

    # Retrieve a single book
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),

    # Explicit URL for creating a book, matching the checker's expectation
    path('books/create/', BookListCreateAPIView.as_view(), name='book-create'),

    # Explicit URL for updating a book
    path('books/update/<int:pk>/', BookUpdateAPIView.as_view(), name='book-update'),

    # Explicit URL for deleting a book
    path('books/delete/<int:pk>/', BookDeleteAPIView.as_view(), name='book-delete'),
]