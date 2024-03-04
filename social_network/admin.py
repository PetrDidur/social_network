from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from social_network.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'author', 'created_at')
    list_display_links = ['author']
    list_filter = ('created_at',)




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'created_at')

