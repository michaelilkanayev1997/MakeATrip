from django import forms
from .models import Contact, AboutUs, FAQTravel, FAQGeneral
from .models import Contact, AboutUs, ItineraryPlanner, ItineraryCategory


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
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


class ItineraryPlannerForm(forms.ModelForm):
    class Meta:
        model = ItineraryPlanner
        fields = '__all__'
        exclude = ['user', 'category']


class ItineraryCategoryForm(forms.ModelForm):
    class Meta:
        model = ItineraryCategory
        fields = ('culture', 'outdoors', 'beaches', 'shopping', 'museums', 'restaurants')
