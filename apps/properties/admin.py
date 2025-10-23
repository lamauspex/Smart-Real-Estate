from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Property, PropertyType


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Property)
class PropertyAdmin(OSMGeoAdmin):
    list_display = ('title', 'property_type', 'price',
                    'area', 'status', 'created_at')
    list_filter = ('property_type', 'status', 'created_at')
    search_fields = ('title', 'address')
    date_hierarchy = 'created_at'
    fields = ('title', 'description', 'owner', 'property_type', 'location',
              'address', 'area', 'rooms', 'floor', 'total_floors',
              'year_built', 'price', 'price_per_m2', 'status')
