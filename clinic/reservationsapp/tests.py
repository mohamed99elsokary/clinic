from clinic import models as clinic_models
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from services import models as service_models

from . import models


class ReservationsTestCase(APITestCase):
    def token(self):
        user = User.objects.create_user(
            username="username", password="password", email="email@email.com"
        )
        token = Token.objects.create(user=user)
        return token

    def service(self):
        service = service_models.Service.objects.create(
            name="service name", price=100, index=1, duration=30
        )

    def work_times(self):
        work_times = clinic_models.WorkTimes.objects.create(
            day="monday", start_time="00:00:00", end_time="12:00:00"
        )

    def reserve(self):
        user = User.objects.get(id=1)
        service = service_models.Service.objects.get(id=1)
        models.Reservation.objects.create(
            user=user,
            service=service,
            date="2022-01-24",
            start_time="08:00:26",
            end_time="08:50:26",
            price=100,
            is_paid=True,
        )

    def test_get_avalabile_times_invalid_body(self):
        data = {}
        response = self.client.post("/api/available-time", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_avalabile_times_while_there_is_not(self):
        data = {"date": "2022-01-24"}
        response = self.client.post("/api/available-time", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_avalabile_times_while_there_is(self):
        self.token()
        self.service()
        self.work_times()
        data = {"date": "2022-01-24"}

        response = self.client.post("/api/available-time", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reservation_with_missing_token(self):
        token = self.token()
        self.service()
        self.work_times()
        data = {
            "service": 1,
            "time": 1643004026,
            "price": 50,
            "is_paid": True,
        }

        response = self.client.post("/api/reservation", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_reservation_with_missing_service(self):
        token = self.token()
        self.service()
        self.work_times()
        data = {
            "token": token,
            "time": 1643004026,
            "price": 50,
            "is_paid": True,
        }

        response = self.client.post("/api/reservation", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_reservation_with_missing_time(self):
        token = self.token()
        self.service()
        self.work_times()
        data = {
            "token": token,
            "service": 1,
            "price": 50,
            "is_paid": True,
        }

        response = self.client.post("/api/reservation", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_reservation_with_missing_price(self):
        token = self.token()
        self.service()
        self.work_times()
        data = {
            "token": token,
            "service": 1,
            "time": 1643004026,
            "is_paid": True,
        }

        response = self.client.post("/api/reservation", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_reservation_with_missing_is_payed(self):
        token = self.token()
        self.service()
        self.work_times()
        data = {
            "token": token,
            "service": 1,
            "time": 1643004026,
            "price": 50,
        }

        response = self.client.post("/api/reservation", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reservation_with_valid_body_invalid_time(self):
        token = self.token()
        self.service()
        clinic_models.work_times.objects.create(
            day="monday", start_time="12:00:00", end_time="05:00:00"
        )
        self.reserve()
        data = {
            "token": token,
            "service": 1,
            "time": 1643004026,
            "price": 50,
            "is_paid": True,
        }

        response = self.client.post("/api/reservation", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_reservation_with_valid_body_with_valid_time(self):
        token = self.token()
        self.service()
        self.work_times()
        data = {
            "token": token,
            "service": 1,
            "time": 1643004026,
            "price": 50,
            "is_paid": True,
        }

        response = self.client.post("/api/reservation", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_my_reservations_with_missing_token(self):
        token = self.token()
        self.service()
        self.work_times()
        self.reserve()
        data = {}

        response = self.client.post("/api/my-reservation", data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_my_reservations_with_no_reservation(self):
        token = self.token()
        self.service()
        self.work_times()
        self.reserve()
        data = {
            "token": token,
        }

        response = self.client.post("/api/my-reservation", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_my_reservations_with_wrong_token(self):
        token = self.token()
        self.service()
        self.work_times()
        self.reserve()
        data = {
            "token": "asduighasuidh",
        }

        response = self.client.post("/api/my-reservation", data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
