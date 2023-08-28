import os

os.environ['FLASK_ENV'] = 'testing'

import pytest
from project.app import create_app
from project.extensions import db, bcrypt
from project.models import Message, User
from config import TestingConfig, app_config
from sqlalchemy.exc import IntegrityError


HASHED_PASSWORD = bcrypt.generate_password_hash("123").decode('UTF-8')

@pytest.fixture()
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    print("App-Config:", app_config)
    app.config['TESTING'] = True
#     # Don't have WTForms use CSRF at all, since it's a pain to test
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        testuser = User(
            email="user1@test.com",
            username="user1",
            password=HASHED_PASSWORD
        )
    
        db.session.add(testuser)
        db.session.commit()
        yield app
        # db.drop_all()

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_empty_message(app):
    with pytest.raises(IntegrityError):
        new_message = Message(text="")
        db.session.add(new_message)
        db.session.commit()



    







