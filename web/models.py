from django.db import models
from django.utils.translation import gettext as _


class Language(models.Model):
    title = models.CharField(_("title"), max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Practice(models.Model):
    title = models.CharField(_("title"), max_length=100)
    image = models.ImageField(_("image"), upload_to='images/', null=True, blank=True)
    description = models.TextField(_("description"), max_length=500)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельности'


class Experience(models.Model):
    title = models.CharField(_("title"), max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'


class Principle(models.Model):
    title = models.CharField(_("title"), max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Принцип'
        verbose_name_plural = 'Принципы'


class Products(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"), max_length=100)
    image = models.ImageField(_("image"), upload_to='images/', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


