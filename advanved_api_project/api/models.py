from django.db import models

# Create your models here.
# api/models.py
from django.db import models

class Author(models.Model):
    """
    Model representing an author. 
    It contains a basic name field for identification.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book. 
    It includes the title, publication year, and a foreign key 
    to link it to a specific author. This creates a one-to-many 
    relationship where one author can have many books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
