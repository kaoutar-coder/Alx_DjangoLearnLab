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


# model user
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)


