# Deleting a Book Instance

### Command:
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check if deletion was successful
print(Book.objects.all())

# Expected Output:
# <QuerySet []>
