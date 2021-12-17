# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import AboutUs, FAQTravel, FAQGeneral, FAQ, ContactUs, Temp, ItineraryPlanner, ItineraryCategory, Career, PrivacyPolicy, Review,users

####################################
# for Temp Only!!!
admin.site.register(Temp)
####################################
####################################
# About US
admin.site.register(AboutUs)
####################################
####################################
# FAQ
admin.site.register(FAQ)
admin.site.register(FAQGeneral)
admin.site.register(FAQTravel)
####################################
####################################
# CONTACTUS
admin.site.register(ContactUs)
####################################
####################################
# TRAVEL
admin.site.register(ItineraryPlanner)
admin.site.register(ItineraryCategory)
####################################
####################################
# CAREER
admin.site.register(Career)
####################################
####################################
# PRIVACY POLICY
admin.site.register(PrivacyPolicy)
####################################
####################################
# REVIEW
admin.site.register(Review)
####################################
####################################
admin.site.register(users)

####################################