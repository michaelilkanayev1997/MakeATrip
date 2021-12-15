from django import forms
from .models import ContactUs, AboutUs, FAQTravel, FAQGeneral, ItineraryPlanner, ItineraryCategory, Career, PrivacyPolicy,Review


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"


class TempForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = "__all__"


class FaqGeneralForm(forms.ModelForm):
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

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = "__all__"


class ItineraryPlannerForm(forms.ModelForm):
    class Meta:
        model = ItineraryPlanner
        fields = '__all__'
        exclude = ['user', 'category']


class ItineraryCategoryForm(forms.ModelForm):
    class Meta:
        model = ItineraryCategory
        fields = ('culture', 'outdoors', 'beaches', 'shopping', 'museums', 'restaurants')



class complaintform(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('complete',)

class PrivacyPolicyForm(forms.ModelForm):
    class Meta:
        model = PrivacyPolicy
        fields = "__all__"

class administrator_complaintsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('complete',)

class ReviewpForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ['created_date']