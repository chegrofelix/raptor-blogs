import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:ragnarok@localhost/moringa'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = 'Ethylenediaminetetraaceticacid'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True    
    DEBUG = True

class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
     pass
    
     
class TestConfig(Config):
   
    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}