import sys
import logging

# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify DEBUG or debug
# command prompt > python 3.Logging_to_file_set_level_command_prompt.py info

# Arguments passed
log_level = sys.argv[1]
numeric_level = getattr(logging, log_level.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % log_level)
logging.basicConfig(level=numeric_level,filename="Sample_file_3.log")


logging.debug('This message should go to the log file')
logging.warning('This is a WARNING message')
logging.error('This is an ERROR message')
logging.critical('This is a CRITICAL message')
