"""
URL configuration for api_project project.

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
     path('api/', include('api.urls')),    # Includes API routes
    
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view

]


from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')



from django.urls import include, path
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),    # Includes API routes
]



urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include (router.urls)),  # This includes all routes registered with the router
]

from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Other URL patterns
    path('api/token/', obtain_auth_token, name='api_token'),  # Token retrieval endpoint
]


