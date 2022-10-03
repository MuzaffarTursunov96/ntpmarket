"""
Django settings for ntpmarket project.

Generated by 'django-admin startproject' using Django 2.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import dj_database_url
import cloudinary
import cloudinary_storage

from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "h8qaj8ttp(vy%43tf=2lde_3z-aw2-gwz!44q3u_od=85%43z^"
# SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DEBUG')
DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True
# ALLOWED_HOSTS = [
#     "127.0.0.1", 
# ]

# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1", 
# ]
CORS_ALLOW_CREDENTIALS = False

# ALLOWED_HOSTS = [config('ALLOWED_HOSTS')]
ALLOWED_HOSTS = ["*"]




INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'projects',
    'rest_framework',
    'rest_framework_simplejwt',
    'cloudinary',
    'cloudinary_storage',
    "corsheaders",
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

# from corsheaders.defaults import default_headers

# CORS_ORIGIN_ALLOW_ALL = True 
# from ntpmarket.DEFAULTS import DEFAULT_HEADERS
# CORS_ALLOW_HEADERS = DEFAULT_HEADERS

# CORS_ALLOW_CREDENTIALS = True
# # Application definition
# ROOT_URLCONF = 'ntpmarket.urls'
# # CORS_ORIGIN_WHITELIST = (
# #   'http://localhost:3000',
# # )

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

WSGI_APPLICATION = 'ntpmarket.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES['default'] = dj_database_url.config()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd2mlthlcmi7oes',
        'USER': 'hvdjhsqbthmpmw',
        'PASSWORD': '35565ce989a42c244749871be9239dac62db03f292df621a3051b4b3396f2f9d',
        'HOST': 'ec2-44-205-63-142.compute-1.amazonaws.com',
        'PORT':'5432',
        # 'NAME': config('DB_NAME'),
        # 'USER': config('DB_USER'),
        # 'PASSWORD': config('DB_PASSWORD'),
        # 'HOST': config('DB_HOST'),
        # 'PORT': config('DB_PORT'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL ='accounts.User'


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'carrentuzbmuzaffar',
    'API_KEY': '471946269558293',
    'API_SECRET':'5PKZZwwxdWI3X7Vk3U-lzgOcQuw',
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10

}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

django_heroku.settings(locals())