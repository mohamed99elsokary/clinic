from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Service)
class Service(admin.ModelAdmin):
    search_fields = ["name", "index", "price", "duration"]
    list_display = ["name", "index", "price", "duration"]

    ordering = ("index",)


@admin.register(models.ServiceDetails)
class ServiceDetails(admin.ModelAdmin):
    list_filter = ["service"]
    search_fields = ["text"]
    list_display = ["service", "index"]

    ordering = ("service", "index")
