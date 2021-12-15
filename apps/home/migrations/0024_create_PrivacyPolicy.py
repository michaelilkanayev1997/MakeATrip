# Generated by Django 3.2.6 on 2021-12-15 19:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_edit_Career'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('subject', models.CharField(blank=True, default='', max_length=200)),
                ('content', models.TextField(blank=True, default='', max_length=500000)),
            ],
        ),
    ]
