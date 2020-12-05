import logging

logging.basicConfig(
    format=' Date:%(asctime)s, created_at:%(created)f, Log_message:%(levelname)s:%(message)s. File:%(filename)s, \n'
           'Function_name:%(funcName)s, level:%(levelname)s, Line_no:%(lineno)d, Module:%(module)s, \n'
           'Logger_name:%(name)s, Process:%(process)d, Path:%(pathname)s \n'
           'args=(1), exc_info=None', level=logging.INFO,
    datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

# https://docs.python.org/3/library/logging.html#logrecord-attributes
# Date Guide - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# missing fields - msg,args , exc_info
