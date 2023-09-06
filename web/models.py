from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import gettext as _


class Practice(models.Model):
    """ Модель описывает деятельность компании """

    title = models.CharField(_("title"), max_length=100)
    image = models.ImageField(_("image"), help_text="Разрешение 1600x1300", upload_to='images/', null=True, blank=True)
    description = models.TextField(_("description"), max_length=500)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельности'


class Experience(models.Model):
    """ Модель описывает опыт компании """

    title = models.CharField(_("title"), max_length=120)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'


class Principle(models.Model):
    """ Модель описывает принципы компании """

    title = models.CharField(_("title"), max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Принцип'
        verbose_name_plural = 'Принципы'


class Products(models.Model):
    """ Модель описывает продукты компании """

    title = models.CharField(_("title"), max_length=25)
    description = models.TextField(_("description"), max_length=100)
    image = models.ImageField(_("image"), help_text="Разрешение 250x200", upload_to='images/', null=True, blank=True)
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
    """ Модель описывает ценности компании """

    title = models.CharField(_("title"), max_length=100)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ценность'
        verbose_name_plural = 'Ценности'


class Photo(models.Model):
    url = models.ImageField(_("image"), help_text="Разрешение 1500х900", upload_to='images/')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Video(models.Model):
    url = models.FileField(_("video"), help_text="Разрешение 1900х500", upload_to='images/')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
