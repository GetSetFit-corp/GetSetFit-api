from fastapi import HTTPException

from app.utils.auth import verify_password
from app.models.user import User as UserModel


class UserRepository:
    def __init__(self, db_client):
        self.db_client = db_client

    def insert(self, user: UserModel) -> UserModel:
        self.db_client.add(user)
        self.db_client.commit()
        self.db_client.refresh(
            user
        )  # reloads auto-generated values (id, timestamps, etc.)
        return user

    def get_by_username_or_email(self, email: str, password: str) -> UserModel:
        user = self.db_client.query(UserModel).filter(UserModel.email == email).first()
        is_correct_password_ = verify_password(password, user.hashed_password)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            if is_correct_password_:
                return user
            else:
                raise HTTPException(status_code=404, detail="User name or password is incorrect")

    def get_by_user_id(self, user_id:int):
        user = self.db_client.query(UserModel).filter(UserModel.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            return user