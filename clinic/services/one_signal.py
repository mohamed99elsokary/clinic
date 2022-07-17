import json

import requests
from decouple import config

# onesignal app_id
ONESIGNAL_APP_ID = config("ONESIGNAL_APP_ID", default="", cast=str)
url = "https://onesignal.com/api/v1/notifications/"
headers = {"content-type": "application/json"}
