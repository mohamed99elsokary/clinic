from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin

from clinic.userapp import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin, ImportExportModelAdmin):
    list_display = [
        "id",
        "email",
        "first_name",
        "last_name",
    ]
    fieldsets = (
        (None, {"fields": ("username", "password", "is_development_api_user")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


@admin.register(models.FcmToken)
class account(admin.ModelAdmin):
    list_filter = ["user"]


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = "action_time"

    # to filter the resultes by users, content types and action flags
    list_filter = ["user", "content_type", "action_flag"]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = ["object_repr", "change_message"]

    list_display = [
        "action_time",
        "user",
        "content_type",
        "action_flag",
    ]
