from django.test import TestCase, Client
from django.urls import reverse
from ...home.models import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.faq_url = reverse('faq')
        self.temp_url = reverse('temp')
        self.about_us_url = reverse('about-us')
        self.contact_us_url = reverse('contact-us')
        self.index_url = reverse('home')


    def test_faq(self):
        response = self.client.get(self.faq_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/faq.html')

    """def test_temp(self):
        response = self.client.get(self.temp_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/temp.html')"""

    def test_about_us(self):
        response = self.client.get(self.about_us_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about-us.html')

    def test_contact_us(self):
        response = self.client.get(self.contact_us_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact-us.html')

    def test_index(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')