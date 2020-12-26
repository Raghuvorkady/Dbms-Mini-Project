from account.forms import RegistrationForm
from django.shortcuts import render

# Create your views here.
def signUp(request):
    signUp = 'libraryApp/sign_up.html'

    signUpForm = RegistrationForm()

    context = {
        "form" : signUpForm
    }
    return render(request, signUp, context)

def signIn(request):
    signIn = 'libraryApp/sign_in.html'
    return render(request, signIn)
