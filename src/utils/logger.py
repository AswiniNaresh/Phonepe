import logging
from src.config import Config

def setup_logging():
    logging.basicConfig(
        level=getattr(logging, Config.LOG_LEVEL),
        format=Config.LOG_FORMAT
    )

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
