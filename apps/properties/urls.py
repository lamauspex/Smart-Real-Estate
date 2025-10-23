from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.properties.views import PropertyViewSet, PropertyTypeViewSet

router = DefaultRouter()
router.register(r'types', PropertyTypeViewSet)
router.register(r'', PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
