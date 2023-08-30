from django.contrib import admin
from .models import Category, Language


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['id']


admin.site.register(Language, LanguageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description']
    ordering = ['id']


admin.site.register(Category, CategoryAdmin)
