# relationship_app/views.py
from django.shortcuts import render, redirect # Import redirect
from django.views.generic import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth.forms import UserCreationForm # For registration form
from django.contrib.auth import login # To automatically log in user after registration
from django.urls import reverse_lazy # For redirects (useful with class-based views)
from django.contrib.auth.decorators import login_required, user_passes_test # Import decorators

from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ---------------- AUTHENTICATION VIEWS ----------------

# Function-based view for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Save the new user
            login(request, user) # Log the user in immediately after registration
            return redirect('relationship_app:book_list') # Redirect to book list page after registration
    else:
        form = UserCreationForm() # Create an empty form for GET requests
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# Helper functions for role-based access control
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@login_required # Ensures user is logged in
@user_passes_test(is_admin, login_url='/relationship/login/') # Only Admin role can access
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required # Ensures user is logged in
@user_passes_test(is_librarian, login_url='/relationship/login/') # Only Librarian role can access
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required # Ensures user is logged in
@user_passes_test(is_member, login_url='/relationship/login/') # Only Member role can access
def member_view(request):
    return render(request, 'relationship_app/member_view.html')