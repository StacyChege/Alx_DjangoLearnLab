# relationship_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'relationship_app' # Namespace for this app's URLs

urlpatterns = [
  # URL for the function-based view (lists all books)
    # Example: /relationship/books/
    path('books/', views.list_books, name='book_list'),

    # URL for the class-based view (details for a specific library)
    # The <int:pk> captures the primary key from the URL (e.g., /relationship/libraries/1/)
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view - redirects to 'login' after logout
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html', next_page='relationship_app:login'), name='logout'),

    # Registration view
    path('register/', views.register, name='register'),

    # New URLs for Role-Based Access Control (Task 3)
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),

    # New URLs for Book CRUD with Permissions (Task 4)
    # Modified URLs for Book CRUD with Permissions (Task 4) to match checker's expectation
    path('add_book/', views.book_create, name='book_add'),
    path('edit_book/<int:pk>/', views.book_update, name='book_edit'),
    path('delete_book/<int:pk>/', views.book_delete, name='book_delete'),
    
]