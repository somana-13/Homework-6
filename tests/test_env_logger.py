"""
Tests for environment variables and logging functionality
"""
import os
import logging
import pytest
from utils.env_config import EnvConfig
from utils.logger import get_logger

def test_env_config_loading():
    """Test that environment variables are loaded correctly"""
    # Test that default values are set
    assert isinstance(EnvConfig.APP_ENV, str)
    assert isinstance(EnvConfig.DEMO_API_KEY, str)
    assert isinstance(EnvConfig.ENABLE_ADVANCED_OPERATIONS, bool)
    
    # Test helper methods
    assert EnvConfig.is_development() == (EnvConfig.APP_ENV.lower() == 'development')
    assert EnvConfig.is_production() == (EnvConfig.APP_ENV.lower() == 'production')
    assert EnvConfig.is_testing() == (EnvConfig.APP_ENV.lower() == 'testing')
    
    # Test get_env_var method
    test_var = EnvConfig.get_env_var('TEST_VAR', 'default_value')
    assert test_var == 'default_value'
    
    # Set an environment variable temporarily and test
    os.environ['TEST_VAR'] = 'test_value'
    test_var = EnvConfig.get_env_var('TEST_VAR', 'default_value')
    assert test_var == 'test_value'
    
    # Clean up
    del os.environ['TEST_VAR']

def test_logger_configuration():
    """Test that logger is properly configured"""
    # Get a test logger
    logger = get_logger('test_logger')
    
    # Verify logger is configured correctly
    assert logger.name == 'test_logger'
    assert logger.level <= logging.INFO
    
    # Verify handlers are set up
    assert logger.handlers
    assert any(isinstance(handler, logging.handlers.RotatingFileHandler) for handler in logger.handlers)
    assert any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)
    
    # Test logging (this just ensures no exceptions are raised)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    
    # Check log file exists
    import pathlib
    log_dir = pathlib.Path('logs')
    assert log_dir.exists()
    
    # No need to verify file contents, just confirm logging doesn't raise exceptions
