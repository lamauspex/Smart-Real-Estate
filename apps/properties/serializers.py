from rest_framework import serializers

from apps.ml.models import Property, PropertyType


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    property_type_name = serializers.CharField(
        source='property_type.name', read_only=True)
    owner_username = serializers.CharField(
        source='owner.username', read_only=True)

    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ('owner', 'price_per_m2')

    def create(self, validated_data):
        # Автоматический расчет цены за м² при создании
        if validated_data.get('price') and validated_data.get('area'):
            validated_data['price_per_m2'] = validated_data['price'] / \
                validated_data['area']
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Пересчет цены за м² при обновлении
        if validated_data.get('price') or validated_data.get('area'):
            price = validated_data.get('price', instance.price)
            area = validated_data.get('area', instance.area)
            if price and area:
                validated_data['price_per_m2'] = price / area
        return super().update(instance, validated_data)
