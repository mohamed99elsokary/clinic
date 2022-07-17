from rest_framework import serializers
from . import models


class WorkTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkTimes
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        exclude = ("id",)


class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Terms
        exclude = ("id",)
