from account.models import Account
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
import datetime
# Create your models here.
# null = True is only for testing
# not needed since django provides a way to store users
# check to either CASCADE or not


class STAFF(models.Model):
    staffEmail = models.EmailField(max_length=50, unique=True, help_text="Email id")

    def __str__(self):
        return self.staffEmail

class PUBLISHER(models.Model):
    pubName = models.CharField(max_length=30, help_text="Publisher name", null=True)
    streetAddr = models.CharField(max_length=50, help_text="Street Address", null=True)
    district = models.CharField(max_length=20, help_text="District", null=True)
    state = models.CharField(max_length=20, help_text="State", null=True)
    pinCode = models.CharField(max_length=6, help_text="PIN Code", null=True)
    phoneNum = models.CharField(max_length=10, help_text="Phone number", null=True)

    def __str__(self):
        return self.pubName

class AUTHOR(models.Model):
    authorName = models.CharField(max_length=30, help_text="Author name")

    def __str__(self):
        return self.authorName

class BOOK(models.Model):
    GENRE = (
        ("CS", "Computer Science"),
        ("MATH", "Mathematics"),
        ("ELE", "Electronics"),
        ("TC", "Telecommunication"),
        ("CHE", "Chemistry"),
        ("PHY", "Physics"),
        ("MEC", "Mechanics"),
        ("EVS", "Environmental Science"),
        ("BIO", "Bioengineering"),
        ("BUS", "Business Skills"),
    )
    bookTitle = models.CharField(max_length=50, help_text="Book Title")
    genre = models.CharField(max_length=30, null=True, choices=GENRE, help_text="Category")
    pubYear = models.CharField(max_length=4, null=True, help_text="Year of publication")
    isbn = models.CharField(max_length=13, null=True, unique=True, help_text="International Standard Book Number")
    librarianID = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, help_text="Librarian ID")
    pubID = models.ForeignKey(PUBLISHER, null=True, on_delete=models.CASCADE, help_text="Publisher ID")
    authorID = models.ManyToManyField(AUTHOR, help_text="Authors")
    # isAvail = models.BooleanField()

    def __str__(self):
        return self.bookTitle


class STOCK(models.Model):
    bookCopies = models.PositiveSmallIntegerField(default=0, help_text="Number of the Book copies")
    bookID = models.OneToOneField(BOOK, null=True, on_delete=models.CASCADE, help_text="Book ID")
    librarianID = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, help_text="Librarian ID")


# class WRITTENBY(models.Model):
#     bookID = models.ManyToManyField(BOOK)
#     authorID = models.ManyToManyField(AUTHOR)


class BORROWEDBOOK(models.Model):
    checkOut = models.DateTimeField(auto_now_add=True, null=True, help_text="Check out date")
    dueDate = models.DateTimeField(null=True, blank=True, help_text="Due date")
    checkIn = models.DateTimeField(auto_now_add=False, null=True, blank=True, help_text="Check in date")
    userID = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, help_text="User ID")
    bookID = models.ForeignKey(BOOK, null=True, on_delete=models.CASCADE, help_text="Book ID")

    def save(self, *args, **kwargs):
        self.dueDate = datetime.datetime.now()+datetime.timedelta(days=14) # original answer used this line: self.created + datetime.timedelta(365).isoformat()
        super(BORROWEDBOOK, self).save(*args, **kwargs) # Call the "real" save() method.


class defaultValues(models.Model):
    # coursesAll = models.CharField(max_length=30, null=True)
    # genreAll = models.CharField(max_length=20, null=True)
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
