from django.db import transaction
from .models import Prediction


class PredictionService:
    """
    Сервис для работы с ML-прогнозами
    """

    @staticmethod
    def predict_property_price(property_obj):
        """
        Основная функция для предсказания цены объекта

        Args:
            property_obj (Property): Объект недвижимости

        Returns:
            Prediction: Объект предсказания
        """
        # Заглушки для ML-функций - в реальном проекте здесь будет ваша логика
        predicted_price = PredictionService._calculate_price(property_obj)
        importance_data = PredictionService._get_feature_importance()

        # Сохраняем результат в транзакции
        with transaction.atomic():
            prediction, created = Prediction.objects.update_or_create(
                property=property_obj,
                defaults={
                    'predicted_price': predicted_price,
                    'model_version': 'v1.0',
                    'confidence': PredictionService._calculate_confidence(property_obj),
                    'feature_importance': importance_data,
                    'prediction_explanation': PredictionService._generate_explanation(
                        property_obj,
                        predicted_price
                    )
                }
            )

        return prediction

    @staticmethod
    def _calculate_price(property_obj):
        """
        Расчет предсказанной цены (заглушка)
        В реальном проекте здесь будет ваша ML-модель

        Args:
            property_obj (Property): Объект недвижимости

        Returns:
            Decimal: Предсказанная цена
        """
        # Простой расчет для демонстрации
        # В реальности здесь будет сложная ML-логика
        base_price = property_obj.area * property_obj.price_per_m2

        # Корректировки в зависимости от характеристик
        if property_obj.floor and property_obj.total_floors:
            if property_obj.floor == property_obj.total_floors:
                base_price *= 1.05  # Этажность +5%
            elif property_obj.floor == 1:
                base_price *= 0.95  # Первый этаж -5%

        if property_obj.year_built and property_obj.year_built < 1980:
            base_price *= 0.9  # Старый дом -10%

        return round(base_price, 2)

    @staticmethod
    def _get_feature_importance():
        """
        Получение важности признаков (заглушка)
        В реальном проекте здесь будет анализ ML-модели

        Returns:
            dict: Словарь с важностью признаков
        """
        return {
            'area': 0.35,
            'location': 0.25,
            'rooms': 0.15,
            'floor': 0.10,
            'year_built': 0.10,
            'property_type': 0.05
        }

    @staticmethod
    def _calculate_confidence(property_obj):
        """
        Расчет уверенности прогноза (заглушка)
        В реальном проекте здесь будет анализ качества данных

        Args:
            property_obj (Property): Объект недвижимости

        Returns:
            float: Уверенность (0-1)
        """
        # Чем больше заполнено полей, тем выше уверенность
        filled_fields = sum([
            bool(property_obj.floor),
            bool(property_obj.total_floors),
            bool(property_obj.year_built),
            bool(property_obj.description)
        ])

        base_confidence = 0.7
        confidence_boost = filled_fields * 0.075
        return min(base_confidence + confidence_boost, 0.99)

    @staticmethod
    def _generate_explanation(property_obj, predicted_price):
        """
        Генерация объяснения прогноза (заглушка)

        Args:
            property_obj (Property): Объект недвижимости
            predicted_price (Decimal): Предсказанная цена

        Returns:
            str: Объяснение прогноза
        """
        explanation = f"Прогноз основан на площади {property_obj.area} м²"

        if property_obj.location:
            explanation += f" и расположении в {property_obj.address}"

        if property_obj.year_built:
            explanation += f". Год постройки {property_obj.year_built} учтен в расчете"

        return explanation
