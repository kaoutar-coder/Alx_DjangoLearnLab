from django.contrib import admin

# Register your models here.

from .models import Author, Book, Library, Librarian

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)


# TASK 4

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_date']






