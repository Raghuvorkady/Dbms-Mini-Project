from django.db.models import query
from libraryApp.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .filters import BookFilter
from .forms import AddAuthorForm, AddBookForm, AddPublisherForm, SelectAuthorForm, SelectPublisherForm

class tempBook:

    def __init__(self, slNo, bookTitle, bookID, genre, pubName, pubYear, author, isbn, stock):
        self.slNo = slNo
        self.bookTitle = bookTitle
        self.bookID = bookID
        self.genre = genre
        self.pubName = pubName
        self.pubYear = pubYear
        self.author = author
        self.isbn = isbn
        self.stock = stock

# Create your views here.
class tempDashboard:

    def __init__(self, slNo, bookTitle, bookID, userName, authorName, isbn, checkOut, checkIn, dueDate):
        self.slNo = slNo
        self.bookTitle = bookTitle
        self.bookID = bookID
        self.userName = userName
        self.authorName = authorName
        self.isbn = isbn
        self.checkOut = checkOut
        self.checkIn = checkIn
        self.dueDate = dueDate


def index(request):
    main = 'libraryApp/main.html'
    return render(request, main)


def addPublisherDetails(request, option):
    publisherDetails = 'libraryApp/add_publisher_details.html'
    publishers = PUBLISHER.objects.all()

    selectPublisherForm = SelectPublisherForm()
    addPublisherForm = AddPublisherForm()

    if request.method == "POST":
        print("PUB REQUEST:",request.POST)
        addPub = request.POST['pubName']
        if addPub == '':
            selectedPub = request.POST['publisher']
            print(selectedPub)
            return redirect(addAuthorDetails, option=option)
        else:
            print("add PUB:", addPub)
            addPublisherForm = AddPublisherForm(request.POST)
            if addPublisherForm.is_valid():
                addPublisherForm.save()
                return redirect(addAuthorDetails, option=option)


    context = {
        'publishers' : publishers,
        'option' : option,
        'selectPublisherForm' : selectPublisherForm,
        'addPublisherForm' : addPublisherForm,
    }
    
    return render(request, publisherDetails, context)


def addAuthorDetails(request, option):
    authorDetails = 'libraryApp/add_author_details.html'
    authors = AUTHOR.objects.all()

    selectAuthorForm = SelectAuthorForm()
    addAuthorForm = AddAuthorForm()

    if request.method == "POST":
        print("AUTH REQUEST:",request.POST)
        addAuthor = request.POST['authorName']
        if addAuthor == '':
            selectedAuthor = request.POST['author']
            print(selectedAuthor)
            return redirect(addBookDetails, option=option)
        else:
            print("add PUB:", addAuthor)
            addAuthorForm = AddAuthorForm(request.POST)
            if addAuthorForm.is_valid():
                addAuthorForm.save()
                return redirect(addBookDetails, option=option)


    context = {
        'authors': authors,
        'option' : option,
        'selectAuthorForm' : selectAuthorForm,
        'addAuthorForm' : addAuthorForm
    }
        
    return render(request, authorDetails, context)


