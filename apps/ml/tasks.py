import logging
from celery import shared_task

from apps.properties.models import Property
from apps.ml.services import RecommendationService
from apps.ml.models import PricePredictionModel


logger = logging.getLogger(__name__)


@shared_task
def update_recommendations():
    """Обновление рекомендаций для всех пользователей"""
    try:
        recommendation_service = RecommendationService()
        recommendation_service.build_similarity_matrix()
        logger.info("Recommendations updated successfully")
    except Exception as e:
        logger.error(f"Error updating recommendations: {e}")


@shared_task
def predict_property_price(property_id):
    """Предсказание цены для конкретного объекта"""
    try:
        property_obj = Property.objects.get(id=property_id)

        # Собираем данные для предсказания
        property_data = {
            'property_type': property_obj.property_type,
            'area': property_obj.area,
            'rooms': property_obj.rooms if hasattr(property_obj, 'rooms') else 2,
            'location_score': property_obj.location_score if hasattr(property_obj, 'location_score') else 5
        }

        # Используем последнюю модель
        model = PricePredictionModel.objects.order_by('-created_at').first()
        if model:
            predicted_price = model.predict_price(property_data)
            logger.info(
                f"Predicted price for property {property_id}: {predicted_price}")
            return predicted_price

    except Exception as e:
        logger.error(f"Error predicting price for property {property_id}: {e}")
        return None
