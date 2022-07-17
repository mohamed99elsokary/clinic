from rest_framework import status
from rest_framework.test import APITestCase
from . import models


def setup():
    models.Coupon.objects.create(coupon="aushdaiusd", value=50)


class CouponsTestCase(APITestCase):
    def test_get_invalid_coupon_value(self):
        response = self.client.get("/api/coupon/aushdaiusd")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_valid_coupon_value(self):
        setup()
        response = self.client.get("/api/coupon/aushdaiusd")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
