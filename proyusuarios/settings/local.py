# este local.py es parte de lo que era el setting.py eliminado 
# y llama a base.py como complemento para ambiente de desarrollo

from .base import *
import os


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


STATIC_URL = 'static/'

# configurar donde se ubican los archivos estáticos
STATICFILES_DIRS = [BASE_DIR / 'static']

# establece ruta donde quedaran archivos multimedias
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')