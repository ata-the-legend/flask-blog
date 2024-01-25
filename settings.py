import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "d8b23c19e91922798b701bbc46e49c542ee531fe6f747954544c50ac24f337a7"
    CSRF_KEY = "ac0234d4a13567ad984e3b9c0662fa9f8ca868e8cdde16edaaacd7478fc24add"

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR, 'app.db')

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ...