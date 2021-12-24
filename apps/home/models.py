from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid

##########################################################################################################


##########################################################################################################
SUBJECT_CHOICES = (
    ('1', 'GENERAL'),
    ('2', 'COMPLAINT'),
)


##########################################################################################################

class ContactUs(models.Model):
    full_name = models.CharField(max_length=200, default="", blank=True)
    email = models.EmailField(max_length=100, default="", blank=True)
    subject = models.CharField(max_length=9, choices=SUBJECT_CHOICES, default='1')
    comment = models.TextField(max_length=200, default="", blank=True)
    created_date = models.DateField(default=datetime.now, blank=True)
    complete = models.BooleanField(default=False)

    class Meta:
        db_table = "home_contact_us"

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    pass


##########################################################################################################

class AboutUs(models.Model):
    name = models.CharField(max_length=200, default="", blank=True)
    subject = models.TextField(max_length=500, default="", blank=True)
    content = models.TextField(max_length=500, default="", blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


##########################################################################################################
class Career(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    job_title = models.CharField(max_length=200, default="", blank=True)
    job_net = models.CharField(max_length=200, default="", blank=True)
    job_detail = models.TextField(max_length=500, default="", blank=True)
    job_deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.job_title


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
    # subject = models.CharField(max_length=200)
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
    user = models.ForeignKey(t_user, on_delete=models.CASCADE, blank=True, null=True)
    destination = models.CharField(max_length=254)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    # travelers = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(ItineraryCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "%s -- %s > %s by %s" % (self.start_date, self.end_date, self.destination, self.user)


##########################################################################################################


class UserReviews(models.Model):
    user = models.ForeignKey(travel_user, on_delete=models.DO_NOTHING, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


##########################################################################################################

class PrivacyPolicy(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    subject = models.CharField(max_length=200, default="", blank=True)
    content = models.TextField(max_length=500000, default="", blank=True)

    def __str__(self):
        return self.subject


#####################################################################################################
VOTE_choice = (
    ('Very good', 'Very good'),
    ('Good', 'Good'),
    ('Mediocre', 'Mediocre'),
    ('Bad', 'Bad'),
    ('Very Bad', 'Very Bad'),

)


class Review(models.Model):
    feedback = models.CharField(max_length=200, choices=VOTE_choice)
    comment = models.TextField(max_length=500, default="", blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.feedback


#####################################################################################################
# for_usage
class users(models.Model):
    Types_users = models.CharField(max_length=100, null=False, blank=False)
    num_users = models.IntegerField()

    def __str__(self):
        return f'{self.Types_users} - {self.num_users}'


#####################################################################################################

class Travelers(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(t_user, on_delete=models.CASCADE, blank=True, null=True)
    travel = models.ManyToManyField('Travels')

    def __str__(self):
        return "%s > %s, from %s - %s" % (self.user, self.travel.destination, self.travel.start_date, self.travel.end_date)


class Travels(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    destination = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.destination


class Places(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    destination = models.ForeignKey(Travels, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False)
    opening_hours = models.CharField(max_length=100, null=False, blank=False)
    rating = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=3)
    type = models.CharField(max_length=100, null=False, blank=False)
    photo_url = models.CharField(max_length=500, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    driving = models.CharField(max_length=500, null=False, blank=False)
    walking = models.CharField(max_length=500, null=False, blank=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
