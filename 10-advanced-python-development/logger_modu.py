import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("test_logger")

logger.info("This will not show up!")
logger.warning("This will.")
