from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import views as auth_views
from . import views
from .views import logout_view
from .views import register_view
from .views import login_view

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('register/', views.register, name='register'),  # ✅ Fix: "views.register" required
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # ✅ Fix: "LoginView.as_view(template_name="
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), 
    path('admin-view/', views.admin_view, name='admin_view'),  # ✅ Admin view URL
    path('librarian-view/', views.librarian_view, name='librarian_view'),  # ✅ Librarian view URL
    path('member-view/', views.member_view, name='member_view'),  # ✅ Member view URL
    path('books/add_book/', views.add_book, name='add_book'),  # ✅ Add Book URL
    path('books/edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # ✅ Edit Book URL
    path('books/delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # ✅ Delete Book URL
]
