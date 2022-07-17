from import_export import resources

from clinic.userapp.models import User


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = [
            "id",
            "password",
            "last_login",
            "first_name",
            "last_name",
            "date_joined",
            "email",
            "username",
            "phone",
            "verification_code",
            "password_reset_code",
        ]
        export_order = fields
