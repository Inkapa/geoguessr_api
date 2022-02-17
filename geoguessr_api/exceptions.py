class GeoguessrException(Exception):
    """
    Base exception for this library.
    """
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return self.message


class Forbidden(GeoguessrException):
    """Raised if your login details are invalid."""

    def __init__(self, code, url, message):
        self.code = code
        self.url = url
        self.message = message
        super().__init__(self.code, self.message)
