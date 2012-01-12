import os

import django

# a few aliased helpers
dirname = os.path.dirname
join = os.path.join

# GLOBAL DYNAMIC SETTINGS
DJANGO_ROOT = dirname(os.path.realpath(django.__file__))
PROJECT_ROOT = os.path.abspath(join(dirname(__file__),"..",".."))

# GLOBAL CUSTOM SETTING FOR CONFIGURING URLS AND SUCH
PROJECT_SLUG = 'sacredheartcs'

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

SECRET_KEY = '0@(8ia6dc9(k#t!8^q02j^w=8mc^rj#cg=3-4@70%^5b)v9fcc'

ADMINS = (
    ('Serdar', 'zstumgoren@gmail.com'),
)
MANAGERS = ADMINS
DEBUG = False
TEMPLATE_DEBUG = DEBUG
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
ROOT_URLCONF = '%s.config.base.urls' % PROJECT_SLUG

# Statics are collected out of an apps' /static/ 
# folders via management command; Below settings control where 
# an apps' static files are moved to, for example:
#  /home/sacredheartcs/www/static/sacredheartcs/
#  http://my.mediaserver.com/apps/static/sacredheartcs/
STATIC_URL = 'http://127.0.0.1/apps/static/%s/' % PROJECT_SLUG
STATIC_ROOT = PROJECT_ROOT + '/static/%s/' % PROJECT_SLUG

# Admin uploads need to be configured to go to MEDIA_ROOT
MEDIA_URL = 'http://127.0.0.1/apps/media/%s/' % PROJECT_SLUG
MEDIA_ROOT = PROJECT_ROOT + '/media/%s/' % PROJECT_SLUG

#ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'

# NOTE: This is overridden in each env, not appended to, b/c order is significant.
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)

# Templates are found in each app's templates/<appname> folder.
TEMPLATE_DIRS = (
     #join(PROJECT_ROOT, 'templates'),
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
