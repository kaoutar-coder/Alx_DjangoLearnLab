from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title




# Create a custom user model by extending AbstractUser, adding custom fields that are relevant to your application’s needs.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username



"class CustomUser(AbstractUser):", "date_of_birth", "profile_photo"

# Create User Manager for Custom User Model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user with the provided email, username, and password.
        """
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser with the provided email, username, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


    def __str__(self):
        return self.username




# Django provides the ability to add custom permissions to models using the permissions attribute in the Meta class of a model.
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("can_view", "Can view document"),
            ("can_create", "Can create document"),
            ("can_edit", "Can edit document"),
            ("can_delete", "Can delete document"),
        ]
    
    def __str__(self):
        return self.title


# management/commands/configure_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Create user groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Define groups and their permissions
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_edit", "can_create"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in permissions:
                try:
                    permission = Permission.objects.get(codename=perm)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stderr.write(f"Permission '{perm}' does not exist.")
            group.save()
            self.stdout.write(f"Group '{group_name}' configured successfully.")

        self.stdout.write("All groups configured with permissions!")