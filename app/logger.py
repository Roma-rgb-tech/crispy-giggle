import logging 
import sys
from pythonjsonlogger import jsonlogger

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    
    
    handler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(
        fmt="%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()