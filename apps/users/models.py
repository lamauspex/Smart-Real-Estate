from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Расширенная модель пользователя с ролями и дополнительными данными
    """
    ROLE_CHOICES = [
        ('buyer', 'Покупатель'),
        ('seller', 'Продавец'),
        ('agent', 'Агент'),
        ('admin', 'Администратор')
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='buyer',
        verbose_name="Роль"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Телефон"
    )
    preferences = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="Предпочтения"
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
