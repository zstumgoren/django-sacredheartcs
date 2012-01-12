import sys

from config.base.settings import *

if 'test' in sys.argv:
    #FIXTURE_DIRS = (
    #    PROJECT_ROOT + '/apps/outreach/tests/fixtures',
    #)
    SOUTH_TESTS_MIGRATE = False

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
    'debug_toolbar',
    'django_extensions',
    'south'
    #'autocomplete',
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS=('127.0.0.1')

ROOT_URLCONF = 'config.dev.urls'

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    #'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
    #'HIDE_DJANGO_SQL': False,
    #'TAG': 'div',
}

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.contrib.auth.context_processors.auth',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
