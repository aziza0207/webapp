from django.contrib import admin
from .models import Practice, Language, Principle, Products, Experience


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['id']


admin.site.register(Language, LanguageAdmin)


class PracticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description']
    ordering = ['id']


admin.site.register(Practice, PracticeAdmin)


class PrincipleAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['id']


admin.site.register(Principle, PrincipleAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['id']


admin.site.register(Products, ProductsAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['id']


admin.site.register(Experience, ExperienceAdmin)
