from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth import views as auth_views
from .views import logout_view
from .views import register_view
from .views import login_view

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('register/', register_view, name='register'),  # User registration
    path('login/', login_view, name='login'),  # User login
    path('logout/', logout_view, name='logout'),  # User logout
]
