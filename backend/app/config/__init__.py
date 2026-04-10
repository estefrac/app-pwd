import os
from dotenv import load_dotenv

load_dotenv(override=True) # Recarga las variables de entorno desde el archivo .env

class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'SECRET_KEY') # Valor por defecto si no se encuentra la variable de entorno
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600)) # Valor por defecto de 1 hora si no se encuentra la variable de entorno

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
