"""
Django settings for nannies_ca project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#static asset configuration
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, '../nannies_ca/static'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '56f^$%vy-dzq^&_a$oe0js=)hw^&0l)8rk2jqevv_ns($!3kn@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'customer_area',
    'nannies_ca',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nannies_ca.urls'

WSGI_APPLICATION = 'nannies_ca.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '..', 'templates')    
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nanniesca',
        'USER': 'lukashambsch',
        'PASSWORD': 'Howard12',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# STATIC_URL = '/static/'

# # STATIC_ROOT = '/Users/lukashambsch/envs/nannies_ca/dev/nannies_ca/static'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
#     '/static/'
# )

# Host for sending email
EMAIL_HOST = 'smtp.gmail.com'
# Port for sending email
EMAIL_PORT = 587
# Optional SMTP authentication information for EMAIL_HOST
EMAIL_HOST_USER = 'nanniesca@gmail.com'
EMAIL_HOST_PASSWORD = 'Howard#12'

EMAIL_USE_TLS = True

# CRISPY_TEMPLATE_PACK = 'bootstrap3'