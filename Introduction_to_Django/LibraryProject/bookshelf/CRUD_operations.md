# Create a Book Instance

## Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)  # Should print: 1984

# Retrieve a Book Instance

## Command:
```python
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

# Update a Book Instance

## Command:
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)  # Should print: Nineteen Eighty-Four 

# Delete a Book Instance

## Command:
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())  # Should return an empty QuerySet 

