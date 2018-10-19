"""
configurations for the app
"""

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "16896"

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    ENV = 'development'
    SECRET_KEY = "16896"

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "16896"




