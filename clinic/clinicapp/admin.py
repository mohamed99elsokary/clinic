from django.contrib import admin
from . import models


@admin.register(models.WorkTimes)
class WorkTimesAdmin(admin.ModelAdmin):
    """Admin View for WorkTimes"""

    list_display = ["day", "start_time", "end_time"]


@admin.register(models.OnlineWorkTimes)
class OnlineWorkTimesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Terms)
class TermsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    pass
