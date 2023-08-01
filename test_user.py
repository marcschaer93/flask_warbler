"""test_user_model.py"""

from extensions import db
from models import User

def test_user_model(app):
    # Create a user inside the app context
    with app.app_context():
        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )
        db.session.add(u)
        db.session.commit()

    # Access the 'messages' attribute inside the app context
    with app.app_context():
        user = User.query.filter_by(username="testuser").first()
        assert len(user.messages) == 0
        assert len(user.followers) == 0