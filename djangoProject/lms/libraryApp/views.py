from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    main = 'libraryApp/main.html'
    return render(request, main)

def test(request):
    test = 'libraryApp/test.html'
    return render(request, test)

def test2(request):
    test2 = 'libraryApp/test2.html'
    return render(request, test2)

def test3(request):
    test3 = 'libraryApp/test3.html'
    return render(request, test3)

def test4(request):
    test4 = 'libraryApp/test4.html'
    return render(request, test4)

def progressive(request):
    progressive = 'libraryApp/progresive.html'
    return render(request, progressive)

def dashboard(request):
    dashboard = 'libraryApp/dashboard.html'
    return render(request, dashboard)

def borrowBook(request):
    borrowBook = 'libraryApp/borrow_book.html'
    return render(request, borrowBook)

def viewBook(request):
    viewBook = 'libraryApp/view_book.html'
    return render(request, viewBook)

def returnBook(request):
    returnBook = 'libraryApp/return_book.html'
    return render(request, returnBook)

def signIn(request):
    signIn = 'libraryApp/sign_in.html'
    return render(request, signIn)

def signUp(request):
    signUp = 'libraryApp/sign_up.html'
    return render(request, signUp)