import logging
import sys


def create_logger():
    logger = logging.getLogger()
    console_handler = logging.FileHandler(
        "/Users/elenayanushevskaya/Desktop/diplom/.log"
    )
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.setLevel(logging.INFO)

    return logger
