import logging

logging.basicConfig(format=' %(asctime)s %(levelname)s:%(message)s', level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

# ref: https://docs.python.org/3/library/logging.html#logrecord-attributes
# ref: https://docs.python.org/3/howto/logging.html - Displaying the date/time in messages

