# Generated by Django 3.2.6 on 2021-12-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_edit_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career',
            old_name='content',
            new_name='job_detail',
        ),
        migrations.RenameField(
            model_name='career',
            old_name='name',
            new_name='job_net',
        ),
        migrations.RemoveField(
            model_name='career',
            name='subject',
        ),
        migrations.AddField(
            model_name='career',
            name='job_deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='job_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
