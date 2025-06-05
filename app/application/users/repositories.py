from __future__ import annotations
from typing import List, Protocol

from ...domain.entities.user import User

class AbstractUserRepository(Protocol):
    def add(self, user: User) -> User:
        ...

    def get(self, user_id: int) -> User | None:
        ...

    def list(self) -> List[User]:
        ...
