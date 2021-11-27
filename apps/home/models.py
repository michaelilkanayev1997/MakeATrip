# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class AboutUs(models.Model):
    name = models.CharField(max_length=200)
    sub_subject = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    subject = models.CharField(max_length=200)
    sub_subject = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Temp(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TempGeneral(models.Model):
    name = models.CharField(max_length=200)
    subject = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class TempTravel(models.Model):
    name = models.CharField(max_length=200)
    subject = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

