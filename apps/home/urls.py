# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('temp/', views.temp, name="temp"),
    path('FAQ/', views.faq, name="faq"),
    path('about-us/', views.about_us, name="about-us"),
    path('contact-us/', views.contact_us, name="contact-us"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
