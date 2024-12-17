from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Login view using Django's built-in view
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    
    # Logout view using Django's built-in view
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    
    # Custom registration view
    path('register/', views.RegisterView.as_view(), name='register'),
    
    # Custom profile view
    path('profile/', views.ProfileView, name='profile'),
]
