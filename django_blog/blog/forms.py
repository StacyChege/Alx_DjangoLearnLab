# django_blog/blog/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

# This is your registration form from Step 1
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

# Add this new form for profile editing
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')