from django.contrib import admin
from .models import Practice, Principle, Products, Experience
from modeltranslation.admin import TranslationAdmin


@admin.register(Practice)
class PracticeAdmin(TranslationAdmin):
    list_display = ("title", "description")








