# Generated by Django 3.2.6 on 2021-12-10 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20211210_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraryplanner',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.itinerarycategory'),
        ),
        migrations.AlterField(
            model_name='itineraryplanner',
            name='travelers',
            field=models.IntegerField(blank=True),
        ),
    ]
