from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from decouple import config
from dj_rest_auth.registration.views import SocialLoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from clinic.services.exceptions import Http400
from clinic.services.helpers import rand_int_4digits
from clinic.userapp import models
from clinic.userapp.serializers import (
    ChangePasswordSerializer,
    CodeMailSerializer,
    EmailSerializer,
    LoginSerializerr,
    LogoutSerializer,
    PasswordCodeMailSerializer,
    TokenSerializer,
    UserSerializer,
)

"""
    user
"""
token_response = openapi.Response("response description", TokenSerializer)


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.User.objects.all()
    serializer_class = None

    def get_serializer_class(self):
        if self.action == "register":
            return UserSerializer
        elif self.action == "logout":
            return LogoutSerializer
        elif self.action == "login":
            return LoginSerializerr
        elif self.action == "change_password":
            return ChangePasswordSerializer
        elif self.action == "get_user_data":
            return UserSerializer

    @action(methods=["post"], url_path="register", detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.instance
        user.is_active = True
        user.is_active = True
        user.save()
        # _send_verification_email(user)
        refersh_token = RefreshToken.for_user(user)
        access_token = refersh_token.access_token
        serializer = TokenSerializer(
            data={
                "refresh_token": str(refersh_token),
                "access_token": str(access_token),
            }
        )
        serializer.is_valid()
        return Response(serializer.data, status=201)

    @action(methods=["post"], url_path="logout", detail=False)
    def logout(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(methods=["post"], url_path="login", detail=False)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.instance

        refersh_token = RefreshToken.for_user(user)
        access_token = refersh_token.access_token
        serializer = TokenSerializer(
            data={
                "refresh_token": str(refersh_token),
                "access_token": str(access_token),
            }
        )
        serializer.is_valid()
        return Response(serializer.data, status=201)

    @action(methods=["post"], url_path="change-password", detail=False)
    def change_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "New password has been saved."}, status=200)

    @action(methods=["get"], url_path="user-data", detail=False)
    def get_user_data(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=user)
        return Response(serializer.data)


class LoginView(TokenObtainPairView):
    @swagger_auto_schema(responses={200: token_response})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


def _send_verification_email(user):
    if not user.verification_code:
        user.verification_code = rand_int_4digits()
        user.save()
    send_mail(
        subject="clinic Email Verification",
        message="Dear %s,\n\nPlease use this code to verify your "
        "email: %s.\n\nBest regards,\nclinic Team"
        % (user.username, user.verification_code),
        from_email=config("SERVER_EMAIL"),
        recipient_list=[
            user.email,
        ],
    )


"""
    User Verification
"""


def _is_user_active(email):
    try:
        user = models.User.objects.get(email=email)
        if user.is_active:
            raise Http400({"details": ["email is already verified!"]})
        return user
    except models.User.DoesNotExist:
        raise Http400({"details": ["email not registered"]})


class VerifyMailViewSet(viewsets.GenericViewSet):
    serializer_class = None

    def get_serializer_class(self):
        if self.action == "resend_verification_code":
            return EmailSerializer
        if self.action == "verify_email":
            return CodeMailSerializer

    @swagger_auto_schema(responses={200: "email sent"})
    @action(methods=["post"], detail=False)
    def resend_verification_code(self, request):
        """resend verification code"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        user = _is_user_active(email)
        _send_verification_email(user)
        return Response()

    @swagger_auto_schema(responses={200: "verification successfull"})
    @action(methods=["post"], detail=False)
    def verify_email(self, request):
        """verify user"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        verification_code = serializer.data.get("code")
        _is_user_active(email)
        user = self._activate_user(email, verification_code)
        self._send_confirmation_email(user)
        return Response()

    def _activate_user(self, email, verification_code):
        try:
            user = models.User.objects.get(
                verification_code=verification_code,
                email=email,
            )
            user.update(is_active=True, verification_code=None)
            return user
        except models.User.DoesNotExist:
            raise Http400({"details": ["invalid verification code!"]})

    def _send_confirmation_email(self, user):
        send_mail(
            subject="clinic Email Verification",
            message="Dear %s,\n\nThanks for verifying your email.\n\n"
            "Best regards,\nclinic Team" % (user.username,),
            from_email=config("SERVER_EMAIL"),
            recipient_list=[
                user.email,
            ],
        )


"""
    User Reset Password
"""


class ForgetPasswordViewSet(viewsets.GenericViewSet):
    serializer_class = None

    def get_serializer_class(self):
        if self.action == "send_reset_email":
            return EmailSerializer
        if self.action == "check_reset_code":
            return CodeMailSerializer
        if self.action == "reset_password":
            return PasswordCodeMailSerializer

    @swagger_auto_schema(responses={200: "email sent", 404: "no user with this email"})
    @action(methods=["post"], detail=False)
    def send_reset_email(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(models.User, email=serializer.data.get("email"))
        if not user.password_reset_code:
            user.password_reset_code = rand_int_4digits()
            user.save()
        self._send_reset_email(user)
        return Response({"details": "email has been sent with reset code."})

    def _send_reset_email(self, user):
        send_mail(
            subject="Reset clinic Password",
            message="Dear %s,\n\nPlease use this code to "
            "verify your email: %s.\n\nBest regards,\nclinic Team"
            % (user.username, user.password_reset_code),
            from_email=config("SERVER_EMAIL"),
            recipient_list=[user.email],
        )

    @swagger_auto_schema(
        responses={200: "code valid", 404: "no user with this email and code"}
    )
    @action(methods=["post"], detail=False)
    def check_reset_code(self, request):
        """check code validity"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        get_object_or_404(
            models.User,
            password_reset_code=serializer.data.get("code"),
            email=serializer.data.get("email"),
        )
        return Response({"detail": "correct"})

    @swagger_auto_schema(
        responses={
            200: "password has been reset successfully",
            404: "no user with this email and code",
        }
    )
    @action(methods=["post"], detail=False)
    def reset_password(self, request):
        """reset password"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self._get_user_by_reset_code_email(serializer)
        user.set_password(serializer.data.get("password"))
        user.password_reset_code = None
        user.save()
        self._send_confirmation_email(user)
        return Response({"details": "password has been reset successfully."})

    def _get_user_by_reset_code_email(self, serializer):
        code = serializer.data.get("code")
        email = serializer.data.get("email")
        return get_object_or_404(
            models.User,
            password_reset_code=code,
            email=email,
        )

    def _send_confirmation_email(self, user):
        send_mail(
            subject="Reset clinic Password",
            message="Dear %s,\n\nYour password has been reset "
            "successfully.\n\nBest regards,\nclinic Team" % (user.username),
            from_email=config("SERVER_EMAIL"),
            recipient_list=[
                user.email,
            ],
        )
