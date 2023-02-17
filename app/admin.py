from django.contrib import admin

from .models import Category, Tag, Blog, Comment


@admin.register(Category)
class Categoey(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['name', 'slug']


admin.site.register(Blog)
admin.site.register(Comment)
