from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    "available-time", views.AvailableTimesViewSet, basename="available-time"
)
router.register("reservation", views.ReservationViewSet, basename="reservation")
router.register(
    "my-reservations", views.MyReservationsViewSet, basename="my-reservation"
)

urlpatterns = [
    path("", include(router.urls)),
]
