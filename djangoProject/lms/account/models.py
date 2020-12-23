from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, fName, password=None):
        if not email:
            raise ValueError("Users must have email address")
        if not username:
            raise ValueError("Users must have username")
        if not fName:
            raise ValueError("Users must have first name")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            fName=fName
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, fName, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            fName=fName
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    COURSES = (
        ("ISE","Information Science Engineering"),
        ("CSE","Computer Science Engineering"),
        ("ECE","Electronics and Communication Engineering"),
        ("ME","Mechanical Engineering"),
        ("ETE","Electronics and Telecommunication Engineering"),
        ("EEE","Electrical and Electronics Engineering"),
        ("CIV","Civil Engineering"),
        ("MCA","Master of Computer Applications"),
        ("AI&ML","Artificial Intelligence and Machine Learning")
    )
    SEM = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
    )
    
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    username = models.CharField(max_length=30, unique=True)
    fName = models.CharField(max_length=20, help_text='first name')
    mName = models.CharField(max_length=20, help_text='middle name')
    lName = models.CharField(max_length=20, help_text='last name')
    streetAddr = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    pinCode = models.CharField(max_length=6, null=True)
    phoneNum = models.CharField(max_length=10, null=True)

    USN = models.CharField(max_length=10, null=True, unique=True)
    course = models.CharField(max_length=50, null=True, choices=COURSES)
    sem = models.PositiveSmallIntegerField(null=True, choices=SEM)
    salary = models.CharField(max_length=6, null=True)
    
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'fName']

    objects = MyAccountManager()    

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(elf, app_label):
        return True