# Generated by Django 3.2 on 2022-02-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0009_shift_uncommon_holiday'),
    ]

    operations = [
        migrations.AddField(
            model_name='shiftgroup',
            name='uncommon_holiday_req',
            field=models.IntegerField(default=1, verbose_name='حداقل نفر در تعطیلات رسمی'),
        ),
    ]
