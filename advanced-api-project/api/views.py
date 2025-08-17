# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Book
from .serializers import BookSerializer

# This corresponds to "ListView" and "CreateView"
class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list all books and create a new book.
    GET request: list all books.
    POST request: create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# This corresponds to "DetailView", "UpdateView", and "DeleteView"
class BookDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateAPIView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteAPIView(generics.DestroyAPIView):
    """
    API view to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]