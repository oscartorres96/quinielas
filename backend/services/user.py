from backend.schemas.user import UserInDB


def get_user(db: dict, username: str) -> UserInDB | None:
    """Obtiene un usuario de la base de datos simulada."""
    user = db.get(username)
    return UserInDB(**user) if user else None