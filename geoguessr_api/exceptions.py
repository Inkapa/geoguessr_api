class GeoguessrException(Exception):
    """
    Base exception for this library.
    """

    def __init__(self, code, url, message):
        self.code = code
        self.url = url
        self.message = message

    def __str__(self):
        return self.message


class Forbidden(GeoguessrException):
    """Raised if your login details are invalid."""


class NotFound(GeoguessrException):
    """Raised if a ressource such as a user can't be found."""


class BadRequest(GeoguessrException):
    """
    Raised when sending an invalid request such as a friend request to
    a user who already has a pending friend request.
    """