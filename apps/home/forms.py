from django import forms
from .models import Contact, AboutUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class TempForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = "__all__"
