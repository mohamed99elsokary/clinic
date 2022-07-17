from rest_framework import status
from rest_framework.test import APITestCase
from . import models


def setup():
    article = models.Article.objects.create(name="first article", index=1)
    models.ArticleDetails.objects.create(
        article=article, text="lorem cxjnvx,cvxcv", index=1
    )
    models.ArticleDetails.objects.create(
        article=article, text="lorem a9isd9aisd", index=2
    )
    models.ArticleDetails.objects.create(
        article=article, text="lorem uiertierutpert", index=3
    )
    return article.id


class AllArticlesTestCase(APITestCase):
    def test_get_all_articles(self):
        response = self.client.get("/api/articles")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_exist_article_details(self):
        setup()
        response = self.client.get("/api/article/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_exist_article_details(self):
        response = self.client.get("/api/article/1")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
