# api/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Author, Book
from .serializers import BookSerializer

class BookAPITests(APITestCase):
    
    def setUp(self):
        """
        Set up the test environment by creating a user, an author, and a book.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='J.K. Rowling')
        self.book = Book.objects.create(
            title='Harry Potter and the Sorcerer\'s Stone',
            publication_year=1997,
            author=self.author
        )
        self.url_list_create = reverse('book-list')
        self.url_detail = reverse('book-detail', args=[self.book.pk])
        self.url_update = reverse('book-update', args=[self.book.pk])
        self.url_delete = reverse('book-delete', args=[self.book.pk])

    def test_list_books(self):
        """
        Test that an unauthenticated user can list all books.
        """
        response = self.client.get(self.url_list_create)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_create_book_authenticated(self):
        """
        Test that an authenticated user can create a new book.
        """
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'The Lord of the Rings',
            'publication_year': 1954,
            'author': self.author.pk
        }
        response = self.client.post(self.url_list_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
    
    def test_create_book_unauthenticated(self):
        """
        Test that an unauthenticated user cannot create a new book.
        """
        data = {
            'title': 'The Hobbit',
            'publication_year': 1937,
            'author': self.author.pk
        }
        response = self.client.post(self.url_list_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 1)

    def test_update_book_authenticated(self):
        """
        Test that an authenticated user can update a book.
        """
        self.client.login(username='testuser', password='testpassword')
        # Add the 'author' field with the primary key
        updated_data = {
            'title': 'Updated Title', 
            'publication_year': 1999,
            'author': self.author.pk  # Corrected line
        }
        response = self.client.put(self.url_update, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')
        
    def test_update_book_unauthenticated(self):
        """
        Test that an unauthenticated user cannot update a book.
        """
        updated_data = {'title': 'Unauthorized Update', 'publication_year': 2000}
        response = self.client.put(self.url_update, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.book.refresh_from_db()
        self.assertNotEqual(self.book.title, 'Unauthorized Update')

    def test_delete_book_authenticated(self):
        """
        Test that an authenticated user can delete a book.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        """
        Test that an unauthenticated user cannot delete a book.
        """
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_year(self):
        """
        Test that the API can filter books by publication year.
        """
        Book.objects.create(title='Another Book', publication_year=2000, author=self.author)
        response = self.client.get(self.url_list_create, {'publication_year': 2000})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Another Book')
    
    def test_search_books_by_title(self):
        """
        Test that the API can search books by title.
        """
        Book.objects.create(title='The Chamber of Secrets', publication_year=1998, author=self.author)
        response = self.client.get(self.url_list_create, {'search': 'secrets'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Chamber of Secrets')

    def test_order_books_by_title_desc(self):
        """
        Test that the API can order books by title in descending order.
        """
        Book.objects.create(title='The Lord of the Rings', publication_year=1954, author=self.author)
        response = self.client.get(self.url_list_create, {'ordering': '-title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'The Lord of the Rings')
        self.assertEqual(response.data[1]['title'], 'Harry Potter and the Sorcerer\'s Stone')