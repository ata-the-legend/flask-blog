import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "d8b23c19e91922798b701bbc46e49c542ee531fe6f747954544c50ac24f337a7"
    CSRF_KEY = "ac0234d4a13567ad984e3b9c0662fa9f8ca868e8cdde16edaaacd7478fc24add"
    SECURITY_PASSWORD_SALT = "899d183f75b8c86623ebda25de4d2a5de6732b9c3d9ccfcfe5c293ac7635951c"
    SECRET_KEY = "c01163e67a2f1dd94f78c604944fc6024aa0e369bae0c7155b95f0e865f2545f"
    
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR, 'app.db')

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ...