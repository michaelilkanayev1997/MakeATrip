# Generated by Django 3.2.6 on 2021-12-24 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_update_Travel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerarycategory',
            old_name='beaches',
            new_name='calm',
        ),
        migrations.RenameField(
            model_name='itinerarycategory',
            old_name='museums',
            new_name='food',
        ),
        migrations.RenameField(
            model_name='itinerarycategory',
            old_name='outdoors',
            new_name='parks',
        ),
        migrations.RemoveField(
            model_name='itinerarycategory',
            name='restaurants',
        ),
    ]
