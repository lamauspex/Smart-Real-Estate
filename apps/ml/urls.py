from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.ml.views import PredictionViewSet

router = DefaultRouter()
router.register(r'predictions', PredictionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
