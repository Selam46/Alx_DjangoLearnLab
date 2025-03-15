from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    Accessible to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by its ID.
    Accessible to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CreateView: Add a new book (Restricted to authenticated users)
class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can create

# UpdateView: Modify an existing book (Restricted to authenticated users)
class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# DeleteView: Remove a book (Restricted to authenticated users)
class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
