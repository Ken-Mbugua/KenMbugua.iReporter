import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    # DATABASE_URL = os.getenv('DATABASE_URL')
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    PORT = os.getenv("APP_PORT")


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    TEST_DB_NAME = os.getenv("TEST_DB_NAME")


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
