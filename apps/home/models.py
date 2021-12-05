# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Contact(models.Model):
    full_name = models.CharField(max_length=200, default="", blank=True)
    email = models.EmailField(max_length=100, default="", blank=True)
    subject = models.CharField(max_length=200, default="", blank=True)
    comment = models.TextField(max_length=500, default="", blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.full_name


class AboutUs(models.Model):
    name = models.CharField(max_length=200)
    subject = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    # subject = models.CharField(max_length=200)
    # sub_subject = models.TextField(null=True, blank=True)
    # content = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FAQGeneral(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question


class FAQTravel(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question


class Temp(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
