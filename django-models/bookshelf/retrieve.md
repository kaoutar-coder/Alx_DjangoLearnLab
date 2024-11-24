# Retrieve a Book Instance

## Command:
```python
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")