from rest_framework import status
from rest_framework.test import APITestCase
from . import models


def setup():
    # add services
    service1 = models.Service.objects.create(
        name="service 1 ", price=2500, index=1, duration=50
    )
    service2 = models.Service.objects.create(
        name="service 2 ", price=300, index=2, duration=30
    )
    # add service details
    models.ServiceDetails.objects.create(service=service1, index=1, text="service")
    models.ServiceDetails.objects.create(
        service=service2, index=2, text="service details"
    )


class servicesTestCase(APITestCase):
    def test_get_services_while_there_is_none(self):
        response = self.client.get("/api/services")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_services_while_there_is(self):
        setup()
        response = self.client.get("/api/services")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_services_details_while_there_is_none(self):
        response = self.client.get("/api/service/1")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_services_details_while_there_is(self):
        setup()
        response = self.client.get("/api/service/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
