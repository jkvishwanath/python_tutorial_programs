import logging

logger = logging.getLogger("custom_log_instance_name")
handler = logging.FileHandler("Sample_file_name2.log")
logger.addHandler(handler)

logger.warning('This is a WARNING message')
logger.error('This is an ERROR message')
logger.critical('This is a CRITICAL message')

# https://pythonexamples.org/python-logging-to-file/
