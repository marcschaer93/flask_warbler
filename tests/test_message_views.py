"""Test message views"""

import os
os.environ['FLASK_ENV'] = "testing"

import pytest, pdb
from project.app import create_app
from project.extensions import db, bcrypt
from project.models import User, Message
from config import app_config


CURR_USER_KEY = "curr_user"
HASHED_PASSWORD = bcrypt.generate_password_hash("123456").decode('UTF-8')


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


def login(client, testuser):
    """Log in the test user."""
    with client.session_transaction() as sess:
        sess[CURR_USER_KEY] = testuser.id


def test_add_message(client, app):
    """Can user add a message?"""
    # pdb.debug = True
    # pdb.set_trace()
    with app.app_context():
        testuser = User.query.filter_by(username="user1").first()
        # Log in the test user
        login(client, testuser)

    # Make a POST request to add a message
    resp = client.post("/messages/new", data={"text": "Hello"})

    # Check if the response redirects
    assert resp.status_code == 302

    # Check if the message is added to the database
    msg = Message.query.one()
    assert msg.text == "Hello"
    assert Message.query.count() == 1


def test_show_message(client, app):
    """Can a User see a Message by ID ?"""
    
    with app.app_context():
        testuser = User.query.filter_by(username="user1").first()
        # Log in the test user
        login(client, testuser)

        
        msg = Message(id=999, text="New Message", user_id=testuser.id )
        db.session.add(msg)
        db.session.commit()

        #$$# NEWER method (2)
        # msg = Message.query.get(999)
        msg = db.session.get(Message, 999)

        
        resp = client.get(f"/messages/{msg.id}")

    
    assert Message.query.count() == 1
    assert resp.status_code == 200

    
    
    