from account.forms import AccountLoginForm, StaffRegistrationForm, StudentRegistrationForm
from libraryApp.models import *
from django.shortcuts import render, redirect
from .filters import BookFilter
from .forms import AddAuthorForm, AddBookForm, AddPublisherForm, AddStockForm
from django.contrib.auth import authenticate, login, logout
import time
import datetime

class tempBook:
    def __init__(self, slNo, bookTitle, bookID, genre, pubID, pubName, pubYear, authID, author, isbn, stock):
        self.slNo = slNo
        self.bookTitle = bookTitle
        self.bookID = bookID
        self.pubID = pubID
        self.genre = genre
        self.pubName = pubName
        self.pubYear = pubYear
        self.authID = authID
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
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    else:
        return redirect(signIn)


def addPublisherDetails(request, option):
    publisherDetails = 'libraryApp/add_publisher_details.html'
    publishers = PUBLISHER.objects.all()

    #selectPublisherForm = SelectPublisherForm()
    addPublisherForm = AddPublisherForm()

    if request.method == "POST":
        addPublisherForm = AddPublisherForm(request.POST)
        if addPublisherForm.is_valid():
            addPublisherForm.save()
            return redirect(manage)

        # print("PUB REQUEST:",request.POST)
        # addPub = request.POST['pubName']
        # if addPub == '':
        #     selectedPub = request.POST['publisher']
        #     print(selectedPub)
        #     return redirect(addAuthorDetails, option=option)
        # else:
        #     print("add PUB:", addPub)
        #     addPublisherForm = AddPublisherForm(request.POST)
        #     if addPublisherForm.is_valid():
        #         addPublisherForm.save()
        #         return redirect(addAuthorDetails, option=option)

    context = {
        'publishers': publishers,
        'option': option,
        # 'selectPublisherForm' : selectPublisherForm,
        'addPublisherForm': addPublisherForm
    }

    return render(request, publisherDetails, context)


def addAuthorDetails(request, option):
    authorDetails = 'libraryApp/add_author_details.html'
    authors = AUTHOR.objects.all()

    #selectAuthorForm = SelectAuthorForm()
    addAuthorForm = AddAuthorForm()

    if request.method == "POST":
        addAuthorForm = AddAuthorForm(request.POST)
        if addAuthorForm.is_valid():
            addAuthorForm.save()
            return redirect(manage)

        """print("AUTH REQUEST:",request.POST)
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
                return redirect(addBookDetails, option=option)"""

    context = {
        'authors': authors,
        'option': option,
        # 'selectAuthorForm' : selectAuthorForm,
        'addAuthorForm': addAuthorForm
    }

    return render(request, authorDetails, context)


def addBookDetails(request, option):
    bookDetails = 'libraryApp/add_book_details.html'

    addBookForm = AddBookForm()
    addStockForm = AddStockForm()
    
    print("\nUSER: ", request.user)
    print("\nUSER ID: ", request.user.id)

    #addBookForm.fields['librarianID'].widget.attrs['readonly'] = True # text input


    if request.method == "POST":
        print("BOOK REQUEST:", request.POST)
        addBookForm = AddBookForm(request.POST)

        if addBookForm.is_valid():
            bookID = addBookForm.save()
            print("\nBOOK ID: ", bookID)

            stock = request.POST['bookCopies']
            bookID.librarianID = Account.objects.get(id=request.user.id)
            bookID.save()

            STOCK.objects.create(
                bookID=bookID, bookCopies=stock, librarianID=bookID.librarianID)

            return redirect(manage)

    context = {
        'option': option,
        'addBookForm': addBookForm,
        'addStockForm': addStockForm
    }
    return render(request, bookDetails, context)


def updatePublisherDetails(request, pubID):
    publisherDetails = 'libraryApp/add_publisher_details.html'
    publishers = PUBLISHER.objects.get(id=pubID)

    print("PUBID", pubID)
    addPublisherForm = AddPublisherForm(instance=publishers)
    if request.method == "POST":
        addPublisherForm = AddPublisherForm(request.POST, instance=publishers)
        if addPublisherForm.is_valid():
            addPublisherForm.save()
            print("REQUEST:", request.POST)
            return redirect(manage)

    context = {
        'publishers': publishers,
        'addPublisherForm': addPublisherForm,
        'option': 'Update'
    }
    return render(request, publisherDetails, context)


