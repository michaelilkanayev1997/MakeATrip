from django import forms
from .models import Contact, AboutUs, FAQTravel, FAQGeneral


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class TempForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = "__all__"


class FaqGenralForm(forms.ModelForm):
    class Meta:
        model = FAQGeneral
        fields = "__all__"

class FaqTravelForm(forms.ModelForm):
    class Meta:
        model = FAQTravel
        fields = "__all__"
