from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"Author '{author_name}' does not exist."

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # ManyToMany relationship
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        librarian = Librarian.objects.get(library__name=library_name)  # OneToOne relationship
        return librarian.name
    except Librarian.DoesNotExist:
        return f"No librarian found for library '{library_name}'."

