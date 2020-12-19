from django.forms import ModelForm, fields, models
from .models import AUTHOR, BOOK, PUBLISHER, STOCK
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    fName = forms.CharField(max_length=20, label='first name')
    mName = forms.CharField(max_length=20, label='middle  name')
    lName = forms.CharField(max_length=20, label='last name')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SelectPublisherForm(forms.ModelForm):
    # publishers = PUBLISHER.objects.all()
    # publishersChoice = []
    # for i in publishers:
    #     name = i.pubName
    #     publishersChoice.append((name, name))

    #publisher = forms.ChoiceField(choices=publishersChoice)
    publisher = forms.ModelChoiceField(queryset=PUBLISHER.objects.all())
    
    class Meta:
        model = PUBLISHER
        fields = ['pubName']
    #your_name = forms.CharField(label='Your name', max_length=100)

class AddPublisherForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['pubName'].required = False
    #     self.fields['streetAddr'].required = False
    #     self.fields['district'].required = False
    #     self.fields['state'].required = False
    #     self.fields['pinCode'].required = False
    #     self.fields['phoneNum'].required = False
        
    class Meta:
        model = PUBLISHER
        fields = '__all__'

class SelectAuthorForm(forms.Form):
    authors = AUTHOR.objects.all()
    authorsChoice = []
    for i in authors:
        name = i.authorName
        authorsChoice.append((name, name))
    
    author = forms.ChoiceField(choices=authorsChoice)

class AddAuthorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['authorName'].required = False
        
    class Meta:
        model = AUTHOR
        fields = '__all__'

class AddBookForm(ModelForm):
    #noc = forms.IntegerField(min_value=0, help_text="Enter number of book copies")
    class Meta:
        model = BOOK
        fields = '__all__'

# class AddWrittenByForm(ModelForm):
#     class Meta:
#         model = WRITTENBY
#         fields = ['bookID', 'authorID']

class AddStockForm(ModelForm):
    class Meta:
        model = STOCK
        fields = ['bookCopies']