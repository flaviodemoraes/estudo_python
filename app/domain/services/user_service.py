from ..entities.user import User

class UserService:
    """Domain service with business rules for Users"""

    def validate_user(self, user: User) -> None:
        if not user.email or '@' not in user.email:
            raise ValueError('Invalid email')
