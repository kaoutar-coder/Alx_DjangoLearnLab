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
    ('Admin'),
    ('Librarian'),
    ('Member')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"



