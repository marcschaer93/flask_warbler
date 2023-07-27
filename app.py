import os

from flask import Flask
from extensions import db, debug, bcrypt
from routes import main


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

    # Load configuration and set up other app settings (if needed)

    # Initialize the database, debugToolbar
    db.init_app(app)
    debug.init_app(app)
    bcrypt.init_app(app)

    # Import and register blueprints
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    # Import and register Blueprints (if you have any)
    # Example:
    # from .blueprints import some_blueprint
    # app.register_blueprint(some_blueprint)

    return app



# Call the create_app function to get the Flask app instance
app = create_app()


if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)