from sqlalchemy.orm import Session

from .base import SQLAlchemyRepository
from .user_model import UserModel
from ...domain.entities.user import User

class UserRepository(SQLAlchemyRepository[UserModel]):
    def __init__(self, session: Session):
        super().__init__(UserModel, session)

    def add(self, user: User) -> User:
        model = UserModel(name=user.name, email=user.email)
        model = super().add(model)
        return User(id=model.id, name=model.name, email=model.email)

    def get(self, user_id: int) -> User | None:
        model = super().get(user_id)
        if model:
            return User(id=model.id, name=model.name, email=model.email)
        return None

    def list(self) -> list[User]:
        models = super().list()
        return [User(id=m.id, name=m.name, email=m.email) for m in models]
