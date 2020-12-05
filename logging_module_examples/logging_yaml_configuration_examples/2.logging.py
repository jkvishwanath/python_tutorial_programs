import os
import yaml
import logging
import logging.config


def setup_logging(default_path, default_level):
    with open(default_path, 'rt') as f:
        try:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        except Exception as e:
            print(e)
            print('Error in Logging Configuration. Using default configs')
            logging.basicConfig(level=default_level)


setup_logging('2.logging.yaml', logging.INFO)
print(__name__)
logger = logging.getLogger(__name__)
logger.debug("Debug inside the function")
logger.info("Info inside the function")
logger.warning("Warning inside the function")
logger.error("Error inside the function")
logger.critical("Critical inside the function")

# https://gist.github.com/kingspp/9451566a5555fb022215ca2b7b802f19
