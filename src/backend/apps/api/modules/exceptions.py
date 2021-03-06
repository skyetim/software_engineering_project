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


class DateFormatError(BackendBaseException):
    CODE = 9


class VisibilityError(BackendBaseException):
    CODE = 10


class TravelDoesNotExistException(BackendBaseException):
    CODE = 11


class TravelGroupDoesNotExistException(BackendBaseException):
    CODE = 12


class TravelGroupOwnershipMismatch(BackendBaseException):
    CODE = 13


class TravelAlreadyExistsInTravelGroup(BackendBaseException):
    CODE = 14


class TravelDoesNotExistInTravelGroup(BackendBaseException):
    CODE = 15


class TravelAlreadyExistsException(BackendBaseException):
    CODE = 16


class DateStartLaterThanDateEndError(BackendBaseException):
    CODE = 17


class TravelDoesNotBelongToTravelGroup(BackendBaseException):
    CODE = 18


class TravelAssociationAlreadyExist(BackendBaseException):
    CODE = 19


class TravelAssociationDoesNotExist(BackendBaseException):
    CODE = 20


class IllegalPswdHashFormat(BackendBaseException):
    CODE = 21


class FriendAlreadyExistsException(BackendBaseException):
    CODE = 22


class UserSessionTimeoutException(BackendBaseException):
    CODE = 23


class PermissionDeniedException(BackendBaseException):
    CODE = 24


class MsgTypeError(BackendBaseException):
    CODE = 25


class MessageDoesNotExistException(BackendBaseException):
    CODE = 26
