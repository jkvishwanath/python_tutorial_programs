import logging
import logging.config

logging.config.fileConfig(fname='1.log.conf', disable_existing_loggers=False)

logger = logging.getLogger('dev')
logger.info('This is an information message')

# ref: http://zetcode.com/python/logging/
