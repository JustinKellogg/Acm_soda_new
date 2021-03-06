# Django settings for acm_soda project.
import socket
import os
import django.template.loaders.filesystem

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SODA_FIFO_IN = '/tmp/vendsodain'
SODA_FIFO_OUT = '/tmp/vendsodaout'

ADMINS = (
    ('Josh Bohde', 'josh.bohde@gmail.com'),
    ('Justin Kellogg', 'justin.kellogg@mst.edu')
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '../soda.db', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://127.0.0.1:8000/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'hc)0=ded!zn_kebxvuzy$ll-mooon!8b)yf67xz@=#43@(an6a'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
  #  'django.template.loaders.filesystem.load_template_source',
  #  'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'acm_soda.urls'

TEMPLATE_DIRS = (
    #'/home/numix/code/acm_soda/templates/',
  #  "C:/Users/Justin/PycharmProjects/Acm_soda_new/acm_soda/templates",
    os.path.join(os.path.dirname(__file__), 'templates'),

    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'acm_soda.api',
    'acm_soda.web',
    'django.contrib.admin'
)

STATIC_DOC_ROOT = '/nethome/users/jrl2n4/acmsoda/acm_soda/media'
LOGIN_REDIRECT_URL = 'web/profile'
LOGIN_URL = '/web/login'

# Override these settings w/ production settings if on the Soda Server
#if socket.gethostname() == 'acmsoda':
#    try:
#        from production_settings import *
#    except ImportError, exp:
#        pass
