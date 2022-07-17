from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("conversation", views.ConversationViewSet, basename="conversation")
router.register("messages", views.MessageViewSet, basename="messages")
urlpatterns = [
    path("", include(router.urls)),
]
