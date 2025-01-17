# CRUD Operations in Django Shell

## Create Operation
**Command**:
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

## Retrieve Operation

**Command**:
```python
books = Book.objects.all()
for book in books:
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

## Update Operation

**Command**:
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

## Delete Operation 

**Command**:
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())


