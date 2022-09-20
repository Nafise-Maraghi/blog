from django.contrib import admin

from .models import Author, Post


@admin.register(Author)
class UserAdmin(admin.ModelAdmin):
    fields = ['__all__']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['__all__']
