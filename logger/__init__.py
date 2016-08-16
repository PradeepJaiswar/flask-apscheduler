import logging
from config.env import get_config
from flask import g

class AppFilter(logging.Filter):
    def filter(self, record):
        record.correlationId = get_correlation_id()
        return True

class log(logging.getLoggerClass()):

    def __init__(self):
        formatter = logging.Formatter(get_config().LOGGING_FORMAT)
        self.root.setLevel(get_config().LOGGING_LEVEL)
        self.root.handlers = []

        handler = logging.FileHandler(get_config().LOGGING_LOCATION)
        handler.setFormatter(formatter)
        self.root.addFilter(AppFilter())

        self.root.addHandler(handler)


    def debug(self, message):
        self.root.debug(message)

    def debug(self, message):
        self.root.debug(message)

    def info(self, message):
        self.root.info(message)

    def warning(self, message):
        self.root.warning(message)

    def error(self, message):
        self.root.error(message)

    def critical(self, message):
        self.root.critical(message)


def get_correlation_id():
    """
    Return the correlation Id stored in thread local storage.
    """
    return g.get('correlation_id')
