from libraryApp.models import AUTHOR, BOOK, PUBLISHER, WRITTENBY
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    main = 'libraryApp/main.html'
    return render(request, main)

def addPublisherDetails(request):
    publisherDetails = 'libraryApp/add_publisher_details.html'
    return render(request, publisherDetails)

def addAuthorDetails(request):
    authorDetails = 'libraryApp/add_author_details.html'
    return render(request, authorDetails)

def addBookDetails(request):
    bookDetails = 'libraryApp/add_book_details.html'
    return render(request, bookDetails)

def addBookTemplate(request):
    addBookTemplate = 'libraryApp/add_book_template.html'
    return render(request, addBookTemplate)

def progressive(request):
    progressive = 'libraryApp/progresive.html'
    return render(request, progressive)

def dashboard(request):
    dashboard = 'libraryApp/dashboard.html'
    return render(request, dashboard)

def borrowBook(request):
    borrowBook = 'libraryApp/borrow_book.html'

    books = BOOK.objects.all()

    for i in books:
        pub = PUBLISHER.objects.filter(pubName=i.pubID)
        for i in pub.all():
            print(i)
            
        wb = WRITTENBY.objects.filter(bookID = i.id)
        print(wb)
    
    author = AUTHOR.objects
    context = {'books': books}
    return render(request, borrowBook, context)

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