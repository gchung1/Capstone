from django.contrib import admin
from .models import Post, Category



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publish_date', 'status')
    search_fields = ('title', 'body')
    list_filter = ('category', 'status', 'publish_date')
    ordering = ('-publish_date',)
