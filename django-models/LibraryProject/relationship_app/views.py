from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from .models import Book

# Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'list_books.html', {'books': books})

# Class-Based View to Show Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'  # This is used in the template
