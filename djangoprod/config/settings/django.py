"""
This module consists of Django configurations for the project
"""
from .env_vars import *


###############################################################################################################
###########################################  Django configurations ############################################
###############################################################################################################
# False if not in os.environ because of casting
DEBUG = ENV('DEBUG')

# Admin and email
ADMINS = [
    ('Rishabh','rishabhojha11@gmail.com'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#! TODO-Boilerplate: Fix this name
ROOT_URLCONF = 'djangoprod.config.urls'

WSGI_APPLICATION = 'djangoprod.config.wsgi.application'

#########################################  TimeZone configurations ##########################################
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'

# Use for langugage transalation when using Django templates.
# Not useful for us since we use DRF
# https://stackoverflow.com/questions/25341003/djando-cms-with-use-i18n-false
USE_I18N = False

# Show date time using the current locale format
# By default true in django 4.0 https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-USE_L10N
USE_L10N = True

# https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-USE_TZ
USE_TZ = False

#######################################  Application configurations ########################################
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'rest_framework',
    'simple_history',
]

LOCAL_APPS = [
    'common.apps.CommonConfig',
    'djangoprod_tests.apps.DjangoProdTestConfig',
]

CUSTOM_APPS = [
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + CUSTOM_APPS

#######################################  Middleware configurations ########################################
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

########################################  Templates configurations ########################################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'common/templates')],
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

########################################  Password Validators ########################################
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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
