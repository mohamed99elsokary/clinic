"""
Django settings for clinic project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import timedelta
from os.path import join, normpath

from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default=False, cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "userapp.User"
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.AllowAllUsersModelBackend"]


# Application definition

DJANGO_APPS = [
    "clinic.voltapp",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "dj_rest_auth.registration",
    # rest framework
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "import_export",
    "django_filters",
    # all auth
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
    "dj_rest_auth",
    "drf_yasg",
    "smart_selects",
]

# local apps
LOCAL_APPS = [
    "clinic.userapp",
    "clinic.articlesapp",
    "clinic.clinicapp",
    "clinic.conversationapp",
    "clinic.couponesapp",
    "clinic.cvapp",
    "clinic.notificationsapp",
    "clinic.servicesapp",
    "clinic.reservationsapp",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
SITE_ID = 1

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "clinic.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "clinic.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": config("DATABASE_NAME", cast=str),
#         "USER": config("DATABASE_USER", cast=str),
#         "PASSWORD": config("DATABASE_PASSWORD", cast=str),
#         "HOST": config("DATABASE_URL", cast=str),
#         "PORT": config("DATABASE_PORT", cast=str),
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/


LANGUAGE_CODE = "en"

TIME_ZONE = "Africa/Cairo"

USE_I18N = True

USE_L10N = True

USE_TZ = True

gettext = lambda s: s  # noqa
LANGUAGES = (("en", gettext("English")), ("ar", gettext("Arabic")))

LOCALE_PATHS = (normpath(join(BASE_DIR, "locale")),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_DIRECTORY = "/media/"

AUTH_PASSWORD_VALIDATORS = []
AWS_QUERYSTRING_AUTH = False


""" CORS ORIGIN """
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


""" REST FRAMEWORK """
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "clinic.services.paginator.CustomPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
}

""" JWT Settings"""

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "AUTH_HEADER_TYPES": ("Token",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

"""Import Export"""
IMPORT_EXPORT_USE_TRANSACTIONS = True

LOGIN_URL = "/en/admin/login/"

""" SWAGGER_SETTINGS """
SWAGGER_SETTINGS = {
    "DEFAULT_AUTO_SCHEMA_CLASS": "clinic.swagger.CustomSwaggerAutoSchema",
    "LOGIN_URL": LOGIN_URL,
    "LOGOUT_URL": "/admin/logout/",
    "PERSIST_AUTH": True,
    "DEEP_LINKING": True,
    "DOC_EXPANSION": "none",
    "SECURITY_DEFINITIONS": {
        "JWT": {"type": "apiKey", "name": "Authorization", "in": "header"},
    },
}

""" All Auth Settings"""
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_PROVIDERS = {}
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
""" Rest Auth settings """
REST_USE_JWT = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True
