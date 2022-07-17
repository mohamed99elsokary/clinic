from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(models.Field)
class cv(ImportExportModelAdmin):
    pass


@admin.register(models.ScientificDegree)
class cv(admin.ModelAdmin):
    pass


@admin.register(models.Experience)
class cv(admin.ModelAdmin):
    pass


@admin.register(models.Skill)
class cv(admin.ModelAdmin):
    pass


@admin.register(models.Other)
class cv(admin.ModelAdmin):
    pass


@admin.register(models.cv)
class cv(admin.ModelAdmin):
    pass
