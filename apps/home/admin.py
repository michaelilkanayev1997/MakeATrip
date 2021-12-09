# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import AboutUs, FAQTravel, FAQGeneral, FAQ,Contact, Temp
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
admin.site.register(Contact)
####################################