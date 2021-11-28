# Generated by Django 3.2.6 on 2021-11-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211127_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQTravel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='sub_subject',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='subject',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='content',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='sub_subject',
        ),
    ]