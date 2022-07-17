from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication

from clinic.swagger import CustomOpenAPISchemaGenerator

# Admin settings
admin.site.site_header = "clinic"
admin.site.site_title = "clinic site admin"
admin.site.index_title = "clinic site administration"

# URL settings

main_patterns = i18n_patterns(
    path("admin/", include("clinic.voltapp.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("clinic.articlesapp.urls")),
    path("api/", include("clinic.clinicapp.urls")),
    path("api/", include("clinic.conversationapp.urls")),
    path("api/", include("clinic.couponesapp.urls")),
    path("api/", include("clinic.cvapp.urls")),
    path("api/", include("clinic.notificationsapp.urls")),
    path("api/", include("clinic.reservationsapp.urls")),
    path("api/", include("clinic.servicesapp.urls")),
    path("api/", include("clinic.userapp.urls")),
)
urlpatterns = main_patterns


# Health url
urlpatterns += [path("health/", lambda res: HttpResponse("good"))]


# swagger urls and configuration
schema_view = get_schema_view(
    openapi.Info(
        title="clinic API",
        default_version="v1",
        description="clinic Swagger Documentation",
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
    authentication_classes=(SessionAuthentication,),
    generator_class=CustomOpenAPISchemaGenerator,
    patterns=main_patterns,
)
urlpatterns += [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
