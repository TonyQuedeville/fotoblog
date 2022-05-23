from django.contrib import admin
from blog.models import Photo, Blog

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'uploader')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')

admin.site.register(Blog, BlogAdmin)
