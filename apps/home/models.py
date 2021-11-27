# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Temp(models.Model):
    name = models.CharField(max_length=200)
    header = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    name = models.CharField(max_length=200)
    header = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    name = models.CharField(max_length=200)
    header = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
