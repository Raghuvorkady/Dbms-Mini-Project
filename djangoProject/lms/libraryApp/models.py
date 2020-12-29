from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings

from django.dispatch import receiver
from django.db.models.signals import post_save

import datetime

# Create your models here.
# null = True is only for testing
# not needed since django provides a way to store users
# check to either CASCADE or not


class STAFF(models.Model):
    staffEmail = models.EmailField(
        max_length=50, unique=True, help_text="Email id")

    def __str__(self):
        return self.staffEmail


class PUBLISHER(models.Model):
    pubName = models.CharField(
        max_length=30, help_text="Publisher name", null=True)
    streetAddr = models.CharField(
        max_length=50, help_text="Street Address", null=True)
    district = models.CharField(max_length=20, help_text="District", null=True)
    state = models.CharField(max_length=20, help_text="State", null=True)
    pinCode = models.CharField(max_length=6, help_text="PIN Code", null=True, validators=[RegexValidator(
        regex='[0-9]{6}', message="Enter a valid Postal Identification Number", code="invalid_pinCode")])
    phoneNum = models.CharField(
        max_length=10, help_text="Phone number", null=True, validators=[
            RegexValidator(regex='[0-9]{10}', message="Enter a valid Phone Number", code="invalid_phoneNum")])
    # validators for pinCode, phoneNum

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
    genre = models.CharField(max_length=30, null=True,
                             choices=GENRE, help_text="Category")
    pubYear = models.CharField(
        max_length=4, null=True, help_text="Year of publication")
    isbn = models.CharField(max_length=13, null=True, unique=True,
                            help_text="International Standard Book Number")
    librarianID = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, help_text="Librarian ID")
    pubID = models.ForeignKey(
        PUBLISHER, null=True, on_delete=models.CASCADE, help_text="Publisher ID")
    authorID = models.ManyToManyField(AUTHOR, help_text="Authors")
    # validators for isbn, pubYear

    def __str__(self):
        return self.bookTitle


class STOCK(models.Model):
    bookCopies = models.PositiveSmallIntegerField(
        default=0, help_text="Number of the Book copies")
    bookID = models.OneToOneField(
        BOOK, null=True, on_delete=models.CASCADE, help_text="Book ID")
    librarianID = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, help_text="Librarian ID")


class BORROWEDBOOK(models.Model):
    checkOut = models.DateTimeField(
        auto_now_add=True, null=True, help_text="Check out date")
    dueDate = models.DateTimeField(null=True, blank=True, help_text="Due date")
    checkIn = models.DateTimeField(
        auto_now_add=False, null=True, blank=True, help_text="Check in date")
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, help_text="User ID")
    bookID = models.ForeignKey(
        BOOK, null=True, on_delete=models.CASCADE, help_text="Book ID")

    def save(self, *args, **kwargs):
        # original answer used this line: self.created + datetime.timedelta(365).isoformat()
        self.dueDate = datetime.datetime.now()+datetime.timedelta(days=14)
        # Call the "real" save() method.
        super(BORROWEDBOOK, self).save(*args, **kwargs)


@receiver(post_save, sender=AUTHOR)
def onAuthorInsertion(sender, instance, **kwargs):
    auth = instance.authorName
    print("Author added", auth)
    
@receiver(post_save, sender=PUBLISHER)
def onAuthorInsertion(sender, instance, **kwargs):
    pub = instance.pubName
    print("Publisher added", pub)

@receiver(post_save, sender=BOOK)
def onBookInsertion(sender, instance, **kwargs):
    bookTitle = instance.bookTitle
    print("Book added", bookTitle)
