# relationship_app/forms.py
from django import forms
from .models import Book, Author, Library # Import necessary models

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # Specify the fields you want to include in the form
        # You might need to adjust this based on the actual fields in your Book model
        fields = ['__all__'] # Add other fields like 'publication_date' if they exist in your Book model

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name', 'books'] # Or specific fields you want to allow editing for library

# You can add more forms here for other models as needed