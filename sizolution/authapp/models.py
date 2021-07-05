from django.contrib.auth.models import AbstractUser
from django.db import models


class SizolutionUser(models.Model):
    phone_number = models.CharField(
        verbose_name='номер телефона', max_length=18, blank=False, null=False)
    phone_code = models.CharField(
        verbose_name='код телефона', max_length=64, blank=False, null=False)
    status = models.BooleanField(verbose_name='статус', default=False,
                                 db_index=True)

    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['status', 'updated']
