"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include

from .views import list_books, LibraryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),  # Inclure les URL de l'application
]


# CONFEGURATION URL


from django.urls import path
from .views import UserLoginView, UserLogoutView, register

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]



#URL Configuration

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]


# task 4

from django.urls import path
from . import views

urlpatterns = [
    path('books/add_book/', views_add_book, name='add_book'),
    path('books/<int:book_id>/edit_book/', views_edit_book, name='edit_book'),
    path('books/<int:book_id>/delete_book/', views.delete_book, name='delete_book'),
    path('books/', views.book_list, name='book_list'),  # Vue pour lister les livres
]
