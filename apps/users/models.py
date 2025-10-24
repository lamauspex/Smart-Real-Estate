import random
import string
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone
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

    # Основные поля
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='buyer',
        verbose_name="Роль"
    )

    # Контактная информация
    phone = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Номер телефона должен быть в формате +79991234567"
            )
        ],
        verbose_name="Телефон"
    )

    # Визуализация
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name="Аватар"
    )

    # Настройки и предпочтения
    preferences = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="Предпочтения"
    )

    # Верификация
    is_verified = models.BooleanField(
        default=False,
        verbose_name="Верифицирован"
    )
    verification_code = models.CharField(
        max_length=6,
        blank=True,
        null=True,
        verbose_name="Код верификации"
    )
    verification_code_created_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата создания кода верификации"
    )

    class Meta:
        indexes = [
            models.Index(fields=['role']),
            models.Index(fields=['is_verified']),
            models.Index(fields=['phone']),
        ]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def generate_verification_code(self):
        """Генерирует новый код верификации"""
        code = ''.join(random.choices(string.digits, k=6))
        self.verification_code = code
        self.verification_code_created_at = timezone.now()
        self.save()
        return code

    def verify_code(self, code):
        """Проверяет код верификации"""
        if not code or not self.verification_code:
            return False

        if self.verification_code == code and self.verification_code_created_at:
            # Проверяем, что код не старше 15 минут
            time_diff = timezone.now() - self.verification_code_created_at
            if time_diff.total_seconds() < 900:  # 15 минут
                self.is_verified = True
                self.verification_code = None
                self.verification_code_created_at = None
                self.save()
                return True
        return False

    def clean_verification_code(self):
        """Очищает устаревший код верификации"""
        if self.verification_code_created_at:
            time_diff = timezone.now() - self.verification_code_created_at
            if time_diff.total_seconds() >= 900:  # 15 минут
                self.verification_code = None
                self.verification_code_created_at = None
