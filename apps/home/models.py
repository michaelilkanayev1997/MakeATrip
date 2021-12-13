from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid


##########################################################################################################

class Contact(models.Model):
    full_name = models.CharField(max_length=200, default="", blank=True)
    email = models.EmailField(max_length=100, default="", blank=True)
    subject = models.CharField(max_length=200, default="", blank=True)
    comment = models.TextField(max_length=500, default="", blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        db_table = "home_contact"

    def __str__(self):
        return self.full_name


##########################################################################################################

class AboutUs(models.Model):
    name = models.CharField(max_length=200, default="", blank=True)
    subject = models.TextField(max_length=500, default="", blank=True)
    content = models.TextField(max_length=500, default="", blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


##########################################################################################################

class FAQ(models.Model):
    name = models.CharField(max_length=200)
    test = models.CharField(max_length=200, default="", blank=True)

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


##########################################################################################################

class Temp(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)


##########################################################################################################

travel_user = get_user_model()
t_user = User

class ItineraryCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    culture = models.BooleanField(default=False)
    outdoors = models.BooleanField(default=False)
    beaches = models.BooleanField(default=False)
    shopping = models.BooleanField(default=False)
    museums = models.BooleanField(default=False)
    restaurants = models.BooleanField(default=False)


class ItineraryPlanner(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(t_user, on_delete=models.DO_NOTHING, blank=True, null=True)
    destination = models.CharField(max_length=254)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    # category = models.ForeignKey(ItineraryCategory, on_delete=models.DO_NOTHING, blank=True, null=True)


    def __str__(self):
        return "%s -- %s > %s by %s" % (self.start_date, self.end_date, self.destination, self.user)


##########################################################################################################


class UserReviews(models.Model):
    user = models.ForeignKey(travel_user, on_delete=models.DO_NOTHING, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

