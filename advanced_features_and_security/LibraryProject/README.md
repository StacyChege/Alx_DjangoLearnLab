# LibraryProject

This is my first Django project for the Alx_DjangoLearnLab.

# Permissions & Groups Setup in Bookshelf App

## Custom Permissions
Defined in `Book` model (`bookshelf/models.py`):
- `can_view`: View a book
- `can_create`: Add a new book
- `can_edit`: Edit an existing book
- `can_delete`: Delete a book

## Groups
Created via Django shell and assigned relevant permissions:
- **Viewers**: Assigned `can_view`
- **Editors**: Assigned `can_view`, `can_edit`
- **Admins**: Assigned all permissions: `can_view`, `can_create`, `can_edit`, `can_delete`

## Enforcing Permissions
Views in `views.py` are protected using `@permission_required()` decorators:
- `create_book`: Requires `can_create`
- `edit_book`: Requires `can_edit`
- `delete_book`: Requires `can_delete`
- `view_book`: Requires `can_view`

## Testing Access
You can create test users and assign them to groups using Django shell:
```python
from django.contrib.auth.models import Group
from bookshelf.models import CustomUser

user = CustomUser.objects.create_user(username='...', password='...', email='...', date_of_birth='...')
group = Group.objects.get(name='...')
user.groups.add(group)
