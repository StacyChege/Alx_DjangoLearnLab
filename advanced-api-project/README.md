# Django API Project with Generic Views

This project demonstrates the use of Django REST Framework's generic views and permissions.

## API Endpoints

- **`GET /api/books/`**: Lists all books.
  - **Permissions**: Anyone can access.

- **`POST /api/books/`**: Creates a new book.
  - **Permissions**: Requires an authenticated user.

- **`GET /api/books/<int:pk>/`**: Retrieves a single book by ID.
  - **Permissions**: Requires an authenticated user.

- **`PUT/PATCH /api/books/<int:pk>/`**: Updates a book by ID.
  - **Permissions**: Requires an authenticated user.

- **`DELETE /api/books/<int:pk>/`**: Deletes a book by ID.
  - **Permissions**: Requires an authenticated user.

## Customizations

- The `BookListCreateView` uses `generics.ListCreateAPIView` to handle both listing and creating books.
- The `BookRetrieveUpdateDestroyView` uses `generics.RetrieveUpdateDestroyAPIView` for a single book's detail, update, and delete operations.
- Permissions are applied using DRF's `IsAuthenticatedOrReadOnly` and `IsAuthenticated` classes, directly controlling access based on user authentication status.



# API Query Capabilities

The `GET /api/books/` endpoint now supports the following query parameters for filtering, searching, and ordering:

* **Filtering**: Use specific field names as query parameters.
    -   Example: `?title=The Great Gatsby&publication_year=1925`
    -   Available fields: `title`, `author__name`, `publication_year`.

* **Searching**: Use the `search` query parameter for a text search.
    -   Example: `?search=harry potter`
    -   Searchable fields: `title`, `author__name`.

* **Ordering**: Use the `ordering` query parameter with a field name to sort the results. Prefix with `-` for descending order.
    -   Example: `?ordering=-publication_year`
    -   Orderable fields: `title`, `publication_year`.