import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    TESTING = False

class DevConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
