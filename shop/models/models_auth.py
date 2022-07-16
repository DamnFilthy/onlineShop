from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    email = models.EmailField(max_length=50, verbose_name='Почта')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    password = models.CharField(max_length=3000, verbose_name='Пароль')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name
