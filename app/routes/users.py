
from fastapi import APIRouter
from app.schemas import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])

users = []

@router.post("/")
def create_user(user: UserCreate):
    users.append(user)
    return {"message": "User created", "user": user}
