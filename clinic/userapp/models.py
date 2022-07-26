from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from clinic.services.custom_Models import CustomModel
from clinic.services.helpers import rand_int_4digits


class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields["is_active"] = True
        return super().create_superuser(username, email, password, **extra_fields)


class User(CustomModel, AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        unique=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=300)
    username = models.CharField(
        _("username"),
        max_length=150,
    )

    # verification
    is_active = models.BooleanField(default=True)

    verification_code = models.CharField(
        max_length=10, default=rand_int_4digits, null=True, blank=True
    )

    is_development_api_user = models.BooleanField(
        default=False,
        help_text=_(
            "indicate if this user could be used in developer "
            "only private APIs like create statistics endpoints."
        ),
    )
    password_reset_code = models.CharField(max_length=10, null=True, blank=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class FcmToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username
