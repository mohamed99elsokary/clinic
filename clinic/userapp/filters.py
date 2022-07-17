from django_filters import rest_framework as filters

from clinic.userapp.models import User


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ["id", "email"]
