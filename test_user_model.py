# test_user_model.py
import os
import pytest

from app import create_app
from extensions import db
from models import User


# # BEFORE we import our app, let's set an environmental variable
# # to use a different database for tests (we need to do this
# # before we import our app, since that will have already
# # connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


@pytest.fixture()
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config['TESTING'] = True
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    # Don't have WTForms use CSRF at all, since it's a pain to test
    app.config['WTF_CSRF_ENABLED'] = False
    with app.app_context():
        user1 = User(
            email="user1@test.com",
            username="user1",
            password="123"
        )
        user2 = User(
            email="user2@test.com",
            username="user2",
            password="HASHED_PASSWORD"
        )

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        db.create_all()
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


from sqlalchemy.exc import IntegrityError

def test_invalid_username_signup(app, client):
    # Test invalid username signup
    with pytest.raises(IntegrityError):
        User.signup(None, "test@test.com", "password", None)




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
        user1 = User.query.filter_by(username="user1").first()
        u = User.authenticate("user1" , "123")
        assert u is not None

