import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Using .get() to match the expected query
        books = Book.objects.filter(author=author)  # Explicitly filtering books by the author
        return [book.title for book in books]
    except Author.DoesNotExist:
        return []

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Using .get() to match the expected query
        return [book.title for book in library.books.all()]
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Using .get() as required
        librarian = Librarian.objects.get(library=library)  # Ensuring the librarian lookup is explicit
        return librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage
if __name__ == "__main__":
    print("Books by Author X:", get_books_by_author("Author X"))
    print("Books in Library Y:", get_books_in_library("Library Y"))
    print("Librarian of Library Z:", get_librarian_for_library("Library Z"))
