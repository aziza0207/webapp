from django.db import models
from django.utils.translation import gettext as _


class Practice(models.Model):
    title = models.CharField(_("title"), max_length=100)
    image = models.ImageField(_("image"), upload_to='images/', null=True, blank=True)
    description = models.TextField(_("description"), max_length=500)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельности'


class Experience(models.Model):
    title = models.CharField(_("title"), max_length=100)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'


class Principle(models.Model):
    title = models.CharField(_("title"), max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Принцип'
        verbose_name_plural = 'Принципы'


class Products(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"), max_length=100)
    image = models.ImageField(_("image"), upload_to='images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
