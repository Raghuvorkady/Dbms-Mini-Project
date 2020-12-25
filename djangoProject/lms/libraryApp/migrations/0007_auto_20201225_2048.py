# Generated by Django 3.1.2 on 2020-12-25 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0006_auto_20201225_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='bookID',
            field=models.ForeignKey(help_text='Book ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='libraryApp.book'),
        ),
    ]