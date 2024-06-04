from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import auth
import home
import user

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "thisisasecretkey"
    app.permanent_session_lifetime = timedelta(minutes=5)

    app.register_blueprint(auth.bp)    
    app.register_blueprint(home.bp)   
    app.register_blueprint(user.bp)   

    return app

app = create_app()
