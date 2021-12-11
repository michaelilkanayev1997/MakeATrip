from django import forms
from .models import Contact, AboutUs, FAQTravel, FAQ, FAQGeneral


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

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = "__all__"
