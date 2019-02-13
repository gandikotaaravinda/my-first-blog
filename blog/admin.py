from django.contrib import admin
from .models import Post, Comment

class MyAdminSite(admin.AdminSite):
	admin.site.register(Post)
	admin.site.register(Comment)

# Register your models here.
