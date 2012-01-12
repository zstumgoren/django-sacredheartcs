from config.base.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '%s/%s.sqlite' % (PROJECT_ROOT, PROJECT_SLUG),
    }
}

INSTALLED_APPS += (
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_extensions',
    'debug_toolbar',
    'south',
    #'autocomplete',
)
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'config.prod.urls'

#HTDOCS_ROOT = '/var/www/%s/' % PROJECT_SLUG
#STATIC_URL = 'http://my.mediaserver.com/apps/static'

#STATIC_URL = '%s/%s/static/' % (STATIC_URL, PROJECT_SLUG)
#STATIC_ROOT = '%s/%s/static/' % (HTDOCS_ROOT, PROJECT_SLUG)
#MEDIA_URL = '%s/%s/media/' % (STATIC_URL, PROJECT_SLUG)
#MEDIA_ROOT = '%s/%s/media/' % (HTDOCS_ROOT, PROJECT_SLUG)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'common.utils.json.WPNIJSONPMiddleware',
    'common.utils.cache.WPNICacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)
