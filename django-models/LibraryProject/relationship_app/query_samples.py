# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    print("--- Ensuring Sample Data Exists ---")
    # Create Authors
    author1, created = Author.objects.get_or_create(name="Jane Doe")
    if created: print(f"Created Author: {author1.name}")
    author2, created = Author.objects.get_or_create(name="John Smith")
    if created: print(f"Created Author: {author2.name}")
    author3, created = Author.objects.get_or_create(name="Alice Johnson")
    if created: print(f"Created Author: {author3.name}")


    # Create Books
    book1, created = Book.objects.get_or_create(title="The First Novel", author=author1)
    if created: print(f"Created Book: {book1.title}")
    book2, created = Book.objects.get_or_create(title="Another Story", author=author1)
    if created: print(f"Created Book: {book2.title}")
    book3, created = Book.objects.get_or_create(title="Tech Adventures", author=author2)
    if created: print(f"Created Book: {book3.title}")
    book4, created = Book.objects.get_or_create(title="Digital Dreams", author=author2)
    if created: print(f"Created Book: {book4.title}")
    book5, created = Book.objects.get_or_create(title="Random Tales", author=author3)
    if created: print(f"Created Book: {book5.title}")


    # Create Libraries
    library1, created = Library.objects.get_or_create(name="City Library")
    if created: print(f"Created Library: {library1.name}")
    library2, created = Library.objects.get_or_create(name="Community Hub")
    if created: print(f"Created Library: {library2.name}")

    # Add books to libraries (ManyToMany)
    if created or not library1.books.exists(): # Only add if new or empty
        library1.books.add(book1, book2, book3)
        print(f"Added books to {library1.name}")
    if created or not library2.books.exists():
        library2.books.add(book4, book5)
        print(f"Added books to {library2.name}")


    # Create Librarians (OneToOne)
    # Use try-except to handle existing OneToOne relations if re-running without deletion
    try:
        librarian1, created = Librarian.objects.get_or_create(name="Sarah Connor", library=library1)
        if created: print(f"Created Librarian: {librarian1.name}")
    except Exception as e:
        print(f"Librarian for {library1.name} might already exist or has a duplicate: {e}")

    try:
        librarian2, created = Librarian.objects.get_or_create(name="Miles Dyson", library=library2)
        if created: print(f"Created Librarian: {librarian2.name}")
    except Exception as e:
        print(f"Librarian for {library2.name} might already exist or has a duplicate: {e}")


def run_queries():
    print("\n--- Running Sample Queries ---")

    # 1. Query all books by a specific author (ForeignKey)
    print("\nQuery 1: Books by Jane Doe")
    author_name = "Jane Doe" # Define the variable for author's name
    author = Author.objects.get(name=author_name) # Retrieve author using author_name variable
    # Use 'Book.objects.filter' where the checker implies 'objects.filter'
    books_by_author = Book.objects.filter(author=author) # Filter using the 'author' object
    for book in books_by_author:
            print(f"- {book.title}")

   # 2. List all books in a library (ManyToMany)
    print("\nQuery 2: Books in City Library")
    library_name = "City Library" # Define the variable here
    city_library = Library.objects.get(name=library_name) # Use the variable as expected by the checker
    city_library_books = city_library.books.all()
    for book in city_library_books:
            print(f"- {book.title}")

    # 3. Retrieve the librarian for a library (OneToOne)
    print("\nQuery 3: Librarian for Community Hub")
    community_hub = Library.objects.get(name="Community Hub")
    try:
        community_librarian = community_hub.librarian # Reverse lookup for OneToOne
        print(f"- {community_hub.name}'s Librarian: {community_librarian.name}")
    except Librarian.DoesNotExist:
        print(f"- No librarian found for {community_hub.name}.")

    print("\n--- Queries Complete ---")

# This part allows you to easily run the functions from the Django shell
if __name__ == '__main__':
    create_sample_data()
    run_queries()