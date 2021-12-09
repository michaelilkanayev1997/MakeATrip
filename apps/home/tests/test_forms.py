from django.test import SimpleTestCase
from apps.home.forms import ContactForm
from django import forms

class testforms(SimpleTestCase):
    def test_expense_form_valid_data(self):
        form=ContactForm(data={
            'full_name': 'expense1',
            'email': 'wwww@gmail.com',
            'subject': 'development',
            'comment': 'SHALOM'
        })

        self.assertTrue(form.is_valid())

        def test_expense_form_not_valid_data(self):
            form =ContactForm(data={})
            self.assertFalse(form.is_valid())

