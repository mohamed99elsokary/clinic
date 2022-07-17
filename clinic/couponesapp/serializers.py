from rest_framework import serializers
from . import models


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coupon
        fields = "__all__"
        # read_only_fields = ("name", "value")
