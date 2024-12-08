from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"
from .models import Book
from .serializers import BookSerializer





class BookListView(generics.ListAPIView):
    """
    View to list all books in the database.
    Allows read-only access to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No restrictions for read-only access


class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by its ID.
    Allows read-only access to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No restrictions for read-only access

    class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book in the database.
    Restricted to authenticated users.
    Includes permission checks and custom validation.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create books

    def perform_create(self, serializer):
        if serializer.validated_data['publication_year'] > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book in the database.
    Restricted to authenticated users.
    Includes permission checks and custom validation.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update books

    def perform_update(self, serializer):
        if serializer.validated_data.get('publication_year', date.today().year) > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book from the database.
    Restricted to authenticated users.
    Includes permission checks.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete books



from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


### API Query Parameters

#### Filtering
#- `?title=<title>`
#- `?author=<author>`
#- `?publication_year=<year>`

#### Searching
#- `?search=<search-term>` (Searches `title` and `author` fields)

#### Ordering
#- `?ordering=title` (Ascending by title)
#- `?ordering=-publication_year` (Descending by publication year)


