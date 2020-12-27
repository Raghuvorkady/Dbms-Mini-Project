from account.models import Account
from django.forms import ModelForm, fields, models
from .models import AUTHOR, BOOK, PUBLISHER, STOCK
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = '__all__'


class AddPublisherForm(ModelForm):
    class Meta:
        model = PUBLISHER
        fields = '__all__'


class AddAuthorForm(ModelForm):
    class Meta:
        model = AUTHOR
        fields = '__all__'


class AddBookForm(ModelForm):
    class Meta:
        model = BOOK
        fields = '__all__'
        exclude = ['librarianID']


class AddStockForm(ModelForm):
    class Meta:
        model = STOCK
        fields = ['bookCopies']
