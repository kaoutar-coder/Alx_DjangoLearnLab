# Delete a Book Instance

## Command:
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())  # Should return an empty QuerySet 
