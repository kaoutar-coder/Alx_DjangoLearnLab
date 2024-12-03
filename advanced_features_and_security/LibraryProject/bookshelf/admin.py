from django.contrib import admin

# Register your models here.




# Register the Book model with the admin interface


from .models import Book

# Custom admin class to configure how Book is displayed
class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication_year in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters based on publication_year
    list_filter = ('publication_year',)
    
    # Enable search functionality on title and author
    search_fields = ('title', 'author')

# Register the Book model with custom configurations
admin.site.register(Book, BookAdmin)

