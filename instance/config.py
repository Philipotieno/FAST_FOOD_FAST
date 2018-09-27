'''Set up environment specific configurations'''
import os

class Config(object):
    '''Parent configuration class'''
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')

class Development(Config):
    '''Configuration for development environment'''
    DEBUG = True
    APP_SETTINGS = "development"

class Testing(Config):
    '''Configuration for testing environment'''
    DEBUG = True
    TESTING = True
    DB_NAME = os.getenv('TEST_DB')
    APP_SETTINGS = "testing"

class Production(Config):
    '''Configuration for production environment'''
    DEBUG = False
    TESTING = False
    APP_SETTINGS = "production"

'''Used to export the above environments'''
app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production
    }
    