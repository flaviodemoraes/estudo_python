from typing import List

from .repositories import AbstractUserRepository
from ...domain.entities.user import User
from ...domain.services.user_service import UserService

class UserAppService:
    def __init__(self, repo: AbstractUserRepository, domain_service: UserService | None = None):
        self.repo = repo
        self.domain_service = domain_service or UserService()

    def create_user(self, name: str, email: str) -> User:
        user = User(id=None, name=name, email=email)
        self.domain_service.validate_user(user)
        return self.repo.add(user)

    def list_users(self) -> List[User]:
        return self.repo.list()

    def get_user(self, user_id: int) -> User | None:
        return self.repo.get(user_id)
