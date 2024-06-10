from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import auth
import home
import user
import os

from config import configs


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(configs[config])
    
    app.register_blueprint(auth.bp, url_prefix="/authentication")    
    app.register_blueprint(home.bp, url_prefix="/home")   
    app.register_blueprint(user.bp)   

    return app

app = create_app(os.getenv("FLASK_ENV") or "default")


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Page not found<h1>", 404
