

from pathlib import Path
import os
# import cloudinary_storage



BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '$45r&4hj_$@u1vm&ts#itdgoln78rxf69c%7^j1-s3p)5b_*hy'


DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'WeMeet',
    'django_inlinecss',
    'channels',
    'cloudinary_storage',
    'cloudinary',
]


ASGI_APPLICATION = "WeMeet.asgi.application"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

        'OPTIONS': {
                'charset': 'utf8mb4',
                'use_unicode': True, },
    },
}



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
STATIC_ROOT = str(os.path.join(BASE_DIR, 'WeMeet/static'),)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'wemeetweb',
    'API_KEY': '652496293865574',
    'API_SECRET': 'ciUDj7hvzZpRHdF06WVjF6Z3w2E'
}
MEDIA_URL = '/media/ProfilePicture/'  # or any prefix you choose
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
import cloudinary

cloudinary.config(cloud_name='wemeetweb',
                  api_key='652496293865574',
                  api_secret='ciUDj7hvzZpRHdF06WVjF6Z3w2E')
##RahulNavneeth@12345 -- cloudinary


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'wemeetweb@gmail.com'
EMAIL_HOST_PASSWORD ='RahulNavneeth.'