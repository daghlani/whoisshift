# Generated by Django 3.2 on 2022-02-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0012_profile_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='in_day_shift',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='in_night_shift',
            field=models.BooleanField(default=True),
        ),
    ]
