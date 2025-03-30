from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404  # Ensure we are using the correct import
from django.contrib.auth import get_user_model
from .models import Post, Like
from notifications.models import Notification  # Fix: Import Notification model directly
from notifications.utils import create_notification  # Make sure you have a utility method to create notifications

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Fix: Retrieve the Post using get_object_or_404
        post = get_object_or_404(Post, pk=pk)

        # Ensure that the user doesn't like the post more than once
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"message": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Fix: Directly create a Notification object (Notification.objects.create)
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked",
            target=post
        )

        return Response({"message": "Post liked successfully"}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Fix: Retrieve the Post using get_object_or_404
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has liked the post and remove the like
        like = Like.objects.filter(user=request.user, post=post)

        if like.exists():
            like.delete()
            return Response({"message": "Post unliked successfully"}, status=status.HTTP_200_OK)

        return Response({"message": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)
