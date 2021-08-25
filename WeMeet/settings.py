

from pathlib import Path
import os
# import django_heroku

# import cloudinary_storage



BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '$45r&4hj_$@u1vm&ts#itdgoln78rxf69c%7^j1-s3p)5b_*hy'


DEBUG = True

ALLOWED_HOSTS = ['wemeet-web.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'WeMeet',
    'corsheaders',
    'django_inlinecss',
    'channels',
    'cloudinary_storage',
    'cloudinary',
]


ASGI_APPLICATION = "WeMeet.asgi.application"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
] # If this is used, then not need to use `CORS_ALLOW_ALL_ORIGINS = True`
CORS_ALLOWED_ORIGIN_REGEXES = [
    'http://localhost:8000',
]
ROOT_URLCONF = 'WeMeet.urls'

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





WSGI_APPLICATION = 'WeMeet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'WeMeet',
        'USER': 'WeMeet',
        'PASSWORD': 'WeMeetWeMeetWeMeet',
        'HOST':'127.0.0.1',
        'PORT': '3306',

        # 'OPTIONS': {
        #         'charset': 'utf8mb4',
        #         'use_unicode': True, },
    },
}

import dj_database_url

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIR = (os.path.join(BASE_DIR, 'static'),)

STATIC_ROOT = os.path.join(BASE_DIR,'live-static','static-root')
MEDIA_ROOT = os.path.join(BASE_DIR,'live-static','media-root')
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'wemeetcloudweb',
    'API_KEY': '346766117525321',
    'API_SECRET': 'CaLs0jV1Rr-orT0EE6JQL7OYUSw'
}
MEDIA_URL = '/media/ProfilePicture/'  # or any prefix you choose



DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
import cloudinary

cloudinary.config(cloud_name='wemeetcloudweb',
                  api_key='346766117525321',
                  api_secret='CaLs0jV1Rr-orT0EE6JQL7OYUSw')
##RahulNavneeth@12345 -- cloudinary


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'wemeetweb@gmail.com'
EMAIL_HOST_PASSWORD ='RahulNavneeth.'


##RahulNavneeth.13 -- Heroku


# Activate Django-Heroku.
# django_heroku.settings(locals())