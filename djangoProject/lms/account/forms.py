from libraryApp.models import STAFF
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.contrib.auth import login, logout, authenticate
from django.forms.models import ModelForm
from account.models import Account

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
    
    def clean_USN(self):
        usn = self.cleaned_data['USN']
        if len(usn) != 10:
            raise forms.ValidationError("Enter a valid USN")
        else:
            return usn

class StaffRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['salary'].required = True

    class Meta:
        model = Account
        fields = ['email', 'username', 'fName', 'mName', 'lName', 'streetAddr', 
        'district', 'state', 'pinCode', 'phoneNum', 'salary']

    def clean_email(self):
        staff = STAFF.objects.all()
        staffEmails = []
        email = self.cleaned_data['email']
        for i in staff:
            staffEmails.append(i.staffEmail)
        if email in staffEmails:
            if Account.objects.filter(email=email).exists():
                raise forms.ValidationError("This email address is already in use.")
            else:
                return email
        else:
            raise forms.ValidationError("Invalid staff mail id | Please contact admin")

class AccountLoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
        

