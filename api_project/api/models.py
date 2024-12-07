from django.db import models

# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} by {self.author}"