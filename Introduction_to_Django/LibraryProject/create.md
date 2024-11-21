Commande ECHO activ�e.
# CREATE Operation

## Commande utilisée
```python
from bookshelf.models import Book

# Création d'un nouvel objet Book
new_book = Book(title="Django for Beginners", author="William S. Vincent", publication_year=2024)
new_book.save()
