# Generated by Django 3.2.6 on 2021-12-12 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_delete_temp_kfir_again'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempTest',
            fields=[
                ('destination', models.CharField(max_length=254)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('travelers', models.IntegerField(blank=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                # ('category', models.ForeignKey(blank=True, null=True,
                # on_delete=django.db.models.deletion.DO_NOTHING, to='home.itinerarycategory')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
