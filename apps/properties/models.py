
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PropertyImage(models.Model):
    """
    Модель для хранения изображений недвижимости
    """
    property = models.ForeignKey(
        'Property',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='property_images/')
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.property.title}"


class PropertyType(models.Model):
    """
    Тип недвижимости (квартира, дом, земельный участок и т.д.)
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Тип"
    )

    def __str__(self):
        return self.name


class Property(models.Model):
    """
    Основная модель недвижимости
    """
    STATUS_CHOICES = [
        ('available', 'Доступно'),
        ('sold', 'Продано'),
        ('rented', 'Сдано'),
        ('pending', 'В ожидании')
    ]

    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )

    # Связи
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='properties',
        verbose_name="Владелец"
    )
    property_type = models.ForeignKey(
        PropertyType,
        on_delete=models.PROTECT,
        verbose_name="Тип недвижимости"
    )

    # Геоданные (PostGIS)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name="Широта"
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name="Долгота"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )

    # Основные характеристики
    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Площадь (м²)"
    )
    rooms = models.PositiveIntegerField(verbose_name="Комнаты")
    floor = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Этаж"
    )
    total_floors = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Этажность"
    )
    year_built = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Год постройки"
    )

    # Ценовые данные
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Цена"
    )
    price_per_m2 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за м²"
    )

    # Системные поля
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available',
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Объект недвижимости"
        verbose_name_plural = "Объекты недвижимости"

    def __str__(self):
        return f"{self.title} ({self.address})"
