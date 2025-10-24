from django.db.models import Q


class PropertyFilter:
    @staticmethod
    def filter_properties(queryset, filters):
        if filters.get('min_price'):
            queryset = queryset.filter(price__gte=filters['min_price'])
        if filters.get('max_price'):
            queryset = queryset.filter(price__lte=filters['max_price'])
        if filters.get('property_types'):
            queryset = queryset.filter(
                property_type__in=filters['property_types'])
        if filters.get('min_area'):
            queryset = queryset.filter(area__gte=filters['min_area'])
        if filters.get('search'):
            search_term = filters['search']
            queryset = queryset.filter(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term) |
                Q(address__icontains=search_term)
            )
        return queryset
