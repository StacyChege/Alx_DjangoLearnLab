# Django Blog Authentication System

This project implements a user authentication system using Django's built-in features and custom views.

## Features
- **User Registration:** Handled by a custom view and form.
- **User Login/Logout:** Utilizes Django's built-in views for security and simplicity.
- **User Profile:** A basic profile page accessible only to authenticated users.

## How it Works
- **URL Patterns:**
  - `/register/`: User registration.
  - `/login/`: User login.
  - `/logout/`: User logout.
  - `/profile/`: User profile management.
- **Views:** The `register` and `profile` views are custom, while `login` and `logout` use Django's built-in `auth_views`.
- **Forms:** The `CustomUserCreationForm` extends Django's default `UserCreationForm` to include an email field.
- **Templates:** HTML templates for each view are located in the `blog/templates/blog/` directory.

## Testing
- To test registration, go to `/register/`.
- To test login/logout, go to `/login/` and `/logout/`.
- Try to access `/profile/` without being logged in to verify the `login_required` decorator is working.