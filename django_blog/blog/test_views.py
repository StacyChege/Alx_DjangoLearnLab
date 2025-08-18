from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

class AuthenticationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.profile_url = reverse('profile')

    def test_registration_view(self):
        """Test that a new user can register."""
        response = self.client.post(self.register_url, {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 302)  # Redirects to login
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        """Test that an existing user can log in."""
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        """Test that a logged-in user can log out."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Redirects to logged out page
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_profile_access(self):
        """Test that only authenticated users can view the profile."""
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)  # Redirects to login
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200) # OK

    def test_profile_update(self):
        """Test that a user can update their email."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.profile_url, {'username': 'testuser', 'email': 'updated@example.com'})
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updated@example.com')