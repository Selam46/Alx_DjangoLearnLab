from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # ✅ List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # ✅ Get book details
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # ✅ Create book
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # ✅ Update book
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # ✅ Delete book
]
