
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


    # CREAT LoginView

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = 'login.html'

# CREAT LogoutView
from django.contrib.auth.views import LogoutView


class UserLogoutView(LogoutView):
    template_name = 'logout.html'



# Custom Registration View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Replace 'home' with your app's homepage view name
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



#Set Up Role-Based Views

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def check_role(role):
    def inner_check(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return inner_check

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'member_view.html')
