from datetime import timedelta
from pathlib import Path

from . import env_config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env_config.CONFIG__SECRET_KEY
DEBUG = env_config.CONFIG__DEBUG

ALLOWED_HOSTS = [env_config.CONFIG__ALLOWED_HOSTS]


class SuffixRouter:
    SUFFIX_API: str = "api/v1/"

    AUTH: str = f"{SUFFIX_API}authentication/"
    USER: str = f"{SUFFIX_API}user/"
    FINANCE: str = f"{SUFFIX_API}finance/"
    STATISTIC: str = f"{SUFFIX_API}statistic/"


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',

    'app.authentication.apps.AuthenticationConfig',
    'app.user.apps.UserConfig',
    'app.finance.apps.FinanceConfig',
    'app.statistic.apps.StatisticConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=env_config.CONFIG__ACCESS_TOKEN_LIFETIME),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=env_config.CONFIG__REFRESH_TOKEN_LIFETIME),
    'ROTATE_REFRESH_TOKENS': env_config.CONFIG__ROTATE_REFRESH_TOKENS,
    'BLACKLIST_AFTER_ROTATION': env_config.CONFIG__BLACKLIST_AFTER_ROTATION,
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        }
    },
    # 'USE_SESSION_AUTH': True,
}

AUTH_USER_MODEL = 'user.CustomUser'

LANGUAGE_CODE = 'ru-Ru'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_TZ = False

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env_config.CONFIG__EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = env_config.CONFIG__EMAIL_HOST_PASSWORD