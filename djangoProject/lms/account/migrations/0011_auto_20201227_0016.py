# Generated by Django 3.1.2 on 2020-12-26 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20201223_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='USN',
            field=models.CharField(blank=True, help_text='University Serial Number', max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_USN', message='Enter a valid USN', regex='[1-4]{1}[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}[0-9]{3}')]),
        ),
    ]
