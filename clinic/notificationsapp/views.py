from rest_framework import viewsets
from . import serializers, models


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer
