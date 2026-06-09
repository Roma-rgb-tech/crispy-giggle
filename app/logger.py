import logging
import sys
from pythonjsonlogger import jsonlogger
import logging_loki
import os

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(jsonlogger.JsonFormatter(
        fmt="%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S"
    ))
    logger.addHandler(stdout_handler)

    loki_url = os.getenv("LOKI_URL")
    loki_user = os.getenv("LOKI_USER")
    loki_token = os.getenv("LOKI_TOKEN")

    if loki_url and loki_user and loki_token:
        loki_handler = logging_loki.LokiHandler(
            url=f"{loki_url}/loki/api/v1/push",
            tags={"app": "fastapi", "env": os.getenv("ENV", "production")},
            auth=(loki_user, loki_token),
            version="1",
        )
        logger.addHandler(loki_handler)

    return logger

logger = setup_logger()