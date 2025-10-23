from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Property, PropertyType
from .serializers import PropertySerializer, PropertyTypeSerializer


class PropertyTypeFilter(filters.FilterSet):
    class Meta:
        model = PropertyType
        fields = ['name']


class PropertyFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="area", lookup_expr='lte')

    class Meta:
        model = Property
        fields = ['property_type', 'status', 'rooms', 'min_price', 'max_price',
                  'min_area', 'max_area']


class PropertyTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    filterset_class = PropertyTypeFilter
    permission_classes = [IsAuthenticated]


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filterset_class = PropertyFilter
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def near_me(self, request):
        """Поиск объектов рядом с пользователем"""
        if not request.user.location:
            return Response(
                {"error": "У пользователя не указана локация"},
                status=status.HTTP_400_BAD_REQUEST
            )

        radius = float(request.query_params.get(
            'radius', 5000))  # 5 км по умолчанию
        properties = self.queryset.filter(
            location__distance_lte=(request.user.location, radius)
        )

        page = self.paginate_queryset(properties)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(properties, many=True)
        return Response(serializer.data)
