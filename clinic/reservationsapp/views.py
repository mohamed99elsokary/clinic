from django.shortcuts import get_list_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers

# convert time to time stamp


class AvailableTimesViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.AvailableTimesSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.save()
        return Response(serializer)

    @action(
        methods=["post"],
        detail=False,
        url_path="online_reservations",
    )
    def online_reservations(self, request):
        serializer = serializers.AvailableOnlineTimesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.save()
        return Response(serializer)


class ReservationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.ReservationSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.save()

        return Response("created successfully", status=status.HTTP_201_CREATED)


class MyReservationsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.MyReservationSerializer

    def list(self, request):
        user = request.user
        reservations = get_list_or_404(models.Reservation, user=user)
        serializer = serializers.MyReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
