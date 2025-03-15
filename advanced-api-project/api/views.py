from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Allow unauthenticated users to view books
class BookListView(generics.ListAPIView):
    """
    API view to retrieve list of books.
    Accessible to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Explicitly allow all users

class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by ID.
    Accessible to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Explicitly allow all users

# Restrict modification actions to authenticated users
class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users
