from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserActivity(models.Model):
    ACTION_CHOICES = [
        ('view_property', 'Просмотр объекта'),
        ('search', 'Поиск'),
        ('favorite', 'Добавление в избранное'),
        ('contact', 'Контакт с владельцем'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='activities'
    )
    action = models.CharField(
        max_length=50,
        choices=ACTION_CHOICES
    )
    property = models.ForeignKey(
        'properties.Property',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict)
