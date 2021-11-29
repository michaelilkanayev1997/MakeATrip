# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .testt import tes1t

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('temp.html', views.temp, name="temp"),
    path('FAQ.html', views.faq, name="faq"),
    path('about-us.html', views.about_us, name="about-us"),
    path('contact-us.html', views.contact_us, name="contact-us"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
