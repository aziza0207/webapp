from django.contrib import admin
from django.utils.html import format_html
from .models import Practice, Principle, Products, Experience, Contacts, Value, Photo, Video
from modeltranslation.admin import TranslationAdmin


@admin.register(Practice)
class PracticeAdmin(TranslationAdmin):

    list_display = ("title", "description", )

    group_fieldsets = True

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Principle)
class PrincipleAdmin(TranslationAdmin):
    list_display = ("title",)

    group_fieldsets = True

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Products)
class ProductsAdmin(TranslationAdmin):
    list_display = ("title",)

    group_fieldsets = True

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Experience)
class ExperienceAdmin(TranslationAdmin):
    list_display = ("title",)

    group_fieldsets = True

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Contacts)
class ContactsAdmin(TranslationAdmin):
    list_display = ("address",)

    group_fieldsets = True

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Value)
class ValueAdmin(TranslationAdmin):
    list_display = ("title",)

    group_fieldsets = True

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class PhotoAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.url.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', ]


admin.site.register(Photo, PhotoAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ['url']


admin.site.register(Video, VideoAdmin)
