import logging
from logging.config import fileConfig

fileConfig('2.logging_config.ini')
logger = logging.getLogger()
logger.debug('the best scripting language is python in the world')