from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Post
from .forms import PostForm

@permission_required('blog.can_view', raise_exception=True)
def view_post(request, post_id):
    # Only users with the 'can_view' permission can view posts
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/view_post.html', {'post': post})

@permission_required('blog.can_create', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to list of posts
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@permission_required('blog.can_edit', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to list of posts
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

@permission_required('blog.can_delete', raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('post_list')  # Redirect to list of posts
