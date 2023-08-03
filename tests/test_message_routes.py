# # test_message_routes.py

# import os
# import pytest

# from app import create_app
# from extensions import db
# from models import User, Message

# # # BEFORE we import our app, let's set an environmental variable
# # # to use a different database for tests (we need to do this
# # # before we import our app, since that will have already
# # # connected to the database

# os.environ['DATABASE_URL'] = "postgresql:///warbler-test"



# @pytest.fixture()
# def app():
#     """Create and configure a new app instance for each test."""
#     app = create_app()
#     app.config['TESTING'] = True
#     # Don't have WTForms use CSRF at all, since it's a pain to test
#     app.config['WTF_CSRF_ENABLED'] = False
#     with app.app_context():
#         db.create_all()
#         yield app
#         # db.drop_all()
#         testuser = User.signup(username="testuser",
#                                 email="test@test.com",
#                                 password="testuser",
#                                 image_url=None)

#         db.session.add(testuser)
#         db.session.commit()


# CURR_USER_KEY = "curr_user"



# @pytest.fixture
# def client(app):
#     """Create a test client for the app."""
#     with app.test_client() as client:
#         with app.app_context():
#             yield client


# def login(client, testuser):
#     """Log in the test user."""
#     with client.session_transaction() as sess:
#         sess[CURR_USER_KEY] = testuser.id


# def test_add_message(client):
#     """Can user add a message?"""

#     # Create a test user in the database
#     testuser = User(
#         email="test@test.com",
#         username="testuser",
#         password="HASHED_PASSWORD"
#     )
#     db.session.add(testuser)
#     db.session.commit()

#     # Log in the test user
#     login(client, testuser)

#     # Make a POST request to add a message
#     resp = client.post("/messages/new", data={"text": "Hello"})

#     # Check if the response redirects
#     assert resp.status_code == 302

#     # Check if the message is added to the database
#     msg = Message.query.one()
#     assert msg.text == "Hello"
    
    