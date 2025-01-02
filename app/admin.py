from django.contrib import admin
from .models import Post, Category, Comment, Alert, Profile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Alert)
admin.site.register(Profile)
