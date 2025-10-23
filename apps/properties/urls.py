from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, PropertyTypeViewSet

router = DefaultRouter()
router.register(r'types', PropertyTypeViewSet)
router.register(r'', PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
