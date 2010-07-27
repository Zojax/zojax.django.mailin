import logging, logging.handlers, os

from zojax.django.mailin import settings

LOGGING_INITIATED = False

def init_logging():
    logger = logging.getLogger('zojax.django.mailin')
    logger.setLevel(logging.INFO)
    try:
        os.makedirs(os.path.dirname(settings.MAILIN_LOG_FILENAME))
    except OSError:
        pass
    handler = logging.handlers.TimedRotatingFileHandler(settings.MAILIN_LOG_FILENAME, when = 'midnight')
    formatter = logging.Formatter(settings.MAILIN_LOG_MSG_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

if not LOGGING_INITIATED:
    LOGGING_INITIATED = True
    init_logging()
