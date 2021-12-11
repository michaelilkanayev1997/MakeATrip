from django import forms
from .models import Contact, Review



########################################################
#contact-us
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
######################################################
#Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields = "__all__"

    def __init__(self, *args, **kwargs):
            super(ReviewForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})

######################################################
