# Generated by Django 3.2.6 on 2021-12-12 21:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_create_UserReviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]