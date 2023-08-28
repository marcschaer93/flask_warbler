################################################################################################
# # CREATE_APP


import os
from flask import Flask
from project.extensions import db, bcrypt, debug
from config import app_config

def create_app():
    app = Flask(__name__)

    ## Load configuration from config.py
    app.config.from_object(app_config)

    ## Initialize the database and bcrypt
    db.init_app(app)
    bcrypt.init_app(app)

     ## Initialize the debug toolbar
    debug.init_app(app)

    ## Import and register blueprints
    from project.views.home import home
    from project.views.auth import auth_bp
    from project.views.profile import profile_bp
    from project.views.message import message_bp
    
    app.register_blueprint(home)
    app.register_blueprint(auth_bp, url_prefix="")
    app.register_blueprint(profile_bp, url_prefix="/users")
    app.register_blueprint(message_bp, url_prefix="/messages")

    with app.app_context():
        db.create_all()

    return app
