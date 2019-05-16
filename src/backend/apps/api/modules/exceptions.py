class BackendBaseException(Exception):
    CODE = 1


class WrongPasswordException(BackendBaseException):
    CODE = 2


class UserDoesNotExistException(BackendBaseException):
    CODE = 3


class UserAlreadyExistsException(BackendBaseException):
    CODE = 4


class UserAuthorizationException(BackendBaseException):
    CODE = 5


class FriendDoesNotExistException(UserDoesNotExistException):
    CODE = 6


class NoCityFoundException(BackendBaseException):
    CODE = 7


class CityIdDoesNotExistException(BackendBaseException):
    CODE = 8
