# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.urls import path, re_path
from apps.home import views


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('temp/', views.temp, name='temp'),
    path('edit-faq/', views.edit_faq, name='edit-faq'),
    path('faq/', views.faq, name="faq"),
    path('about-us/', views.about_us, name="about-us"),
    path('career/', views.career, name="career"),
    path('career/<str:pk>/', views.job_detail, name="career"),
    path('create-about-us/', views.create_about_us, name='create-about-us'),
    path('update-about-us/<str:pk>/', views.update_about_us, name='update-about-us'),
    path('delete-about-us/<str:pk>/', views.delete_about_us, name='delete-about-us'),
    path('terms-of-use/', views.terms_of_use, name="terms-of-use"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('complaints/', views.complaints, name='complaints'),
    path('complaints/<str:pk>/', views.complaint, name='complaints'),
    path('privacy-policy/', views.privacy_policy, name="privacy-policy"),
    path('to_do_list/', views.to_do_list, name="to_do_list"),
    path('recent_trips/', views.recent_trips, name="recent_trips"),
    path('review/', views.review_project, name="review"),
    path('monthly_inquiries_report/', views.monthly_inquiries_report, name="monthly_inquiries_report"),
    path('system-usages/', views.system_usages, name="system-usages"),
    path('popular/', views.report_most_popular, name="popular"),
    path('employees-report/', views.employees_report, name="employees-report"),
    path('trip/', views.trip, name="trip"),
    path('report_analysis/', views.report_analysis, name="report_analysis"),
    path('system_integrity_check/', views.system_integrity_check, name="system_integrity_check"),

    # re_path(r'^.*\.*', views.pages, name='pages'),



]
