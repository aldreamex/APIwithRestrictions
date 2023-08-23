from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from advertisements.serializers import AdvertisementSerializer
from advertisements.models import Advertisement
from advertisements.filters import AdvertisementFilter
from django_filters.rest_framework import DjangoFilterBackend

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]

        if self.action in ['create', 'partial_update', 'destroy']:
            return [IsOwnerOrAdmin()]

        return []