from django.contrib import admin

from . import models


@admin.register(models.Article)
class Article(admin.ModelAdmin):
    search_fields = ["name", "index"]
    list_display = ["name", "index"]
    ordering = ("index",)


@admin.register(models.ArticleDetails)
class ArticleDetails(admin.ModelAdmin):
    list_filter = ["article"]
    search_fields = ["text"]
    list_display = ["article", "index"]
    ordering = ("article", "index")
