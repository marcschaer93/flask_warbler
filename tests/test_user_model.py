# test_user_model.py
import os
# # BEFORE we import our app, let's set an environmental variable
# # to use a different database for tests (we need to do this
# # before we import our app, since that will have already
# # connected to the database
#$$# Put this on top !!!
os.environ['FLASK_ENV'] = 'testing'



import pytest
from project.app import create_app
from project.extensions import db, bcrypt
from project.models import User
from config import TestingConfig, app_config
from sqlalchemy.exc import IntegrityError


#$$#
HASHED_PASSWORD = bcrypt.generate_password_hash("123").decode('UTF-8')


@pytest.fixture()
def app():
    """Create and configure a new app instance for each test."""
    
    app = create_app()
    # app.config.from_object(TestingConfig)
    #$$#
    print("App Config:", app_config)
    print("SQLALCHEMY_DATABASE_URI:", app.config['SQLALCHEMY_DATABASE_URI'])
     # Don't have WTForms use CSRF at all, since it's a pain to test
    app.config['WTF_CSRF_ENABLED'] = False
    with app.app_context():
        db.create_all()
        user1 = User(
            email="user1@test.com",
            username="user1",
            password=HASHED_PASSWORD
        )
        user2 = User(
            email="user2@test.com",
            username="user2",
            password=HASHED_PASSWORD
        )

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    """A test client for the app."""
    
    return app.test_client()


def test_signup_route(app, client):
    # Test successful signup
    response = client.post("/signup", data={
        "username": "testuser",
        "email": "test@testuser.com",
        "password": "testuser",
        "image_url": None,
        
    }, follow_redirects=True)

    assert response.status_code == 200
    with app.app_context():
        user = User.query.filter_by(username="testuser").first()
        
        assert User.query.count() == 3
        assert user is not None
        assert user.email == "test@testuser.com"
        assert user.username == "testuser"
        assert user.password.startswith("$2b$") == True
        assert repr(user) == "<User #3: testuser, test@testuser.com>"


def test_invalid_username_signup(app, client):
    # Test invalid username signup
    with pytest.raises(IntegrityError):
        User.signup("user1", "test@test.com", "password", None)
        ####
        db.session.commit() # Commit the transaction to trigger the IntegrityError

        
def test_invalid_email_signup(app, client):
    # Test invalid username signup
    with pytest.raises(IntegrityError):
        User.signup("user_no_mail", None, "password", None)
        ####
        db.session.commit() # Commit the transaction to trigger the IntegrityError

        
def test_invalid_password_signup(app, client):
    # Test invalid username signup
    with pytest.raises(ValueError):
        User.signup("wrong", "wrong@gmail.com" , "", None)
        ####
        db.session.commit() # Commit the transaction to trigger the ValueError
        
        User.signup("wrong", "wrong@gmail.com" , None, None)
        ####
        db.session.commit() # Commit the transaction to trigger the ValueError


def test_is_following(app):
    # Create a user inside the app context
    with app.app_context():
        user1 = User.query.filter_by(username="user1").first()
        user2 = User.query.filter_by(username="user2").first()
        user1.following.append(user2)
        db.session.commit()

    # Ensure there are two users in the database
        assert User.query.count() == 2
        assert User.query.filter_by(username="user1").first() is not None
        assert User.query.filter_by(username="user2").first() is not None
        assert user1.is_following(user2) is True
        assert user2.is_following(user1) is False

        
def test_is_followed_by(app):
     with app.app_context():
        user1 = User.query.filter_by(username="user1").first()
        user2 = User.query.filter_by(username="user2").first()
        user2.following.append(user1)
        db.session.commit()

    # Ensure there are two users in the database
        assert User.query.count() == 2
        assert User.query.filter_by(username="user1").first() is not None
        assert User.query.filter_by(username="user2").first() is not None
        assert user1.is_followed_by(user2) is True
        assert user2.is_followed_by(user1) is False


def test_valid_authentication(app):
    with app.app_context():
        u = User.authenticate("user1" , "123")
        assert u is not False

        
def test_invalid_username(app):
    with app.app_context():
        result = User.authenticate("fritz", "123")
        assert result is False

        
def test_invalid_password(app):
    with app.app_context():
        result = User.authenticate("user1", "1")
        assert result is False

        
