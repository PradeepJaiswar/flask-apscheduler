import logging
from config.env import get_config

class log(logging.getLoggerClass()):

    def __init__(self):
        formatter = logging.Formatter(get_config().LOGGING_FORMAT)
        level = get_config().LOGGING_LEVEL
        self.root.setLevel(get_config().LOGGING_LEVEL)
        self.root.handlers = []

        handler = logging.FileHandler(get_config().LOGGING_LOCATION)
        handler.setFormatter(formatter)
        self.root.addHandler(handler)

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
