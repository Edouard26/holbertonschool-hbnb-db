from src.models.user import User
import unittest

def test_create_user(session):
    user_data = {
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "password123",
        "is_admin": False
    }
    user = User.create(user_data)
    session.add(user)
    session.commit()

    fetched_user = session.query(User).filter_by(email="test@example.com").first()
    assert fetched_user is not None
    assert fetched_user.first_name == "Test"
    assert fetched_user.last_name == "User"

def test_update_user(session):
    user = session.query(User).filter_by(email="test@example.com").first()
    User.update(user.id, {"first_name": "Updated"})
    session.commit()

    updated_user = session.query(User).filter_by(email="test@example.com").first()
    assert updated_user.first_name == "Updated"

def test_delete_user(session):
    user = session.query(User).filter_by(email="test@example.com").first()
    session.delete(user)
    session.commit()

    deleted_user = session.query(User).filter_by(email="test@example.com").first()
    assert deleted_user is None