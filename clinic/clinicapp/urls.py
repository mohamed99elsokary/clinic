from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("terms", views.TermsViewSet, basename="terms")
router.register("contact", views.ContactViewSet, basename="contact")
router.register("work-times", views.WorkTimesViewSet, basename="work-times")
router.register("location", views.LocationViewSet, basename="location")


urlpatterns = [
    path("", include(router.urls)),
]
