"""Authentication utilities for Tabroom API."""


class CookieAuth:
    """Cookie-based authentication handler for Tabroom."""

    COOKIE_NAME = "TabroomToken"

    def __init__(self, token: str | None = None):
        """
        Initialize cookie auth.

        Args:
            token: Optional existing TabroomToken value
        """
        self.token = token

    def set_token(self, token: str) -> None:
        """Set the authentication token."""
        self.token = token

    def clear_token(self) -> None:
        """Clear the authentication token."""
        self.token = None

    def is_authenticated(self) -> bool:
        """Check if we have an authentication token."""
        return self.token is not None

    def get_cookies(self) -> dict[str, str]:
        """Get cookies dict for requests."""
        if self.token:
            return {self.COOKIE_NAME: self.token}
        return {}
