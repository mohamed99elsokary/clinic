# Create your models here.
from django.db import models

from clinic.articlesapp import models as articles_models


class Article(models.Model):
    name = models.CharField(max_length=300)
    cover = models.ImageField(
        upload_to="media/article",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )
    index = models.IntegerField()

    class Meta:
        ordering = ("index",)

    def __str__(self):
        return self.name


class ArticleDetails(models.Model):
    article = models.ForeignKey(
        articles_models.Article,
        on_delete=models.CASCADE,
        related_name="article_details",
    )
    image = models.ImageField(
        upload_to="media/article_details",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )
    text = models.TextField()
    index = models.IntegerField()

    class Meta:
        ordering = ("index",)

    def __str__(self):
        return self.article.name
