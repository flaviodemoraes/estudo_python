import pytest
from app.domain.entities.user import User
from app.domain.services.user_service import UserService


def test_validate_user_valid_email():
    user = User(id=None, name='Test', email='test@example.com')
    service = UserService()
    service.validate_user(user)


def test_validate_user_invalid_email():
    user = User(id=None, name='Test', email='invalid-email')
    service = UserService()
    with pytest.raises(ValueError):
        service.validate_user(user)
