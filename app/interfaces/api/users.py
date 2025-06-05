from fastapi import APIRouter, Depends, HTTPException

from ...application.users.services import UserAppService
from ...application.users.schemas import UserCreate, UserRead
from ...infrastructure.database import SessionLocal
from ...infrastructure.repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["users"])


def get_service():
    db = SessionLocal()
    try:
        repo = UserRepository(db)
        service = UserAppService(repo)
        yield service
    finally:
        db.close()


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, service: UserAppService = Depends(get_service)):
    try:
        new_user = service.create_user(user.name, user.email)
        return UserRead.from_orm(new_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[UserRead])
def list_users(service: UserAppService = Depends(get_service)):
    users = service.list_users()
    return [UserRead.from_orm(u) for u in users]


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, service: UserAppService = Depends(get_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserRead.from_orm(user)
