import pytest
from typing import List
from app.application.users.services import UserAppService
from app.domain.entities.user import User
from app.application.users.repositories import AbstractUserRepository


class InMemoryUserRepo(AbstractUserRepository):
    def __init__(self):
        self.users: List[User] = []
        self.next_id = 1

    def add(self, user: User) -> User:
        user.id = self.next_id
        self.next_id += 1
        self.users.append(user)
        return user

    def get(self, user_id: int) -> User | None:
        for u in self.users:
            if u.id == user_id:
                return u
        return None

    def list(self) -> List[User]:
        return list(self.users)


def test_create_and_get_user():
    repo = InMemoryUserRepo()
    service = UserAppService(repo)
    created = service.create_user('Alice', 'alice@example.com')
    assert created.id == 1
    assert service.get_user(created.id) == created
    assert service.list_users() == [created]


def test_create_user_invalid_email():
    repo = InMemoryUserRepo()
    service = UserAppService(repo)
    with pytest.raises(ValueError):
        service.create_user('Bob', 'invalid')
