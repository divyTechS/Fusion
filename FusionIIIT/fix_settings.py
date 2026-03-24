import os

path = "/mnt/c/Users/indra/Desktop/Fusion/Fusion/FusionIIIT/Fusion/settings/common.py"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Add simplejwt to INSTALLED_APPS
if "'rest_framework_simplejwt'," not in text:
    text = text.replace("'rest_framework',", "'rest_framework',\n    'rest_framework_simplejwt',")

# Setup REST_FRAMEWORK settings
if "REST_FRAMEWORK" not in text:
    text += """

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
"""

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
