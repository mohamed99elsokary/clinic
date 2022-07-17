from rest_framework import mixins, viewsets

from . import models, serializers


class CouponViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Coupon.objects.all()
    serializer_class = serializers.CouponSerializer
    lookup_field = "coupon"
