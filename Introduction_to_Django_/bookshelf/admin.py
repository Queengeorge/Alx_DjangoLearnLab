from django.contrib import admin
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display fields in the list view
    list_filter = ('author', 'publication_year')  # Filters on the right side of the list view
    search_fields = ('title', 'author')  # Enable search functionality
