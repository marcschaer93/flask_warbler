import os
import unittest
from app import create_app, db
from models import User, Message, Follows, Likes

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


class UserModelTestCase(unittest.TestCase):
    """Test the User model."""

    def setUp(self):
        """Create test client, add sample data."""
        self.app = create_app()  # Create the Flask app
        
        with self.app.app_context():  # Enter the app context
            db.create_all()  # Create the necessary tables for the test database
            
        self.client = self.app.test_client()

    def tearDown(self):
        """Clean up after each test."""
        with self.app.app_context():  # Enter the app context
            db.session.remove()  # Close the database session
            db.drop_all()  # Drop the tables

    def test_user_model(self):
        """Does basic User model work?"""
        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

    def test_user_signup(self):
        """Test User signup method."""
        user = User.signup(
            username="testuser",
            email="test@test.com",
            password="password",
            image_url="image.jpg"
        )
        db.session.commit()

        # Check if user was added to the database
        self.assertEqual(User.query.filter_by(username="testuser").first(), user)

    def test_user_authentication(self):
        """Test User authenticate method."""
        user = User.signup(
            username="testuser",
            email="test@test.com",
            password="password",
            image_url="image.jpg"
        )
        db.session.commit()

        # Test correct authentication
        authenticated_user = User.authenticate("testuser", "password")
        self.assertEqual(authenticated_user, user)

        # Test incorrect authentication
        authenticated_user = User.authenticate("testuser", "wrongpassword")
        self.assertFalse(authenticated_user)


if __name__ == '__main__':
    unittest.main()
