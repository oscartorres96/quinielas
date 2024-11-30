from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta
from backend.security import verify_password, create_access_token, decode_access_token
from backend.schemas.token import TokenData
from backend.services.user import get_user
from backend.config import ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(db: dict, username: str, password: str):
    """Autentica al usuario verificando el nombre de usuario y la contraseña."""
    user = get_user(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def login_for_access_token(db: dict, form_data, expire_minutes=ACCESS_TOKEN_EXPIRE_MINUTES):
    """Crea un token JWT para un usuario autenticado."""
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        print(f"User not found: {form_data.username}, {form_data.password}")
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    expires = timedelta(minutes=expire_minutes)
    return create_access_token(data={"sub": user.username}, expires_delta=expires)


def get_current_user(token: str = Depends(oauth2_scheme), db=None):
    """Obtiene el usuario actual basado en el token."""
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    username = payload.get("sub")
    user = get_user(db, username)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
