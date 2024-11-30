from fastapi import APIRouter, Depends
from backend.services.auth import get_current_user
from backend.schemas.user import User

router = APIRouter()

fake_users_db = {
    "testuser": {
        "username": "testuser",
        "full_name": "Test User",
        "email": "testuser@example.com",
        "password": "newpassword123",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$KEeD8Pa1nYXHiePDPzVmpA$42/yf4JLPCgIspZiqA3Ip49n8J7uNVrc7bJJpImKoq0",
        "disabled": False,
    }
}


@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(lambda: get_current_user(db=fake_users_db))):
    return current_user
