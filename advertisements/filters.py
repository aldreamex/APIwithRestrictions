from django_filters import rest_framework as filters, DateTimeFromToRangeFilter
from advertisements.models import Advertisement

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateTimeFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']
