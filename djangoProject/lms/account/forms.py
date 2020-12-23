from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.models import ModelForm
from account.models import Account

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'username', 'fName', 'mName', 'lName', 'streetAddr', 
        'district', 'state', 'pinCode', 'phoneNum']

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'username', 'fName', 'mName', 'lName', 'streetAddr', 
        'district', 'state', 'pinCode', 'phoneNum', 'USN', 'course', 'sem']

class StaffRegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'username', 'fName', 'mName', 'lName', 'streetAddr', 
        'district', 'state', 'pinCode', 'phoneNum', 'salary']