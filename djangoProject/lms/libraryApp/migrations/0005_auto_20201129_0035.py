# Generated by Django 3.1.2 on 2020-11-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0004_auto_20201129_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='checkIn',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]