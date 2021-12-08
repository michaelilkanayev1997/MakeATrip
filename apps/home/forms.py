from django import forms
from .models import Contact,ProductReview


########################################################
#contact-us
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
######################################################
#ProductReview
class ReviewAdd(forms.ModelForm):
	class Meta:
		model=ProductReview
		fields=('review_text','review_rating')


######################################################