# Generated by Django 4.2.4 on 2023-08-31 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_products_description_en_products_description_ky_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description_ky',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='products',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='products',
            name='title_ky',
        ),
        migrations.RemoveField(
            model_name='products',
            name='title_ru',
        ),
        migrations.AddField(
            model_name='practice',
            name='description_en',
            field=models.TextField(max_length=500, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='practice',
            name='description_ky',
            field=models.TextField(max_length=500, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='practice',
            name='description_ru',
            field=models.TextField(max_length=500, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='practice',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='practice',
            name='title_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='practice',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
    ]