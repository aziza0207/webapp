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


class Contacts(models.Model):
    phone = models.CharField(_("phone"), max_length=12)
    email = models.EmailField(_("email"))
    address = models.CharField(_("address"), max_length=100)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Value(models.Model):
    title = models.CharField(_("title"), max_length=100)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ценность'
        verbose_name_plural = 'Ценности'


class Photo(models.Model):
    url = models.ImageField(_("image"), upload_to='images/')



    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Video(models.Model):
    url = models.ImageField(_("image"), upload_to='images/')



    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
