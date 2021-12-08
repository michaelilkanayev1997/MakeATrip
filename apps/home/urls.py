# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf.urls import url
from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('temp/', views.temp, name='temp'),
    path('edit-faq/', views.edit_faq, name='edit-faq'),
    path('faq/', views.faq, name="faq"),
    path('about-us/', views.about_us, name="about-us"),
    path('terms-of-use/', views.terms_of_use, name="terms-of-use"),
    path('contact-us/', views.contact_us, name="contact-us"),
    re_path(r'^.*\.*', views.pages, name='pages'),

]
