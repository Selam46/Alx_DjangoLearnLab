]from django.urls import path
from .views import register_view, login_view, logout_view, profile_view
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView, CommentCreateView, 
    CommentUpdateView, CommentDeleteView, search_posts, PostListView
)
urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"), 
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/comments/new/", CommentCreateView, name="CommentCreateView"),
    path("comment/<int:pk>/update/", CommentUpdateView, name="CommentUpdateView"),
    path("comment/<int:pk>/delete/", CommentDeleteView, name="CommentDeleteView"),
    path("", PostByTagListView.as_view(), name="post_list"),
    path("search/", search_posts, name="search_posts"),
    path("tags/<slug:tag_slug>/", PostListView.as_view(), name="posts_by_tag"),
]



