import os

from . import *  # noqa: F403
import dj_database_url

# This is NOT a complete production settings file. For more, see:
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}