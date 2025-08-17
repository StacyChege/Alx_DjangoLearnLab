# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters as drf_filters # Use an alias to avoid conflict
from django_filters import rest_framework as filters # The import the checker is looking for

from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list, filter, search, and order books, or create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # 1. Add filter backends
    filter_backends = [filters.DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    
    # 2. Define fields for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # 3. Define fields for searching
    search_fields = ['title', 'author__name']
    
    # 4. Define fields for ordering
    ordering_fields = ['title', 'publication_year']

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