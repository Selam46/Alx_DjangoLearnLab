from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# ✅ List all books (Anyone can read)
class BookListView(generics.ListAPIView):
    """
    API view to retrieve list of books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ✅ Retrieve a single book by ID (Anyone can read)
class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ✅ Create a new book (Authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# ✅ Update an existing book (Authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# ✅ Delete a book (Authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
