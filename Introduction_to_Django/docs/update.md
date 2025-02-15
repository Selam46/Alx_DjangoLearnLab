# Update Book Title
from bookshelf.models import Book

# Retrieve the Book Instance by title
book = Book.objects.get(title="1984")

# Update the book's title
book.title = "Nineteen Eighty-Four"
book.save()

# Print the updated title
print(f"Updated Title: {book.title}")

# Expected Output:
# Updated Title: Nineteen Eighty-Four
