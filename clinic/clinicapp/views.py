from rest_framework import mixins, viewsets
from rest_framework.response import Response

from . import models, serializers


class TermsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.TermsSerializer

    def list(self, request):
        queryset = models.Terms.objects.first()
        serializer_class = serializers.TermsSerializer(queryset)
        return Response(serializer_class.data)


class ContactViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.ContactSerializer

    def list(self, request):
        queryset = models.Contact.objects.first()
        serializer_class = serializers.ContactSerializer(queryset)
        return Response(serializer_class.data)


class LocationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.LocationSerializer

    def list(self, request):
        queryset = models.Location.objects.first()
        serializer_class = serializers.LocationSerializer(queryset)
        return Response(serializer_class.data)


class WorkTimesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.WorkTimes.objects.all()
    serializer_class = serializers.WorkTimesSerializer

    def list(self, request):
        queryset = models.WorkTimes.objects.all()
        serializer_class = self.serializer_class(queryset, many=True)
        return Response(serializer_class.data)
