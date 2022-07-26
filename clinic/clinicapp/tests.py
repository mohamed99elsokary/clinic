from rest_framework import status
from rest_framework.test import APITestCase
from . import models


class WorkTimesTestCase(APITestCase):
    def setup(self):
        models.WorkTimes.objects.create(
            day="sunday", start_time="05:03:04", end_time="09:03:24"
        )
        models.WorkTimes.objects.create(
            day="monday", start_time="05:03:04", end_time="09:03:24"
        )
        models.WorkTimes.objects.create(
            day="friday", start_time="05:03:04", end_time="09:03:24"
        )

    def test_no_work_times(self):
        response = self.client.get("/api/work-times")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_work_times(self):
        self.setup()
        response = self.client.get("/api/work-times")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LocationTestCase(APITestCase):
    def setup(self):
        models.Location.objects.create(
            address="any address text ", latitude="05:03:04", longitude="09:03:24"
        )

    def test_no_location(self):
        response = self.client.get("/api/location")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_location(self):
        self.setup()
        response = self.client.get("/api/location")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ContactTestCase(APITestCase):
    def setup(self):
        models.Contact.objects.create(
            email="email@email.com",
            facebook="https://www.youtube.com/",
            instagram="https://www.youtube.com/",
            youtube="https://www.youtube.com/",
            phone="+201111155856",
            whatsapp="+201111155856",
        )

    def test_no_contact(self):
        response = self.client.get("/api/contact")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_contact(self):
        self.setup()
        response = self.client.get("/api/contact")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TermsTestCase(APITestCase):
    def setup(self):
        models.Terms.objects.create(
            terms="siudjauisdhjiausdjiuashdiaasjiajsdoiajsaoiajsdoiasjdoiasjdoiasjdoiajsdoiasjdoiajsdoiajsdiushdifushdfui",
        )

    def test_no_terms(self):
        response = self.client.get("/api/terms")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_terms(self):
        self.setup()
        response = self.client.get("/api/terms")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
