"""Config your app"""

import os


# Base Config class with common settings
class Config:
    CURR_USER_KEY = "curr_user"
    SECRET_KEY = os.environ.get('SECRET_KEY', 'hypto-krypto')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql:///warbler')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


# Development Config
class DevelopmentConfig(Config):
    DEBUG = True

# Production Config
class ProductionConfig(Config):
    # SQLALCHEMY_ECHO = False
    pass

# Testing Config
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory SQLite for testing
    

# Choose the appropriate configuration based on the environment
if os.environ.get('FLASK_ENV') == 'production':
    app_config = ProductionConfig
elif os.environ.get('FLASK_ENV') == 'testing':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig
