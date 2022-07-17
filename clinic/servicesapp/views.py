from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from . import serializers, models


class ServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.service

    def retrieve(self, request, pk):
        queryset = get_object_or_404(models.Service, id=pk)
        serializer_class = serializers.service_details(queryset)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
