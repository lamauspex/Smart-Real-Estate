from django.contrib import admin

from apps.properties.models import Property, PropertyType, PropertyImage


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'price',
                    'area', 'status', 'created_at')
    list_filter = ('property_type', 'status', 'created_at')
    search_fields = ('title', 'address')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'property_type', 'status')
        }),
        ('Цена и размеры', {
            'fields': ('price', 'area', 'rooms')
        }),
        ('Контакты', {
            'fields': ('owner', 'address', 'phone')
        }),
        ('Изображения', {
            'fields': ('images',)
        }),
        ('Системные поля', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


admin.site.register(PropertyImage)
