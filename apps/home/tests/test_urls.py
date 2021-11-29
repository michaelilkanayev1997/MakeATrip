from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from ... home.views import *

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_temp_url_is_resolved(self):
        url = reverse('temp')
        print(resolve(url))
        self.assertEquals(resolve(url).func, temp)

    def test_faq_url_is_resolved(self):
        url = reverse('faq')
        print(resolve(url))
        self.assertEquals(resolve(url).func, faq)

    def test_about_us_url_is_resolved(self):
        url = reverse('about-us')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about_us)

    def test_contact_us_url_is_resolved(self):
        url = reverse('contact-us')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact_us)
