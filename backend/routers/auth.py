from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from backend.services.auth import login_for_access_token
from backend.schemas.token import Token

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


@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    access_token = login_for_access_token(fake_users_db, form_data)
    return {"access_token": access_token, "token_type": "bearer"}
