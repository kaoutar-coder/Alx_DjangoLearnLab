
from django.shortcuts import render

from django.views.generic.detail import DetailView






# Function-based view
from .models import Book
def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
from .models import Library

class LibraryListView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'