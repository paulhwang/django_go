import logging

logger = logging.getLogger(__name__)

def utilLogit(str1, str2):
    logger.error("%s() %s", str1, str2)

def utilAbend(str1, str2):
    logger.error("Abend %s() %s", str1, str2)
