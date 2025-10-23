from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Prediction
from .services import PredictionService
from .serializers import PredictionSerializer


class PredictionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PredictionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Prediction.objects.filter(
            Q(property__owner=self.request.user) |
            Q(property__status='available')
        ).select_related('property', 'property__owner')

    @action(detail=True, methods=['post'])
    def recompute(self, request, pk=None):
        """Пересчет предсказания для объекта"""
        try:
            prediction = self.get_object()
            new_prediction = PredictionService.predict_property_price(
                prediction.property)
            serializer = self.get_serializer(new_prediction)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
