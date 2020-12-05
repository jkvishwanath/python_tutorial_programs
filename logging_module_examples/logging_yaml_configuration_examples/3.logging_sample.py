import logging
import logging.config
import yaml

with open('3.logging_sample.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')

# ref : https://realpython.com/lessons/logger-dictionary/
