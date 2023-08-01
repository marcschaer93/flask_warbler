# test_user_model.py

import os
import pytest

from app import create_app
from extensions import db

# # BEFORE we import our app, let's set an environmental variable
# # to use a different database for tests (we need to do this
# # before we import our app, since that will have already
# # connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


@pytest.fixture()
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture()
def client(app):
    """A test client for the app."""
    return app.test_client()
    
    