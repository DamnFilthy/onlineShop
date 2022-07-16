from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Gadget(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.CharField(max_length=50, verbose_name='Описание')
    old_price = models.IntegerField(verbose_name='Старая цена')
    new_price = models.IntegerField(verbose_name='Новая цена')
    default_price = models.IntegerField(verbose_name='Базовая цена')
    discount = models.IntegerField(verbose_name='Скидка %')
    count = models.IntegerField(verbose_name='Количество на складе')
    active = models.BooleanField(default=True, verbose_name='Доступен для покупки')
    image = models.ImageField(upload_to='static/media/images', blank=True, verbose_name='Изображение товара')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название Категории')
    description = models.CharField(max_length=300, verbose_name='Описание')
    url = models.CharField(max_length=30, verbose_name='Ссылка', blank=True)
    image = models.ImageField(upload_to='static/media/images', blank=True, verbose_name='Изображение категории')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class GadgetImage(models.Model):
    gadget = models.ForeignKey('Gadget', on_delete=models.CASCADE, verbose_name='Фотографии устройства')
    gadgetImage = models.ImageField(upload_to='static/media/images', blank=True, verbose_name='Изображение товара')
