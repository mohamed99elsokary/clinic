from rest_framework import serializers
from . import models


class Article(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__"


class Details(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleDetails
        fields = "__all__"


class ArticleDetails(serializers.ModelSerializer):
    content = Details(many=True, read_only=True, source="article_details")

    class Meta:
        model = models.Article
        fields = ["name", "cover", "content"]
