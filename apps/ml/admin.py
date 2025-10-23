from django.contrib import admin
from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('property', 'predicted_price',
                    'confidence', 'model_version', 'created_at')
    list_filter = ('model_version', 'created_at')
    search_fields = ('property__title', 'property__address')
    raw_id_fields = ('property',)
