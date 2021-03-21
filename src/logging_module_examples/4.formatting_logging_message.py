import logging

# To display the date and time of an event, you would place ‘%(asctime)s’ in your format string:
# The default format for date/time display (shown above) is like ISO8601 or RFC 3339.
# If you need more control over the formatting of the date/time, provide a datefmt argument to basicConfig.

logging.basicConfig(format=' %(asctime)s  %(levelname)s:%(message)s', level=logging.INFO,
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

# ref: https://docs.python.org/3/library/logging.html#logrecord-attributes
# ref: https://docs.python.org/3/howto/logging.html - Displaying the date/time in messages
