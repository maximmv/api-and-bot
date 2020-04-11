from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body', 'created')
    fields = ('title', 'author', 'body', 'created')
    readonly_fields = ['created', ]
