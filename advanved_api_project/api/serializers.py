# api/serializers.py
from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    A serializer for the Book model.
    It serializes all fields of the Book model.
    Includes custom validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation to check that the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    A serializer for the Author model.
    It includes the name field and a nested BookSerializer to handle
    the books associated with the author. The nested serialization allows
    the Author data to be represented with all their related books in a single API response.
    The 'books' field is read-only to prevent it from being modified directly
    when creating or updating an author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']