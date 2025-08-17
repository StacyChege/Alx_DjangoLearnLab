# blog/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Custom views
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
    # Built-in authentication views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),

    # You'll need a home view to show your blog posts later, for now, a placeholder is fine.
    path('', views.register, name='home'),
]