from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book
from .models import Library
# ✅ Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()  # Get all books
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Correct template path

# ✅ Class-Based View for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Correct template path
    context_object_name = 'library'  # Ensures correct context name
