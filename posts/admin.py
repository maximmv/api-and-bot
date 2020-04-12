from django.contrib import admin
from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body', 'created')
    fields = ('title', 'author', 'body', 'created')
    readonly_fields = ['created', ]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'like', 'created')
    fields = ('author', 'post', 'like', 'created')
    readonly_fields = ['created', ]
