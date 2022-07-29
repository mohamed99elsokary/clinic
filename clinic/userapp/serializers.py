from django.contrib.auth import authenticate
from rest_framework import serializers

from clinic.services.custom_ModelSerializer import CustomModelSerializer
from clinic.userapp.models import FcmToken, User


class UserSerializer(CustomModelSerializer):
    password = serializers.CharField(write_only=True)
    fcm_token = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "phone_number",
            "password",
            "fcm_token",
            "first_name",
            "last_name",
        )

    def create(self, validated_data):
        fcm_token = validated_data.pop("fcm_token")
        user = User.objects.create_user(**validated_data)
        FcmToken.objects.get_or_create(user=user, token=fcm_token)
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            raise serializers.ValidationError("can not update password.")
        return super().update(instance, validated_data)


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=200)
    refresh_token = serializers.CharField(max_length=200)


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200)


class CodeMailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200)
    code = serializers.CharField(
        allow_blank=False,
        max_length=30,
        trim_whitespace=True,
        min_length=4,
    )


class PasswordCodeMailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200)
    code = serializers.CharField(
        allow_blank=False,
        max_length=30,
        trim_whitespace=True,
        min_length=4,
    )
    password = serializers.CharField(
        allow_blank=False,
        min_length=6,
    )


class LogoutSerializer(serializers.Serializer):
    fcm_token = serializers.CharField()

    def create(self, data):
        fcm_token = data["fcm_token"]
        request = self.context.get("request")
        try:
            fcm_token = FcmToken.objects.get(token=fcm_token)
            fcm_token_user = fcm_token.user
            if fcm_token_user == request.user:
                fcm_token.delete()
        except:
            raise serializers.ValidationError({"token": "Invalid Token"})
        return data


class LoginSerializerr(CustomModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    fcm_token = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "password", "fcm_token")

    def create(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if user == None:
            raise serializers.ValidationError(
                {"email or password": "Invalid email or password"}
            )
        else:
            FcmToken.objects.get_or_create(user=user, token=data["fcm_token"])
        return user


class ChangePasswordSerializer(CustomModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id",)

    def create(self, data):
        user = self.context["request"].user
        user_email = user.email
        user = authenticate(email=user_email, password=data["old_password"])
        if user == None:
            raise serializers.ValidationError({"password": "Invalid password"})
        else:
            user.set_password(data["new_password"])
        return user
