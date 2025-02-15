# Delete the Book Instance
from bookshelf.models import Book

# Retrieve the Book Instance by title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Print all books in the database
print(Book.objects.all())  # Should return an empty queryset

# Expected Output:
# <QuerySet []>
