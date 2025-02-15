from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in the admin list view
    search_fields = ('title', 'author')  # Allow searching by title and author
    list_filter = ('publication_year',)  # Add a filter by publication year
