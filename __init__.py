import os

from flask import Flask
from .extensions import db

def create_app():
    app = Flask(__name__)
    
    # Get DB_URI from environ variable (useful for production/testing) or,
    # if not set there, use development local db.
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        os.environ.get('DATABASE_URL', 'postgresql:///warbler'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")

    db.init_app(app)
   

    # Import and register Blueprints (if you have any)
    # Example:
    # from .blueprints import some_blueprint
    # app.register_blueprint(some_blueprint)

    return app