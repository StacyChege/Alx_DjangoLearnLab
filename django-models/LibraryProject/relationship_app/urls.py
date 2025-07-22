# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, register_view
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'relationship_app' # Namespace for this app's URLs

urlpatterns = [
  # URL for the function-based view (lists all books)
    # Example: /relationship/books/
    path('books/', list_books, name='book_list'),

    # URL for the class-based view (details for a specific library)
    # The <int:pk> captures the primary key from the URL (e.g., /relationship/libraries/1/)
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view - redirects to 'login' after logout
    path('logout/', LogoutView.as_view(next_page='relationship_app:login'), name='logout'),

    # Registration view
    path('register/', register_view, name='register'),
    
]