def updateAuthorDetails(request, pk):
    authorDetails = 'libraryApp/add_author_details.html'
    authors = AUTHOR.objects.get(id=pk)

    addAuthorForm = AddAuthorForm(instance=authors)

    if request.method == "POST":
        addAuthorForm = AddAuthorForm(request.POST, instance=authors)
        if addAuthorForm.is_valid():
            addAuthorForm.save()
            return redirect(manage)

    context = {
        # 'authors': authors,
        'option': 'Update',
        'addAuthorForm': addAuthorForm
    }

    return render(request, authorDetails, context)


def updateBookDetails(request, bookID):
    bookDetails = 'libraryApp/add_book_details.html'

    books = BOOK.objects.get(id=bookID)
    stocks = STOCK.objects.filter(bookID__id=bookID).first()
    addBookForm = AddBookForm(instance=books)
    addStockForm = AddStockForm(instance=stocks)
    if request.method == "POST":
        print("BOOK REQUEST:", request.POST)
        addBookForm = AddBookForm(request.POST, instance=books)

        if addBookForm.is_valid():
            bookID = addBookForm.save()
            print("\nBOOK ID: ", bookID)

            stock = request.POST['bookCopies']

            stocks.bookCopies = stock
            stocks.save()
            return redirect(manage)

    context = {
        'option': 'Update',
        'addBookForm': addBookForm,
        'addStockForm': addStockForm
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

    myFilter = BookFilter(request.GET, queryset=BOOK.objects.all())

    if request.method == "POST":
        print(request.POST)
        return redirect(searchBook, book=request.POST['bookTitle'])

    dbActive = True
    bCount = 0
    rCount = 0

    books = BOOK.objects.all()
    bbList = []
    rbList = []

    # start_time = time.time()
    # print("--- %s seconds SET---" % (time.time() - start_time))

    user = request.user
    if user.is_staff:
        for i in books:
            bb = i.borrowedbook_set.all()
            if bb.exists():
                for j in bb:
                    userName = j.userID.fName + " " + j.userID.mName + " " + j.userID.lName
                    if j.checkIn is None:
                        bCount += 1
                        bbList.append(tempDashboard(
                            None, j.bookID, j.bookID.id, userName, None, None, j.checkOut, None, j.dueDate))
                    else:
                        rCount += 1
                        rbList.append(tempDashboard(
                            None, j.bookID, j.bookID.id, userName, None, None, j.checkOut, j.checkIn, None))
    else:
        borrowedBooks = user.borrowedbook_set.all()
        for i in borrowedBooks:
            if i.checkIn is None:
                bCount += 1
                bbList.append(tempDashboard(
                            None, i.bookID.bookTitle, i.bookID.id, None, None, None, i.checkOut, None, i.dueDate))
            else:
                rCount += 1
                rbList.append(tempDashboard(
                            None, i.bookID.bookTitle, i.bookID.id, None, None, None, i.checkOut, i.checkIn, None))

    context = {
        "borrowedBooks": bbList,
        "bCount": bCount,
        "returnedBooks": rbList,
        "rCount": rCount,
        "myFilter": myFilter,
        "dbActive": dbActive
    }
    return render(request, dashboard, context)


def searchBook(request, book):
    searchResult = 'libraryApp/search_result_page.html'
    books = BOOK.objects.filter(bookTitle__icontains=book)

    myFilter = BookFilter(request.POST, queryset=books)
    if request.method == "POST":
        print(request.POST)
        return redirect(searchBook, book=request.POST['bookTitle'])

    print(books)
    booksList = []
    count = 0

    for i in books:
        count += 1
        stock = STOCK.objects.filter(bookID__id=i.id).first()
        authors = AUTHOR.objects.filter(book__id=i.id)
        authorList = []
        authorIDList = []
        for a in authors.all():
            if a not in authorList:  # loic to check redundancy
                authorList.append(a)
                authorIDList.append(a.id)
        authorString = ', '.join(map(str, authorList))
        #print(i.bookTitle, "of genre", i.genre, "of ID:", i.id, "is published by,", pub.pubName,"of id", pub.id, "and authors are: ", authors, "is having:", stock.bookCopies, "copies")
        booksList.append(tempBook(count, i.bookTitle, i.id, i.genre, i.pubID.id,
                                  i.pubID.pubName, i.pubYear, authorIDList, authorString, i.isbn, stock.bookCopies))

    context = {
        'books': booksList,
        'count': count,
        'query': book,
        'myFilter': myFilter
    }
    return render(request, searchResult, context)


def borrowBook(request):
    borrowBook = 'libraryApp/borrow_book.html'

    books = BOOK.objects.all()

    myFilter = BookFilter(request.GET, queryset=BOOK.objects.all())

    if request.method == "POST":
        print(request.POST)
        return redirect(searchBook, book=request.POST['bookTitle'])

    bbActive = True
    booksList = []
    bookCount = BOOK.objects.count()

    for i in books:
        stock = STOCK.objects.filter(bookID__id=i.id).first()
        authors = AUTHOR.objects.filter(book__id=i.id)
        authorList = []
        authorIDList = []
        for a in authors.all():
            if a not in authorList:  # loic to check redundancy
                authorList.append(a)
                authorIDList.append(a.id)
        authorString = ', '.join(map(str, authorList))
        booksList.append(tempBook(None, i.bookTitle, i.id, i.genre, i.pubID.id,
                                  i.pubID.pubName, i.pubYear, authorIDList, authorString, i.isbn, stock.bookCopies))
        #print("BOOK ID",i.id)
        #print("PUB ID",pub.id)

    context = {
        'books': booksList,
        'count': bookCount,
        "myFilter": myFilter,
        "bbActive": bbActive
    }
    return render(request, borrowBook, context)


def viewBook(request, bookID):
    viewBook = 'libraryApp/view_book.html'

    myFilter = BookFilter(request.GET, queryset=BOOK.objects.all())

    if request.method == "POST":
        print(request.POST)
        return redirect(searchBook, book=request.POST['bookTitle'])

    book = BOOK.objects.get(id=bookID)
    pub = PUBLISHER.objects.filter(book__id=book.id).first()
    stock = STOCK.objects.filter(bookID__id=book.id).first()
    authors = AUTHOR.objects.filter(book__id=book.id)
    authorList = []
    authorIDList = []
    for a in authors.all():
        if a not in authorList:  # loic to check redundancy
            authorList.append(a)
            authorIDList.append(a.id)
    authorString = ', '.join(map(str, authorList))
    bookObject = tempBook(None, book.bookTitle, book.id, book.genre, pub.id, pub.pubName,
                          book.pubYear, authorIDList, authorString, book.isbn, stock.bookCopies)

    user = request.user
    isBookBorrowed = False
    bb = user.borrowedbook_set.filter(bookID__id=bookID)
    if bb.count() > 0:
        bb = bb.all()
        for i in bb:
            if i.checkIn is None:
                isBookBorrowed = True
                break
            else:
                isBookBorrowed = False
    
    context = {
        "book": bookObject,
        "pub": pub,
        "myFilter": myFilter,
        "isBookBorrowed" : isBookBorrowed
    }
    return render(request, viewBook, context)

def requestBorrowBook(request, bookid):
    userID = request.user
    bookID = BOOK.objects.get(id=bookid)
    BORROWEDBOOK.objects.create(userID=userID, bookID=bookID)
    stock = STOCK.objects.filter(bookID=bookID).first()
    stock.bookCopies -= 1
    stock.save()
    #stock updation
    return redirect(dashboard)

def requestReturnBook(request, bookid):
    userID = request.user
    bookID = BOOK.objects.get(id=bookid)
    rb = userID.borrowedbook_set.filter(bookID__id=bookid).all()
    for i in rb:
        if i.checkIn is None:
            i.checkIn = datetime.datetime.now()
            i.save()
    stock = STOCK.objects.filter(bookID=bookID).first()
    stock.bookCopies += 1
    stock.save()
    return redirect(dashboard)

def returnBook(request):
    returnBook = 'libraryApp/return_book.html'

    myFilter = BookFilter(request.GET, queryset=BOOK.objects.all())

    if request.method == "POST":
        print(request.POST)
        return redirect(searchBook, book=request.POST['bookTitle'])

    rbActive = True
    borrowedBooksCount = 0
    bbList = []

    user = request.user
    if not user.is_staff:
        borrowedBooks = user.borrowedbook_set.all()
        for i in borrowedBooks:
            if i.checkIn is None:
                bookid = i.bookID.id
                authors = AUTHOR.objects.filter(book__id=bookid)
                authorList = []
                for a in authors.all():
                    if a not in authorList:  # loic to check redundancy
                        authorList.append(a)
                authorString = ', '.join(map(str, authorList))
                borrowedBooksCount += 1
                bbList.append(tempDashboard(
                            None, i.bookID.bookTitle, bookid, None, authorString, i.bookID.isbn, i.checkOut, None, i.dueDate))
        
    context = {
        "borrowedBooks": bbList,
        "count": borrowedBooksCount,
        "myFilter": myFilter,
        "rbActive": rbActive
    }

    return render(request, returnBook, context)


def signIn(request):
    signIn = 'libraryApp/sign_in.html'
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    if request.POST:
        signInForm = AccountLoginForm(request.POST)
        if signInForm.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect(dashboard)
    else:
        signInForm = AccountLoginForm()
    
    context['signInForm'] = signInForm

    return render(request, signIn, context)

def signOut(request):
    logout(request)
    return redirect(signIn)

def signUp(request):
    signUp = 'libraryApp/sign_up.html'

    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)

    studentSignUpForm = StudentRegistrationForm()
    staffSignUpForm = StaffRegistrationForm()

    if request.method == "POST":
        if 'STAFF' in request.POST:
            data = {"salary": request.POST['salary']}
            staffSignUpForm = StaffRegistrationForm(request.POST, initial=data)

            if staffSignUpForm.is_valid():
                staff = staffSignUpForm.save()
                staff.is_staff = True
                staff.save()
                email = staffSignUpForm.cleaned_data.get('email')
                password = staffSignUpForm.cleaned_data.get('password1')
                account = authenticate(email=email, password=password)
                login(request, account)
                return redirect(dashboard)
        else:
            data = {
                "USN": request.POST['USN'],
                "course": request.POST['course'], 
                "sem": request.POST['sem']}

            studentSignUpForm = StudentRegistrationForm(
                request.POST, initial=data)

            if studentSignUpForm.is_valid():
                studentSignUpForm.save()
                email = studentSignUpForm.cleaned_data.get('email')
                password = studentSignUpForm.cleaned_data.get('password1')
                account = authenticate(email=email, password=password)
                login(request, account)
                return redirect(dashboard)
        print("SIGNUP REQUEST", request.POST)

    context = {
        "studentForm": studentSignUpForm,
        "staffForm": staffSignUpForm
    }
    return render(request, signUp, context)


