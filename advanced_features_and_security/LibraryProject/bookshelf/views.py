from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import books

@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
    books = books.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('app_name.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(book, pk=pk)
    if request.method == "POST":
        # Add logic for updating the book
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('app_name.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        # Add logic for creating a new book
        pass
    return render(request, 'create_book.html')
@permission_required('app_name.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})

