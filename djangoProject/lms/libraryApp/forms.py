from django.forms import ModelForm, fields
from .models import AUTHOR, BOOK, PUBLISHER
from django import forms

class SelectPublisherForm(forms.Form):
    publishers = PUBLISHER.objects.all()
    publishersChoice = []
    for i in publishers:
        name = i.pubName
        publishersChoice.append((name, name))

    publisher = forms.ChoiceField(choices=publishersChoice)
    #your_name = forms.CharField(label='Your name', max_length=100)

class AddPublisherForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pubName'].required = False
        self.fields['streetAddr'].required = False
        self.fields['district'].required = False
        self.fields['state'].required = False
        self.fields['pinCode'].required = False
        self.fields['phoneNum'].required = False
        
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
    class Meta:
        model = BOOK
        fields = '__all__'