### Delete Operation
>>> # Confirm deletion by trying to retrieve all books        
>>> all_books = Book.objects.all()
>>> print(all_books)
<QuerySet []>

**Python Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four") # Get the book
book.delete() 
all_books = Book.objects.all()
print(all_books)