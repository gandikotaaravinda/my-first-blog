from django.contrib import admin
from .models import Post

class MyAdminSite(admin.AdminSite):
	admin.site.register(Post)

# Register your models here.
