from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # The homepage view
    path('example-form/', views.example_form_view, name='example_form'),
]
