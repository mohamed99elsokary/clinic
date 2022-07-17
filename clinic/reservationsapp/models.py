from django.db import models

from clinic.servicesapp import models as services_models
from clinic.userapp.models import User


class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_reservations"
    )
    service = models.ForeignKey(
        services_models.Service,
        on_delete=models.CASCADE,
        related_name="reservation_service",
    )
    date = models.DateField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    price = models.IntegerField()
    treatment_notes = models.TextField(default=None, null=True, blank=True)
    tracking_notes = models.TextField(default=None, null=True, blank=True)
    summary = models.TextField(default=None, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)
