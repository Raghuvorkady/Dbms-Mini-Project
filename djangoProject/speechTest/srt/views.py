from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here
def index(request):
    main = 'srt/main.html'
    return render(request, main)

