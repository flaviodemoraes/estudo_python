from __future__ import annotations
from typing import Generic, Type, TypeVar, List
from sqlalchemy.orm import Session

from ..database import Base

ModelType = TypeVar("ModelType", bound=Base)

class SQLAlchemyRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: Session):
        self.model = model
        self.session = session

    def add(self, obj: ModelType) -> ModelType:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def get(self, obj_id: int) -> ModelType | None:
        return self.session.query(self.model).filter(self.model.id == obj_id).first()

    def list(self) -> List[ModelType]:
        return self.session.query(self.model).all()
