#/dependencies/memgraph_connector.py
from passlib.context import CryptContext
from ..models import User

class DbConnector():
    def __init__(self):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        # Mock database
        self.db = {
            "user": {
                "username": "user",
                "password": str(pwd_context.hash("123"))
            }
        }

    async def get_user(self, username: str):
        if username in self.db:
            user_dict = self.db[username]
            user = User(**user_dict)
            return user