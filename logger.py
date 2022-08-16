import logging

logger = logging.getLogger('PyDocker')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
