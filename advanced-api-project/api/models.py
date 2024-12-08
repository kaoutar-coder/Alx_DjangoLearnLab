

# Create your models here.


from django.db import models

class Author(models.Model):
    """
    Represents an author entity with a name field.
    Each author can have multiple books associated with them.
    """
    name = models.CharField(max_length=255)  # Name of the author

    def __str__(self):
        return self.name  # Returns the author's name as a string


class Book(models.Model):
    """
    Represents a book entity with a title, publication year, and a foreign key to an Author.
    The foreign key establishes a one-to-many relationship, where one author can have multiple books.
    """
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # The 'author' field links the book to its author.
    # 'on_delete=models.CASCADE' ensures books are deleted if the related author is deleted.
    # 'related_name="books"' allows reverse lookup from the Author model to access all related books.

    def __str__(self):
        return self.title  # Returns the book's title as a string