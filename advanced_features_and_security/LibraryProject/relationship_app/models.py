from django.db import models

# Create your models here.

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author

    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")  # One-to-Many with Author

    def __str__(self):
        return self.title

# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)  # Name of the library
    books = models.ManyToManyField(Book, related_name="libraries")  # Many-to-Many with Book

    def __str__(self):
        return self.name

# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)  # Name of the librarian
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")  # One-to-One with Library

    def __str__(self):
        return self.name


#Extend the User Model with a UserProfile

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"






# task 4 
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title


# Create a custom user model by extending AbstractUser, adding custom fields that are relevant to your application’s needs.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username




# Create User Manager for Custom User Model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user with the provided email, username, and password.
        """
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser with the provided email, username, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


    def __str__(self):
        return self.username


