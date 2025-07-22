from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model
from django.db.models.signals import post_save # For signals
from django.dispatch import receiver # For signals

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    # ForeignKey: One author can write many books
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"
    class Meta:
        permissions = [
           ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"), 
        ]

class Library(models.Model):
    name = models.CharField(max_length=200)
    # ManyToManyField: A library can have many books, and a book can be in many libraries
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # OneToOneField: One librarian is assigned to one library, and vice-versa
    # related_name is optional but good practice for reverse lookup
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (Librarian of {self.library.name})"

ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
    # Signal to automatically create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Signal to save the UserProfile when the User is saved
# This handles cases where a user might be updated (e.g., in admin)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Ensure the userprofile attribute exists before trying to save it.
    # This prevents errors if for some reason a user is saved before their profile is created (edge cases).
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()