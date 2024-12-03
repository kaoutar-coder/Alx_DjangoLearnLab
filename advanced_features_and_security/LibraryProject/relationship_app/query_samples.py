import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")


def list_books_in_library(library_name):
    """List all books in a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in library '{library_name}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")


def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for library '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library '{library_name}'.")


# Sample calls
if __name__ == "__main__":
    # Replace with actual data to test
    query_books_by_author("Author Name")
    list_books_in_library("Library Name")
    retrieve_librarian_for_library("Library Name")
 
