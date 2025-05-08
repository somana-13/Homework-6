"""
Logging configuration for the calculator application
"""
import os
import logging
import logging.handlers
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get logging configuration from environment variables
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
LOG_FILE = os.getenv('LOG_FILE', 'calculator_app.log')

# Map string level to logging constants
LOG_LEVEL_MAP = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}

def get_logger(name: str) -> logging.Logger:
    """
    Configure and return a logger with the given name.
    Args:
        name: The name for the logger, typically __name__ from the calling module
    Returns:
        A configured logger instance
    """
    # Create logger
    logger = logging.getLogger(name)
    if logger.handlers:
        # Logger already configured
        return logger

    # Set the logging level based on environment variable
    logger.setLevel(LOG_LEVEL_MAP.get(LOG_LEVEL, logging.INFO))

    # Create log directory if it doesn't exist
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    log_file_path = log_dir / LOG_FILE

    # Create formatters
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )

    # Create file handler for logging to a file
    file_handler = logging.handlers.RotatingFileHandler(
        log_file_path, maxBytes=1024*1024, backupCount=5
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(LOG_LEVEL_MAP.get(LOG_LEVEL, logging.INFO))

    # Create console handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(LOG_LEVEL_MAP.get(LOG_LEVEL, logging.INFO))

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
