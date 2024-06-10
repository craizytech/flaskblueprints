from datetime import timedelta

class Config:
    SECRET_KEY = "thisisasecretkey"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
    # SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    # use postgres for production

class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"

class Testing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    

class Production(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/dbname"
    
configs = {
    "development": Development,
    "production": Production,
    "default": Development,
    "test": Testing
}
