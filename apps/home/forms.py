from django import forms
from .models import Contact


########################################################
#contact-us
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
######################################################
#ProductReview



######################################################