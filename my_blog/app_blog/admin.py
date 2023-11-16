from django.contrib import admin

from app_blog.models import PostCategory, Post

admin.site.register(PostCategory)
admin.site.register(Post)
