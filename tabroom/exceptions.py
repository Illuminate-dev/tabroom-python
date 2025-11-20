"""Custom exceptions for the Tabroom API client."""


class TabroomError(Exception):
    """Base exception for all Tabroom API errors."""

    def __init__(self, message: str, status_code: int | None = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class TabroomAuthError(TabroomError):
    """Raised when authentication fails."""

    pass


class TabroomNotFoundError(TabroomError):
    """Raised when a resource is not found (404)."""

    pass


class TabroomValidationError(TabroomError):
    """Raised when request validation fails (422)."""

    pass


class TabroomServerError(TabroomError):
    """Raised when the server returns a 5xx error."""

    pass


class TabroomAPIError(TabroomError):
    """Raised for other API errors."""

    pass
