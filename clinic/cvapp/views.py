from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers, models


class CvViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.cv.objects.all()
    serializer_class = serializers.cv

    def list(self, request):
        cv = get_object_or_404(models.cv, id=1)
        serializer = serializers.cv(cv)
        return Response(serializer.data)
