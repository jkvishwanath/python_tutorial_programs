import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(filename="mylog.log", maxBytes=2000, backupCount=10)
logger.addHandler(handler)

for _ in range(10000):
    logger.warning('Hello, world!')
