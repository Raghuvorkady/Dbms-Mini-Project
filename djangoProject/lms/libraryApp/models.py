from django.db import models

# Create your models here.
# null = True is only for testing
# not needed since django provides a way to store users
# check to either CASCADE or not


class STAFF(models.Model):
    staffEmail = models.CharField(max_length=20)

    def __str__(self):
        return self.staffEmail


class USER(models.Model):
    choicesInCourse = [
        ("ISE", "Information Science Engineering"),
        ("CSE", "Computer Science Engineering"),
        ("ECE", "Electronics and Communication Engineering"),
        ("ME", "Mechanical Engineering"),
    ]
    choicesInSem = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
    ]
    fName = models.CharField(max_length=20)
    mName = models.CharField(max_length=20)
    lName = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=20)
    streetAddr = models.CharField(max_length=50)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pinCode = models.CharField(max_length=6)
    phoneNum = models.CharField(max_length=10)
    USN = models.CharField(max_length=10)
    course = models.CharField(
        max_length=3,
        choices=choicesInCourse,
    )
    sem = models.IntegerField(
        choices=choicesInSem,
    )

    def __str__(self):
        return self.email


class LIBRARIAN(models.Model):
    fName = models.CharField(max_length=20)
    mName = models.CharField(max_length=20)
    lName = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=20)
    streetAddr = models.CharField(max_length=50)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pinCode = models.CharField(max_length=6)
    phoneNum = models.CharField(max_length=10)
    salary = models.CharField(max_length=6)

    def __str__(self):
        return self.email


class PUBLISHER(models.Model):
    pubName = models.CharField(max_length=30)
    streetAddr = models.CharField(max_length=50)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pinCode = models.CharField(max_length=6)
    phoneNum = models.CharField(max_length=10)

    def __str__(self):
        return self.pubName


class BOOK(models.Model):
    bookTitle = models.CharField(max_length=50)
    genre = models.CharField(max_length=30, null=True)
    pubYear = models.CharField(max_length=4, null=True)
    isbn = models.CharField(max_length=13, null=True)
    librarianID = models.ForeignKey(
        LIBRARIAN, null=True, on_delete=models.SET_NULL)
    pubID = models.ForeignKey(PUBLISHER, null=True, on_delete=models.CASCADE)
    #isAvail = models.BooleanField()

    def __str__(self):
        return self.bookTitle


class AUTHOR(models.Model):
    authorName = models.CharField(max_length=30)

    def __str__(self):
        return self.authorName


class STOCK(models.Model):
    bookCopies = models.IntegerField()
    bookID = models.OneToOneField(BOOK, null=True, on_delete=models.CASCADE)
    librarianID = models.ForeignKey(
        LIBRARIAN, null=True, on_delete=models.SET_NULL)


class WRITTENBY(models.Model):
    dateAdded = models.DateTimeField(auto_now_add=True, null=True)
    bookID = models.ManyToManyField(BOOK)
    authorID = models.ManyToManyField(AUTHOR)


class BORROWEDBOOK(models.Model):
    checkOut = models.DateTimeField(auto_now_add=True, null=True)
    dueDate = models.DateTimeField(auto_now_add=True, null=True)
    checkIn = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    userID = models.ForeignKey(USER, null=True, on_delete=models.SET_NULL)
    bookID = models.ForeignKey(BOOK, null=True, on_delete=models.SET_NULL)


class defaultValues(models.Model):
    courses = (
        "Information Science Engineering",
        "Computer Science Engineering",
        "Electronics and Communication Engineering",
        "Mechanical Engineering",
        "Electronics and Telecommunication Engineering",
        "Electrical and Electronics Engineering",
        "Civil Engineering",
        "Master of Computer Applications",
        "Artificial Intelligence and Machine Learning"
    )

    genre = (
        "History",
        "Math",
        "Science",
        "Travel",
        "Business",
        "Coding"
    )
    """
    statesInIndia = [
        ('KA', 'Karnataka'), 
        ('AP', 'Andhra Pradesh'), 
        ('KL', 'Kerala'), 
        ('TN', 'Tamil Nadu'),
        ('MH', 'Maharashtra'),
        ('UP', 'Uttar Pradesh'),
        ('GA', 'Goa'), 
        ('GJ', 'Gujarat'), 
        ('RJ', 'Rajasthan'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('TG', 'Telangana'), 
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'), 
        ('BR', 'Bihar'), 
        ('CG', 'Chattisgarh'),
        ('HR', 'Haryana'),
        ('JH', 'Jharkhand'), 
        ('MP','Madhya Pradesh'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Orissa'), 
        ('PB', 'Punjab'), 
        ('SK', 'Sikkim'), 
        ('TR', 'Tripura'), 
        ('UA', 'Uttarakhand'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar'), 
        ('CH', 'Chandigarh'), 
        ('DN', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'), 
        ('DL', 'Delhi'), 
        ('LD', 'Lakshadweep'),
        ('PY', 'Pondicherry')
    ]"""
    statesInIndia = ("Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
                     "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "Delhi", "Puducherry")

    districtInKerala = [
        ("Ksd", "Kasaragod"),
    ]
