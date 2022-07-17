from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("articles", views.ArticleViewSet, basename="articles")
urlpatterns = [
    path("", include(router.urls)),
]
