# Generated by Django 3.2.6 on 2021-12-05 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, default='', max_length=200)),
                ('email', models.EmailField(blank=True, default='', max_length=100)),
                ('subject', models.CharField(blank=True, default='', max_length=200)),
                ('comment', models.TextField(blank=True, default='', max_length=500)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
