"""Logging utility for the calculator application."""

import logging
import sys


def setup_logger(name: str = "calculator", level: int = logging.INFO) -> logging.Logger:
    """Sets up and returns a logger instance.

    Args:
        name: The name of the logger.
        level: The logging level.

    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
