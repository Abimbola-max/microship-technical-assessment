from pymongo import MongoClient

from src.data.model.user import User
from src.data.repository.userinterface import UserInterface


class UserRepository(UserInterface):

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['User_Authentication']
        self.collection = self.database['users']

    def save_user(self, user: User):
        user_data = {
            "name": user.name,
            "email": user.email,
            "password": user.password
        }
        insert_result = self.collection.insert_one(user_data)
        user.user_data = str(insert_result.inserted_id)
        return user

    def exists_by_email(self,  email: str) -> bool:
        return self.collection.find_one({"email": email}) is not None