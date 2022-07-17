#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

export DJANGO_SETTINGS_MODULE=clinic.settings.production;
python manage.py migrate
uwsgi /code/wsgi.ini
