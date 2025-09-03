from app.repositories.users import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_payload):
        return self.user_repository.insert(user_payload)

    async def authenticate_user(self, username: str, password: str):
        return self.user_repository.get_by_username_or_email(username, password)



