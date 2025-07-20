### Update Operation
>>> print(book_to_update.title) # Confirm the updated title
Nineteen Eighty-Four

**Python Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984") # Get the book
book.title = "Nineteen Eighty-Four" 
book.save()
print(book.title)