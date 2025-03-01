from django import forms
from .models import Post, Book

# ExampleForm for creating or updating posts
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Post  # Or Book if you're working with books
        fields = ['title', 'content']  # Specify the fields you want in the form
