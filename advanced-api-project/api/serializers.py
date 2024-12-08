from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model. Serializes all fields of the Book model.
    Includes custom validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields in the Book model

    def validate_publication_year(self, value):
        """
        Custom validator for the publication_year field.
        Ensures the publication year is not greater than the current year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):  
    """
    Serializer for the Author model.
    Includes the author's name and a nested representation of related books using the BookSerializer.
    The nested relationship is established dynamically based on the related_name="books" in the Book model.
    """
    books = BookSerializer( many=True, read_only=True, source='books')

    # 'books' field uses the BookSerializer to serialize related books.
    # 'many=True' indicates the relationship is one-to-many.
    # 'read_only=True' ensures books can only be viewed, not modified through the AuthorSerializer.

    class Meta:
        model = Author
        fields = ['name', 'books']  # Includes the name and the nested list of books

       