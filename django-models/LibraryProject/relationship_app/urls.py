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
]
