import logging

logging.basicConfig(filename='example.log')
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# version 3.9: The encoding argument was added.
logging.debug('This message should go to the log file')
logging.warning('This is a WARNING message')
logging.error('This is an ERROR message')
logging.critical('This is a CRITICAL message')

# ref : https://docs.python.org/3/howto/logging.html

