### Retrieve Operation
1984
>>> print(retrieved_book.author)
George Orwell
>>> print(retrieved_book.publication_year)
1949

**Python Command:**
```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title)
print(retrieved_book.author)
print(retrieved_book.publication_year)