from django.contrib import admin
from .models import Post, Category
# Register your models here.
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Author', 'Date', 'Description', 'Image', 'Content', 'category']
    fields = ['Title', 'Author', 'Date', 'Description', 'Image', 'Content', 'category']
@admin.register(Category)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['Name', 'slug', 'parent']

