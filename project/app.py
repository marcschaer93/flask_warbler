# import os

# from flask import Flask
# from project.extensions import db, debug, bcrypt


# # Config
# CURR_USER_KEY = "curr_user"

# ###############################################################################################
# # CREATE_APP

# def create_app():
#     app = Flask(__name__)
#     # app.config['TEMPLATES_AUTO_RELOAD'] = True
#     # Get DB_URI from environ variable (useful for production/testing) or,
#     # if not set there, use development local db.
#     app.config['SQLALCHEMY_DATABASE_URI'] = (
#         os.environ.get('DATABASE_URL', 'postgresql:///warbler'))

#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_ECHO'] = False
#     app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
#     app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")

#     # Load configuration and set up other app settings (if needed)

#     # Initialize the database, debugToolbar
#     db.init_app(app)
#     # debug.init_app(app)
#     bcrypt.init_app(app)

 
#     # Import and register blueprints

#     from project.views.home import home
#     from project.views.auth import auth_bp
#     from project.views.profile import profile_bp
#     from project.views.message import message_bp
    
#     app.register_blueprint(home)
#     app.register_blueprint(auth_bp, url_prefix="")
#     app.register_blueprint(profile_bp, url_prefix="/users")
#     app.register_blueprint(message_bp, url_prefix="/messages")

#     with app.app_context():
#         db.create_all()

#     # Import and register Blueprints (if you have any)
#     # Example:
#     # from .blueprints import some_blueprint
#     # app.register_blueprint(some_blueprint)

#     return app



# # Call the create_app function to get the Flask app instance
# # app = create_app()


# # if __name__ == '__main__':
# #     # Run the Flask development server
# #     app.run(debug=True)



# app/__init__.py

import os
from flask import Flask
from project.extensions import db, bcrypt
from config import app_config

def create_app():
    app = Flask(__name__)

    ## Load configuration from config.py
    # app.config.from_object('config')
    app.config.from_object(app_config)

    # Initialize the database and bcrypt
    db.init_app(app)
    bcrypt.init_app(app)

    # Import and register blueprints
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
