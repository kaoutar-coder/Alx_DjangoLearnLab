# Update a Book Instance

## Command:
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)  # Should print: Nineteen Eighty-Four 