def addBookDetails(request, option):
    bookDetails = 'libraryApp/add_book_details.html'
    authors = AUTHOR.objects.all()
    publishers = PUBLISHER.objects.all()
    genres = defaultValues.genre

    addBookForm = AddBookForm()
    if request.method == "POST":
        print("BOOK REQUEST:",request.POST)
        addBookForm = AddBookForm(request.POST)

        if addBookForm.is_valid():
            bookID = addBookForm.save()
            print("\nBOOK ID: ", bookID)

            stock = request.POST['noc']
            librarianID = request.POST['librarianID']
            authorID = request.POST['author']

            STOCK.objects.create(bookID=bookID, bookCopies=stock, librarianID=LIBRARIAN.objects.get(id=librarianID))
            wb = WRITTENBY.objects.create()
            authorList = []
            authorList = request.POST.getlist('author')
            print("\nls AUTHORS", authorList)
            for i in authorList:
                print("\nAUTHOR",i)
                authorID=AUTHOR.objects.get(id=i)
                wb.authorID.add(authorID)
            wb.bookID.add(bookID)
            
            return redirect(borrowBook)

    context = {
        'authors': authors,
        'publishers' : publishers,
        'genres' : genres,
        'option' : option,
        'addBookForm' : addBookForm
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

    myFilter = BookFilter(request.GET, queryset=BOOK.objects.all())

    dbActive = True
    borrowedBooksList = []
    returnedBooksList = []
    bCount = 0
    rCount = 0
    for i in borrowedBooks:
        user = USER.objects.filter(email=i.userID).first()
        book = BOOK.objects.filter(bookTitle=i.bookID).first()
        userName = user.fName + " " + user.mName + " " + user.lName
        #print(i, "CHECKIN", i.checkIn)
        if i.checkIn is None:
            #print("borrowed",userName)
            bCount += 1
            borrowedBooksList.append(tempDashboard(bCount, i.bookID, book.id, userName, None, None, i.checkOut, None, i.dueDate))
            #print("\nBORROWED LIST\n")
            #print(borrowedBooksList)
        else:
            #print("returned",userName)
            rCount += 1
            returnedBooksList.append(tempDashboard(rCount, i.bookID, book.id, userName, None, None, i.checkOut, i.checkIn, None))
            #print("\nRETURNED LIST\n")
            #print(returnedBooksList)

    context = {
        "borrowedBooks" : borrowedBooksList,
        "bCount" : bCount,
        "returnedBooks" : returnedBooksList,
        "rCount" : rCount,
        "myFilter" : myFilter,
        "dbActive" : dbActive
    }
    return render(request, dashboard, context)


def borrowBook(request):
    borrowBook = 'libraryApp/borrow_book.html'
    
    books = BOOK.objects.all()

    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs

    bbActive = True
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
        booksList.append(tempBook(count, i.bookTitle, i.id, i.genre,
                                  pub.pubName, i.pubYear, authorString, i.isbn, stock.bookCopies))

    context = {
        'books': booksList,
        'count': count,
        "myFilter" : myFilter,
        "bbActive" : bbActive
    }
    return render(request, borrowBook, context)


def viewBook(request, bookID):
    viewBook = 'libraryApp/view_book.html'

    myFilter = BookFilter(request.GET, queryset=BOOK.objects.all())
    books = myFilter.qs

    book = BOOK.objects.get(id=bookID)
    pub = PUBLISHER.objects.filter(book__bookTitle__contains=book.bookTitle).first()
    stock = STOCK.objects.filter(bookID__bookTitle=book.bookTitle).first()
    wb = WRITTENBY.objects.filter(bookID__bookTitle=book.bookTitle)
    authorList = []
    for w in wb.all():
        for j in w.authorID.all():
            authorList.append(j)
    authorString = ', '.join(map(str, authorList))
    bookObject = tempBook(None, book.bookTitle, book.id, book.genre, pub.pubName, book.pubYear, authorString, book.isbn, stock.bookCopies)

    context = {
        "book" : bookObject,
        "pub" : pub,
        "myFilter" : myFilter
    }
    return render(request, viewBook, context)


def returnBook(request):
    returnBook = 'libraryApp/return_book.html'
    borrowedBooks = BORROWEDBOOK.objects.all()

    myFilter = BookFilter(request.GET, queryset=BOOK.objects.all())
    books = myFilter.qs

    rbActive = True
    borrowedBooksList = []
    bCount = 0
    for i in borrowedBooks:
        user = USER.objects.filter(email=i.userID).first()
        wb = WRITTENBY.objects.filter(bookID__bookTitle=i.bookID)
        book = BOOK.objects.filter(bookTitle = i.bookID).first()
        userName = user.fName + " " + user.mName + " " + user.lName
        authorList = []
        for w in wb.all():
            for j in w.authorID.all():
                authorList.append(j)
        authorString = ', '.join(map(str, authorList))
        if i.checkIn is None:
            bCount += 1
            borrowedBooksList.append(tempDashboard(bCount, i.bookID, book.id, userName, authorString, book.isbn, i.checkOut, None, i.dueDate))

    context = {
        "borrowedBooks" : borrowedBooksList,
        "count" : bCount,
        "myFilter" : myFilter,
        "rbActive" : rbActive
    }

    return render(request, returnBook, context)


def signIn(request):
    signIn = 'libraryApp/sign_in.html'
    return render(request, signIn)


def signUp(request):
    signUp = 'libraryApp/sign_up.html'
    states = defaultValues.statesInIndia
    courses = defaultValues.courses
    context = {
        "states" : states,
        "courses" : courses,
    }
    return render(request, signUp, context)

def searchResult(request, book):
    searchResult = 'libraryApp/search_result_page.html'
    books = BOOK.objects.filter(bookTitle__iexact=book)

    myFilter = BookFilter(request.GET, queryset=BOOK.objects.all())
    books = myFilter.qs

    query = request.GET['bookTitle']
    if query is None:
        query = ""

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
        booksList.append(tempBook(count, i.bookTitle, i.id, i.genre,
                                  pub.pubName, i.pubYear, authorString, i.isbn, stock.bookCopies))

    context = {
        'books': booksList,
        'count': count,
        'query' : query,
        'myFilter' : myFilter
    }
    return render(request, searchResult, context)