# Generated by Django 3.1.2 on 2020-12-19 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AUTHOR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BOOK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookTitle', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=30, null=True)),
                ('pubYear', models.CharField(max_length=4, null=True)),
                ('isbn', models.CharField(max_length=13, null=True)),
                ('authorID', models.ManyToManyField(to='libraryApp.AUTHOR')),
            ],
        ),
        migrations.CreateModel(
            name='defaultValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LIBRARIAN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=20)),
                ('mName', models.CharField(blank=True, max_length=20)),
                ('lName', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=20)),
                ('streetAddr', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pinCode', models.CharField(max_length=6)),
                ('phoneNum', models.CharField(max_length=10)),
                ('salary', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='PUBLISHER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubName', models.CharField(max_length=30)),
                ('streetAddr', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pinCode', models.CharField(max_length=6)),
                ('phoneNum', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='STAFF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffEmail', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=20)),
                ('mName', models.CharField(blank=True, max_length=20)),
                ('lName', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(help_text='A valid email address, please.', max_length=254)),
                ('pwd', models.CharField(max_length=20)),
                ('streetAddr', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pinCode', models.CharField(max_length=6)),
                ('phoneNum', models.CharField(max_length=10)),
                ('USN', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=50)),
                ('sem', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='STOCK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookCopies', models.PositiveIntegerField()),
                ('bookID', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='libraryApp.book')),
                ('librarianID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libraryApp.librarian')),
            ],
        ),
        migrations.CreateModel(
            name='BORROWEDBOOK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkOut', models.DateTimeField(auto_now_add=True, null=True)),
                ('dueDate', models.DateTimeField(blank=True, null=True)),
                ('checkIn', models.DateTimeField(blank=True, null=True)),
                ('bookID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libraryApp.book')),
                ('userID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libraryApp.user')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='librarianID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libraryApp.librarian'),
        ),
        migrations.AddField(
            model_name='book',
            name='pubID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='libraryApp.publisher'),
        ),
    ]
