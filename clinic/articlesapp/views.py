from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from . import models, serializers


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.Article

    def list(self, request):
        queryset = models.Article.objects.all()
        serializer_class = serializers.Article(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(models.Article, pk=pk)
        serializer = serializers.ArticleDetails(article)
        return Response(serializer.data)
