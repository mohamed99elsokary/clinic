from django.urls import include, path
from rest_framework import routers

from clinic.userapp.views import (
    FacebookLogin,
    ForgetPasswordViewSet,
    GoogleLogin,
    UserViewSet,
    VerifyMailViewSet,
)

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("users/password", ForgetPasswordViewSet, basename="password_reset")
router.register("users/email", VerifyMailViewSet, basename="email_verification")


urlpatterns = [
    path("", include(router.urls)),
    path("accounts/", include("allauth.urls")),
    path("users/facebook/", FacebookLogin.as_view(), name="fb_login"),
    path("users/google/", GoogleLogin.as_view(), name="google_login"),
]
