from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from clinic.servicesapp import models as services_models

from . import models
from .utils import (
    get_available_time_normal_service,
    get_available_time_online_service,
    time_to_tiemstamp,
)


class AvailableOnlineTimesSerializer(serializers.Serializer):
    date = serializers.DateField(write_only=True, help_text="2022-01-24")

    def create(self, validated_data):
        available_times = get_available_time_online_service(validated_data["date"])
        if not available_times:
            raise serializers.ValidationError("there is no available time at this date")
        return available_times


class AvailableTimesSerializer(serializers.Serializer):
    date = serializers.DateField(write_only=True, help_text="2022-01-24")

    def create(self, data):
        available_times = get_available_time_normal_service(data["date"])
        if not available_times:
            raise serializers.ValidationError("there is no available time at this date")
        return available_times


class ReservationSerializer(serializers.Serializer):
    service = serializers.IntegerField()
    time = serializers.IntegerField()
    price = serializers.IntegerField()
    is_paid = serializers.BooleanField()

    def validate(self, data):
        service = get_object_or_404(services_models.Service, id=data.get("service"))
        duration = service.duration
        # convert timestamp to data
        date_time = datetime.fromtimestamp(data["time"])
        date = date_time.date()
        start_time = time_to_tiemstamp(date_time.time())
        end_time = start_time + duration * 60
        if service.is_online == True:
            available_times = get_available_time_online_service(date)
        else:
            available_times = get_available_time_normal_service(date)
        if available_times:
            for i in available_times:
                if start_time >= i["start_time"] and end_time <= i["end_time"]:
                    pass
                else:
                    raise serializers.ValidationError({"error": "not available times"})
        else:
            raise serializers.ValidationError({"error": "Invalid date or day off"})

        # pass data to validated_data
        data["service"] = service
        data["duration"] = duration
        data["date"] = date
        data["date_time"] = date_time

        return data

    def create(self, validated_data):
        service = validated_data.get("service")
        time = validated_data.get("time")
        duration = validated_data.get("duration")
        date = validated_data.get("date")
        date_time = validated_data.get("date_time")

        end_time = duration * 60 + time
        end_time = datetime.fromtimestamp(end_time).time()
        start_time = date_time.time()
        request = self.context.get("request")

        user = request.user
        service = models.Reservation.objects.create(
            user=user,
            service=service,
            date=date,
            start_time=start_time,
            end_time=end_time,
            price=validated_data.get("price"),
            is_paid=validated_data.get("is_paid"),
        )
        return service


class MyReservationSerializer(serializers.ModelSerializer):
    service = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = models.Reservation
        exclude = ("user",)
