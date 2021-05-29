from django.contrib import admin
from .models import Category, Post, Author, Comment, PostCategory


admin.site.register([Post, Author, Category, Comment, PostCategory])
