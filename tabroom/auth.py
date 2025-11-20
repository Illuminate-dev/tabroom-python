"""Authentication utilities for Tabroom API."""

import base64


class BasicAuth:
    """Basic HTTP authentication handler."""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get_auth_header(self) -> str:
        """Generate the Authorization header value for basic auth."""
        credentials = f"{self.username}:{self.password}"
        encoded = base64.b64encode(credentials.encode()).decode()
        return f"Basic {encoded}"

    def get_headers(self) -> dict[str, str]:
        """Get headers dict with authentication."""
        return {"Authorization": self.get_auth_header()}
