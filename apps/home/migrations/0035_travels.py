# Generated by Django 3.2.6 on 2021-12-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_update_ItineraryPlanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='travels',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]