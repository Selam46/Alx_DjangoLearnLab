import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        books = author.books.all()
        return [book.title for book in books]
    return []

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return [book.title for book in library.books.all()]
    return []

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library and hasattr(library, 'librarian'):
        return library.librarian.name
    return None

# Example usage
if __name__ == "__main__":
    print("Books by Author X:", get_books_by_author("Author X"))
    print("Books in Library Y:", get_books_in_library("Library Y"))
    print("Librarian of Library Z:", get_librarian_for_library("Library Z"))
