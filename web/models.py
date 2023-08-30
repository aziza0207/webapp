from django.db import models
from django.utils.translation import gettext as _


class Language(models.Model):
    title = models.CharField(_("title"), max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Category(models.Model):
    title = models.CharField(_("title"), max_length=100)
    image = models.ImageField(_("image"), upload_to='images/', null=True, blank=True)
    description = models.TextField(_("description"), max_length=500)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
