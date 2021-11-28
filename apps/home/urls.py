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
    path('faq/', views.temp, name="faq"),
    path('about-us/', views.temp, name="about-us"),



    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
