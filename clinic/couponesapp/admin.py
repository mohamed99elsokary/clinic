from django.contrib import admin
from . import models


@admin.register(models.Coupon)
class Service(admin.ModelAdmin):
    search_fields = ["coupon", "value", "name"]
    list_display = ["name", "value", "coupon"]
    ordering = ("value",)
