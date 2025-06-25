from abc import ABC, abstractmethod

from src.data.model.user import User


class UserInterface(ABC):

    @abstractmethod
    def save_user(self, user: User):
        pass

    @abstractmethod
    def exists_by_email(self,  email: str) -> bool:
        pass