def manage(request):
    manage = 'libraryApp/manage_tab.html'
    books = BOOK.objects.all()

    myFilter = BookFilter(request.GET, queryset=BOOK.objects.all())

    if request.method == "POST":
        print(request.POST)
        return redirect(searchBook, book=request.POST['bookTitle'])

    allAuthors = AUTHOR.objects.all()
    allPublishers = PUBLISHER.objects.all()

    mActive = True
    booksList = []
    bookCount = 0
    authCount = AUTHOR.objects.count()
    pubCount = PUBLISHER.objects.count()

    for i in books:
        bookCount += 1
        stock = STOCK.objects.filter(bookID__id=i.id).first()
        authors = AUTHOR.objects.filter(book__id=i.id)

        authorList = []
        authorIDList = []
        for a in authors.all():
            #print("AUTH ID",a.id)
            if a not in authorList:  # loic to check redundancy
                authorList.append(a)
                authorIDList.append(a.id)
        authorString = ', '.join(map(str, authorList))
        pub = PUBLISHER.objects.filter(
            book__id=i.id).first()
        #print(i.bookTitle, "of genre", i.genre, "of ID:", i.id, "is published by,", pub.pubName,"of id", pub.id, "and authors are: ", authors, "is having:", stock.bookCopies, "copies")
        booksList.append(tempBook(bookCount, i.bookTitle, i.id, i.genre, pub.id,
                                  pub.pubName, i.pubYear, authorIDList, authorString, i.isbn, stock.bookCopies))
        #print("BOOK ID",i.id)
        #print("PUB ID",pub.id)

    context = {
        'allBooks': booksList,
        'bookCount': bookCount,
        'myFilter': myFilter,
        'allAuthors': allAuthors,
        'authCount': authCount,
        'allPublishers': allPublishers,
        'pubCount': pubCount,
        'mActive': mActive
    }
    return render(request, manage, context)


def deleteAuthorDetails(request, pk):
    author = AUTHOR.objects.get(id=pk)
    name = author.authorName
    author.delete()

    #messages.success(request, 'Author', name,'deleted successfully!')
    return redirect(manage)


def deletePublisherDetails(request, pk):
    pub = PUBLISHER.objects.get(id=pk)
    name = pub.pubName
    pub.delete()

    #messages.success(request, 'Author', name,'deleted successfully!')
    return redirect(manage)


def deleteBookDetails(request, bookID):
    book = BOOK.objects.get(id=bookID)
    name = book.bookTitle
    book.delete()

    #messages.success(request, 'Author', name,'deleted successfully!')
    return redirect(manage)
