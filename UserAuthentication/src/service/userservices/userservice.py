from datetime import timedelta

from flask_jwt_extended import create_access_token

from src.data.model.user import User
from src.data.repository.userrespository import UserRepository
from src.exceptions.exception import *
from src.service.passwordsecurity.passwordencrypt import PasswordEncrypt


class UserService:

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register(self, user_reg_request):
        if self.user_repo.exists_by_email(user_reg_request['email']):
            raise EmailAlreadyExistException("A user with this email already exists.")
        hashed_password = PasswordEncrypt.encrypt_password(user_reg_request["password"])
        user = User (
            name = user_reg_request["name"],
            email = user_reg_request["email"],
            password=hashed_password
        )
        saved_user = self.user_repo.save_user(user)
        return saved_user

    def login(self, user_login_request):
        email = user_login_request["email"]
        password = user_login_request['password'].strip()
        name = user_login_request['name']

        user = self.user_repo.find_by_name_or_email(name, email)
        if not user:
            raise NotFoundException("User not found")
        hashed_password = user.password

        if not PasswordEncrypt.verify_password(password, hashed_password):
            raise InvalidDetailsException("Invalid details.")
        access_token = create_access_token(
            identity=str(user.email),
            expires_delta=timedelta(hours=1)
        )
        return access_token