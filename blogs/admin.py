from django.contrib import admin
from .models import Blog, Comment
admin.site.register(Blog)

@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'blog','created', 'active']
    list_filter = ['active','created', 'update' ]
    search_fields = ['name', 'email', 'body']
