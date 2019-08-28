from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h4@)+45%@+1$wicc*i8inz8(7rs=07_bz+f%8=nk6yk#6@lhr)'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'wagtail.contrib.styleguide',
]
MIDDLEWARE = MIDDLEWARE + [
  'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = [
  '127.0.0.1',
]
#caching 
# Uncomment this line to enable template caching
# Dont forget to change the LOCATION path
#CACHES = {
#  "default": {
 #   "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
 #   "LOCATION": "C:/Users/mouna/FirstDjadngo/myenvironment/mysitewagtail/cache"
 # } 
#}

try:
    from .local import *
except ImportError:
    pass
