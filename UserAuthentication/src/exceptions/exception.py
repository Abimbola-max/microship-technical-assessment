class NotFoundException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class EmailAlreadyExistException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class InvalidDetailsException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
