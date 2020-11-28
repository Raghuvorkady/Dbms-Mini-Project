from libraryApp.models import *
from django.shortcuts import render
from django.http import HttpResponse
import datetime

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
class tempDashboard:

    def __init__(self, slNo, bookTitle, userName, checkOut, checkIn, dueDate):
        self.slNo = slNo
        self.bookTitle = bookTitle
        self.userName = userName
        self.checkOut = checkOut
        self.checkIn = checkIn
        self.dueDate = dueDate


def index(request):
    main = 'libraryApp/main.html'
    return render(request, main)


def addPublisherDetails(request):
    publisherDetails = 'libraryApp/add_publisher_details.html'
    publishers = PUBLISHER.objects.all()
    
    context = {
        'publishers' : publishers
    }
    
    return render(request, publisherDetails, context)


def addAuthorDetails(request):
    authorDetails = 'libraryApp/add_author_details.html'
    authors = AUTHOR.objects.all()

    context = {
        'authors': authors
    }
        
    return render(request, authorDetails, context)


def addBookDetails(request):
    bookDetails = 'libraryApp/add_book_details.html'
    authors = AUTHOR.objects.all()
    publishers = PUBLISHER.objects.all()
    
    context = {
        'authors': authors,
        'publishers' : publishers

    }
    return render(request, bookDetails, context)


def addBookTemplate(request):
    addBookTemplate = 'libraryApp/add_book_template.html'
    return render(request, addBookTemplate)


def progressive(request):
    progressive = 'libraryApp/progresive.html'
    return render(request, progressive)


def dashboard(request):
    dashboard = 'libraryApp/dashboard.html'
    borrowedBooks = BORROWEDBOOK.objects.all()
    borrowedBooksList = []
    returnedBooksList = []
    count = 0
    for i in borrowedBooks:
        count += 1
        user = USER.objects.filter(email=i.userID).first()
        userName = user.fName + " " + user.mName + " " + user.lName
        print(userName)
        if i.checkIn is not None:
            borrowedBooksList.append(tempDashboard(count, i.bookID, userName, i.checkOut, i.checkIn, i.dueDate + datetime.timedelta(days=14)))
        else:
            returnedBooksList.append(tempDashboard(count, i.bookID, userName, i.checkOut, i.checkIn, i.dueDate))

    context = {
        "borrowedBooks" : borrowedBooksList,
        "returnedBooks" : returnedBooksList
    }
    return render(request, dashboard, context)


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
    states = defaultValues.statesInIndia
    courses = defaultValues.courses
    genres = defaultValues.genre
    context = {
        "states" : states,
        "courses" : courses,
        "genres" : genres
    }
    return render(request, signUp, context)
