# Generated by Django 3.2 on 2022-02-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0007_auto_20220217_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftday',
            name='day_people_list',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shiftday',
            name='day_pr_people_list',
            field=models.TextField(blank=True, null=True),
        ),
    ]
