from .models import Practice, Principle, Experience, Products
from modeltranslation.translator import TranslationOptions, register


@register(Practice)
class TranslationsOptions(TranslationOptions):
    fields = ("title", "description")


@register(Principle)
class TranslationsOptions(TranslationOptions):
    fields = ("title",)


@register(Products)
class TranslationsOptions(TranslationOptions):
    fields = ("title", "description")


@register(Experience)
class TranslationsOptions(TranslationOptions):
    fields = ("title",)
