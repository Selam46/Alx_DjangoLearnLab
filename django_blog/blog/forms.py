from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from taggit.forms import TagWidget

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'class': 'form-control', 'placeholder': 'Add tags (comma-separated)'})
        }

    def save(self, commit=True):
        post = super().save(commit=False)
        tag_list = self.cleaned_data['tags'].split(',')
        if commit:
            post.save()
            post.tags.set(tag_list)  
        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
