# Generated by Django 3.2.6 on 2021-12-15 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_create_PrivacyPolicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='complete',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='no', max_length=9),
        ),
    ]
