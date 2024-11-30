from datetime import datetime, timedelta
from jose import jwt, JWTError
from argon2 import PasswordHasher
from backend.config import SECRET_KEY, ALGORITHM

ph = PasswordHasher()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica si la contraseña proporcionada coincide con el hash almacenado."""
    try:
        return ph.verify(hashed_password, plain_password)
    except Exception:
        return False


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Genera un token JWT."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    """Decodifica y valida un token JWT."""
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None
