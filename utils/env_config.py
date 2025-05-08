"""
Environment variable configuration for the calculator application
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class EnvConfig:
    """
    Class to handle environment variable configuration
    """
    # Application environment
    APP_ENV = os.getenv('APP_ENV', 'development')
    
    # API keys and credentials
    DEMO_API_KEY = os.getenv('DEMO_API_KEY', 'default_key')
    
    # Feature flags
    ENABLE_ADVANCED_OPERATIONS = os.getenv('ENABLE_ADVANCED_OPERATIONS', 'false').lower() == 'true'
    
    @classmethod
    def is_development(cls) -> bool:
        """Check if the application is running in development mode"""
        return cls.APP_ENV.lower() == 'development'
    
    @classmethod
    def is_production(cls) -> bool:
        """Check if the application is running in production mode"""
        return cls.APP_ENV.lower() == 'production'
    
    @classmethod
    def is_testing(cls) -> bool:
        """Check if the application is running in testing mode"""
        return cls.APP_ENV.lower() == 'testing'
    
    @classmethod
    def get_env_var(cls, var_name: str, default: str = None) -> str:
        """
        Get an environment variable by name
        
        Args:
            var_name: Name of the environment variable
            default: Default value if the variable is not set
            
        Returns:
            The value of the environment variable or the default value
        """
        return os.getenv(var_name, default)
