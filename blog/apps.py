from __future__ import unicode_literals
from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class MyAdminConfig(AdminConfig):
    default_site = 'myproject.admin.MyAdminSite'

class BlogConfig(AppConfig):
    name = 'blog'
