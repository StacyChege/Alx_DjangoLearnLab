from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Using viewsets for more functionality
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # This permission class allows authenticated users to create/update/delete books,
    # but allows anyone to view the list of books.

    permission_classes = [IsAuthenticatedOrReadOnly]  

