import os.path
from django.conf import settings

MAILIN_MAX_SIZE = getattr(settings, "MAILIN_MAX_SIZE", 10000000)
MAILIN_MTA_HOSTS = getattr(settings, "MAILIN_MTA_HOSTS", [])

MAILIN_LOG_FILENAME = getattr(settings, "MAILIN_LOG_FILENAME", os.path.join(os.path.dirname(__import__('project').__file__), '..', 'log', 'mailin.log'))
MAILIN_LOG_MSG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
