from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestLogin(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'admin',
            'password': 'admin'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)


class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.username = 'test'
        self.email = 'test@mail.com'
        self.password = 'Pa$$W0rd'

    def test_signup_form(self):
        response = self.client.post(reverse('register'), data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 200)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

