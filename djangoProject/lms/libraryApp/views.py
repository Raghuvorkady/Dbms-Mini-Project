from libraryApp.models import *
from django.shortcuts import render
from django.http import HttpResponse


class tempBook:

    def __init__(self, slNo, bookTitle, genre, pubName, pubYear, author, isbn, stock):
        self.slNo = slNo
        self.bookTitle = bookTitle
        self.genre = genre
        self.pubName = pubName
        self.pubYear = pubYear
        self.author = author
        self.isbn = isbn
        self.stock = stock

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
    booksList = []
    count = 0
    
    for i in books:
        count += 1
        stock = STOCK.objects.filter(bookID__bookTitle=i.bookTitle).first()
        wb = WRITTENBY.objects.filter(bookID__bookTitle=i.bookTitle)
        authorList = []
        for w in wb.all():
            for j in w.authorID.all():
                authorList.append(j)
        authorString = ', '.join(map(str, authorList))
        pub = PUBLISHER.objects.filter(
            book__bookTitle__contains=i.bookTitle).first()
        #print(i.bookTitle, "of genre", i.genre, "of ID:", i.id, "is published by,", pub.pubName,"of id", pub.id, "and authors are: ", authors, "is having:", stock.bookCopies, "copies")
        booksList.append(tempBook(count, i.bookTitle, i.genre,
                                  pub.pubName, i.pubYear, authorString, i.isbn, stock.bookCopies))

    context = {
        'books': booksList,
        'count': count
    }
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
