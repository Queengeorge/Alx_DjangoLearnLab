from relationship_app.models import Author, Book, Library, Librarian

# Create an Author
author = Author.objects.create(name="George Orwell")

# Create Books
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)

# Create a Library
library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)  # Add books to the library

# Create a Librarian
librarian = Librarian.objects.create(name="Alice", library=library)

# Query all books by a specific author
books_by_orwell = Book.objects.filter(author=author)
print("Books by George Orwell:", [book.title for book in books_by_orwell])

# List all books in a library
library_books = library.books.all()
print("Books in Central Library:", [book.title for book in library_books])

# Retrieve the librarian for a library
library_librarian = Librarian.objects.get(library=library)
print("Librarian for Central Library:", library_librarian.name)
