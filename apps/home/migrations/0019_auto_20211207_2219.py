# Generated by Django 3.2.6 on 2021-12-07 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0019_alter_itineraryplanner_user'),
    ]

