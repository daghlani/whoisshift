# Generated by Django 3.2 on 2022-03-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0023_alter_shiftday_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftday',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
