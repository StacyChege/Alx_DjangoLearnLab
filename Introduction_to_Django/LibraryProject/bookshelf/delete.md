### Delete Operation
>>> # Confirm deletion by trying to retrieve all books        
>>> all_books = Book.objects.all()
>>> print(all_books)
<QuerySet []>

**Python Command:**
```python
from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

all_books = Book.objects.all()
print(all_books)