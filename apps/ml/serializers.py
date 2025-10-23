from rest_framework import serializers
from .models import Prediction


class PredictionSerializer(serializers.ModelSerializer):
    property_title = serializers.CharField(
        source='property.title', read_only=True)
    property_address = serializers.CharField(
        source='property.address', read_only=True)

    class Meta:
        model = Prediction
        fields = '__all__'
        read_only_fields = ('property', 'predicted_price', 'confidence',
                            'model_version', 'feature_importance',
                            'prediction_explanation', 'created_at')
