# Generated by Django 3.1.2 on 2020-12-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0005_auto_20201224_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staffEmail',
            field=models.EmailField(help_text='Email id', max_length=50, unique=True),
        ),
    ]