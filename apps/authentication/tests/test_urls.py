from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ...authentication.views import *
from django.contrib.auth.views import LogoutView


class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_view)

    def test_register_user_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_user)
