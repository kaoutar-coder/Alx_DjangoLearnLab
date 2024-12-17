from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123', email='test@example.com')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)  # Successful login redirects
        self.assertRedirects(response, '/')  # Redirect to home

    def test_logout_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Logout redirects
        self.assertRedirects(response, '/')

    def test_registration_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Registration redirects
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_profile_view_access(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Unauthenticated users are redirected to login

        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)  # Authenticated users can access the profile page
