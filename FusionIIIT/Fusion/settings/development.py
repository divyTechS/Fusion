from Fusion.settings.common import *

DEBUG = True

SECRET_KEY = '=&w9due426k@l^ju1=s1)fj1rnpf0ok8xvjwx+62_nc-f12-8('

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fusionlab',
        'USER': 'postgres',
        'PASSWORD': '2304',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

if DEBUG:
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
        'debug_toolbar',
        'django_extensions',
        )


    ###############################
    # DJANGO_EXTENSIONS SETTINGS: #
    ###############################
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

    ###############################
    # DJANGO_EXTENSIONS SETTINGS: #
    ###############################
    SHELL_PLUS = "ipython"

    SHELL_PLUS_PRINT_SQL = True

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
