from django.db import models


from django.db import models


class Image(models.Model):
    url = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Изображение")

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'