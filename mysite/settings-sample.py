# Django settings for mysite project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG


# path to here, including the mysite dir at the end. with trailing slash
ABS_PATH_TO_THIS_REPO = '/home/pyrak/webs/ocw-dartmouth-site/mysite/'

DATA_ROOT = ABS_PATH_TO_THIS_REPO + 'static/data/'

RELATIVE_DATA_ROOT = '/static/data/'

data_sqlite_db_user =  ''
data_sqlite_db_pass =  ''
data_sqlite_db_host =  ''
data_sqlite_db_db = DATA_ROOT + 'metadata.sqlite'

#data_sqlite_db = create_engine('sqlite://%s:%s@%s/%s' % (data_sqlite_db_user, data_sqlite_db_pass, data_sqlite_db_host, data_sqlite_db_db))

METADATA_ENGINE = 'sqlite://%s:%s@%s/%s' % (data_sqlite_db_user, data_sqlite_db_pass, data_sqlite_db_host, data_sqlite_db_db)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('Parker Phinney', 'gameguy43@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'site_database.sqlite3'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

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
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'fln2&5&ko09oyn0^08vmwv-n*6v*tne-s^+6o3+ggg2dk&k$fx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ABS_PATH_TO_THIS_REPO + 'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
)

STATIC_DOC_ROOT = ABS_PATH_TO_THIS_REPO  + 'static/'
