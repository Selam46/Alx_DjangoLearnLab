from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# ✅ Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Correct path

# ✅ Class-Based View to Show Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Correct path
    context_object_name = 'library'  # Used in the template
