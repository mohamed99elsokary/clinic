from django.contrib import admin

from clinic.userapp.models import User

from . import models


# Register your models here.
@admin.register(models.Reservation)
class Service(admin.ModelAdmin):
    list_display = [
        "user",
        "phone_number",
        "service",
        "date",
        "start_time",
        "end_time",
        "is_paid",
        "is_done",
        "summary",
        "treatment_notes",
        "tracking_notes",
    ]
    list_filter = ["date", "is_done", "user"]
    search_fields = ["user__email"]
    ordering = ("date",)

    def phone_number(self, obj):
        user = obj.user
        phone_number = user.phone_number
        return phone_number
