from rest_framework import serializers
from . import models


class details(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceDetails
        fields = "__all__"


class service(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = "__all__"


class service_details(serializers.ModelSerializer):
    content = details(many=True, read_only=True, source="service_details")

    class Meta:
        model = models.Service
        fields = "__all__"
