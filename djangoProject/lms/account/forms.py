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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['USN'].required = True
        self.fields['course'].required = True
        self.fields['sem'].required = True
    
    class Meta:
        model = Account
        fields = ['email', 'username', 'fName', 'mName', 'lName', 'streetAddr', 
        'district', 'state', 'pinCode', 'phoneNum', 'USN', 'course', 'sem']

class StaffRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['salary'].required = True

    class Meta:
        model = Account
        fields = ['email', 'username', 'fName', 'mName', 'lName', 'streetAddr', 
        'district', 'state', 'pinCode', 'phoneNum', 'salary']