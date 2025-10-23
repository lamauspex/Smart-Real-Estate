from django.db import models
from properties.models import Property


class Prediction(models.Model):
    """
    Результаты ML-прогнозирования для объектов недвижимости
    """
    property = models.OneToOneField(
        Property,
        on_delete=models.CASCADE,
        related_name='prediction',
        verbose_name="Объект недвижимости"
    )

    predicted_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Предсказанная цена"
    )
    confidence = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Уверенность прогноза (0-1)"
    )
    model_version = models.CharField(
        max_length=50,
        verbose_name="Версия модели"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата предсказания")

    # Данные для анализа
    feature_importance = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="Важность признаков"
    )
    prediction_explanation = models.TextField(
        blank=True,
        verbose_name="Объяснение предсказания"
    )

    class Meta:
        verbose_name = "Предсказание"
        verbose_name_plural = "Предсказания"

    def __str__(self):
        return f"Прогноз для {self.property.title}"
