# Generated by Django 3.1.2 on 2020-12-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('MATH', 'Mathematics'), ('ELE', 'Electronics'), ('TC', 'Telecommunication'), ('CHE', 'Chemistry'), ('PHY', 'Physics'), ('MEC', 'Mechanics'), ('EVS', 'Environmental Science'), ('BIO', 'Bioengineering'), ('BUS', 'Business Skills')], max_length=30, null=True),
        ),
    ]
