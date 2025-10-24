from apps.analytics.models import UserActivity, Property
from django.db.models import Count
from datetime import datetime, timedelta


class AnalyticsService:
    @staticmethod
    def get_popular_properties(days=30):
        start_date = datetime.now() - timedelta(days=days)
        return Property.objects.filter(
            useractivity__action='view_property',
            useractivity__timestamp__gte=start_date
        ).annotate(
            views_count=Count('useractivity')
        ).order_by('-views_count')[:10]

    @staticmethod
    def get_user_behavior_stats(user_id):
        activities = UserActivity.objects.filter(user_id=user_id)

        stats = {
            'total_views': activities.filter(action='view_property').count(),
            'total_searches': activities.filter(action='search').count(),
            'total_favorites': activities.filter(action='favorite').count(),
            'favorite_property_types': activities.filter(
                action='favorite'
            ).values('property__property_type').annotate(count=Count('id'))
        }
        return stats
