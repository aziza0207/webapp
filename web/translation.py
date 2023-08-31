from .models import Practice
from modeltranslation.translator import TranslationOptions, register


@register(Practice)
class TranslationsOptions(TranslationOptions):
    fields = ("title", "description")
