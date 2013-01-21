## Django settings for ASKBOT enabled project.
from os import path
import sys
import askbot
import secrets
import logging

PROJECT_ROOT = path.dirname(__file__)

# this line is added so that we can import pre-packaged askbot
# dependencies..
sys.path.append(path.join(
  path.dirname(askbot.__file__), 'deps'))

# to debug Jinja2 templates set DEBUG=True and TEMPLATE_DEBUG=False.
# it's strange, but this combination of settings makes the errors in templates
# trigger debugging output.
DEBUG = True
TEMPLATE_DEBUG = False
INTERNAL_IPS = secrets.internal_ips
ADMINS = secrets.admins
MANAGERS = ADMINS

DATABASES = {
  'default': {
    'ENGINE': secrets.db_engine,
    'NAME': secrets.db_name,
    'USER': secrets.db_user,
    'PASSWORD': secrets.db_pass,
    'HOST': secrets.db_host,
    'PORT': secrets.db_port
  }
}

# only postgres (>8.3) and mysql are supported so far others have
# not been tested yet..
DATABASE_ENGINE = secrets.db_engine
# Or path to database file if using sqlite3.
DATABASE_NAME = secrets.db_name
# # Not used with sqlite3.
DATABASE_USER = secrets.db_user
# Not used with sqlite3.
DATABASE_PASSWORD = secrets.db_pass
# Set to empty string for localhost. Not used with sqlite3.
DATABASE_HOST = secrets.db_host
# Set to empty string for default. Not used with sqlite3.
DATABASE_PORT = secrets.db_port

#outgoing mail server settings
SERVER_EMAIL = ''
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = ''
EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_USE_TLS = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# incoming mail settings
# after filling out these settings - please
# go to the site's live settings and enable the feature
# "Email settings" -> "allow asking by email"
#
#   WARNING: command post_emailed_questions DELETES all
#      emails from the mailbox each time
#      do not use your personal mail box here!!!
#
IMAP_HOST = ''
IMAP_HOST_USER = ''
IMAP_HOST_PASSWORD = ''
IMAP_PORT = ''
IMAP_USE_TLS = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'
SITE_ID = secrets.site_id

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
LANGUAGE_CODE = 'en'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
ASKBOT_FILE_UPLOAD_DIR = path.join(
  PROJECT_ROOT, 'upfiles')

# URL prefix for admin media.
# CSS, JavaScript and images. Make sure to use a trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin/media/'
# Make up some unique string, and don't share it with anybody.
SECRET_KEY = secrets.key

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.load_template_source',
  'django.template.loaders.app_directories.load_template_source',
  # below is askbot stuff for this tuple..
  'askbot.skins.loaders.load_template_source',
  # 'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
  # 'django.middleware.gzip.GZipMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  # 'django.middleware.cache.UpdateCacheMiddleware',
  'django.middleware.common.CommonMiddleware',
  # 'django.middleware.cache.FetchFromCacheMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  # 'django.middleware.sqlprint.SqlPrintingMiddleware',
  # below is askbot stuff for this tuple..
  'askbot.middleware.anon_user.ConnectToSessionMessagesMiddleware',
  'askbot.middleware.pagesize.QuestionsPageSizeMiddleware',
  'askbot.middleware.cancel.CancelActionMiddleware',
  'askbot.deps.recaptcha_django.middleware.ReCaptchaMiddleware',
  'django.middleware.transaction.TransactionMiddleware',
  # 'debug_toolbar.middleware.DebugToolbarMiddleware',
  'askbot.middleware.view_log.ViewLogMiddleware',
  'askbot.middleware.spaceless.SpacelessMiddleware',
)


ROOT_URLCONF = path.basename(PROJECT_ROOT) + '.urls'
FILE_UPLOAD_TEMP_DIR = path.join(PROJECT_ROOT, 'tmp'
  ).replace('\\','/')

FILE_UPLOAD_HANDLERS = (
  'django.core.files.uploadhandler.MemoryFileUploadHandler',
  'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)
ASKBOT_ALLOWED_UPLOAD_FILE_TYPES = (
  '.jpg', '.jpeg', '.gif', '.bmp', '.png', '.tiff')

# result in bytes..
ASKBOT_MAX_UPLOAD_FILE_SIZE = (1024 * 1024) * 3 #3MB
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# template have no effect in askbot, use the variable below..
# TEMPLATE_DIRS = (,)

# absolute path to your private skin collection.
# see: http://askbot.org/en/question/207/
ASKBOT_EXTRA_SKIN_DIR = path.join(
  PROJECT_ROOT, 'skins')

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.core.context_processors.request',
  'askbot.context.application_settings',
  # 'django.core.context_processors.i18n',
  # must be before auth..
  'askbot.user_messages.context_processors.user_messages',
  # this is required for admin..
  'django.core.context_processors.auth',
  # necessary for csrf protection..
  'django.core.context_processors.csrf',
)


INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  # all of these are needed for the askbot..
  'django.contrib.admin',
  'django.contrib.humanize',
  'django.contrib.sitemaps',
  # 'debug_toolbar',
  'askbot',
  'askbot.deps.django_authopenid',
  # stackexchange loader..
  # 'askbot.importers.stackexchange',
  'south',
  'askbot.deps.livesettings',
  'keyedcache',
  'robots',
  'django_countries',
  'djcelery',
  'djkombu',
  # to enable user following, see:
  # http://askbot.org/doc/optional-modules.html#follow-users
  # 'followit'
  # experimental, use git clone git://github.com/ericflo/django-avatar.git$
  # requires setting of MEDIA_ROOT and MEDIA_URL.
  # 'avatar',
)


# setup memcached for production use!
# see http://docs.djangoproject.com/en/1.1/topics/cache/ for details
CACHE_BACKEND = 'locmem://'
# needed for django-keyedcache..
CACHE_TIMEOUT = 6000
# make this unique..
CACHE_PREFIX = 'askbot'
# If you use memcache you may want to uncomment the following line to enable
# memcached based sessions..
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache_db'

AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'askbot.deps.django_authopenid.backends.AuthBackend',
)

LOG_FILENAME = 'askbot.log'
logging.basicConfig(
  filename=path.join(PROJECT_ROOT, 'log', LOG_FILENAME),
  level=logging.CRITICAL,
  format='%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
)

# this will allow running your forum with url like http://site.com/forum..
# no leading slash, default = '' empty string.
# ASKBOT_URL = 'forum/'
ASKBOT_URL = ''
_ = lambda v:v #fake translation function for the login url
LOGIN_URL = '/%s%s%s' % (ASKBOT_URL, _('account/'), _('signin/'))
# note - it is important that upload dir url is NOT translated!!!
# also, this url must not have the leading slash
ASKBOT_UPLOADED_FILES_URL = '%s%s' % (ASKBOT_URL, 'upfiles/')
ALLOW_UNICODE_SLUGS = False
# mimic url scheme of stackexchange
ASKBOT_USE_STACKEXCHANGE_URLS = False

# celery Settings
BROKER_BACKEND = "djkombu.transport.DatabaseTransport"
CELERY_ALWAYS_EAGER = True
import djcelery
djcelery.setup_loader()

CSRF_COOKIE_NAME = 'askbot_csrf'
# enter domain hostname here - e.g. example.com
CSRF_COOKIE_DOMAIN = 'global.themedco.com'
