# # test_user_model.py

# import os
# import pytest

# from app import create_app
# from extensions import db
# from models import User

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
#     # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#     # Don't have WTForms use CSRF at all, since it's a pain to test
#     app.config['WTF_CSRF_ENABLED'] = False
#     with app.app_context():
#         user1 = User(
#             email="user1@test.com",
#             username="user1",
#             password="HASHED_PASSWORD"
#         )
#         user2 = User(
#             email="user2@test.com",
#             username="user2",
#             password="HASHED_PASSWORD"
#         )

#         db.session.add(user1)
#         db.session.add(user2)
#         db.session.commit()
#         db.create_all()
#         yield app
#         db.session.remove()
#         db.drop_all()


# @pytest.fixture()
# def client(app):
#     """A test client for the app."""
#     return app.test_client()

