from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "service",
        "article",
        "url",
    )
