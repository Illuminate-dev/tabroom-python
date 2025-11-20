"""User profile operations."""

from typing import TYPE_CHECKING

from ..models import Person, Session

if TYPE_CHECKING:
    from ..client import BaseClient


class UserResource:
    """User profile and authentication operations."""

    def __init__(self, client: "BaseClient"):
        self._client = client

    def get_profile(self) -> Person:
        """
        Load the profile data of the logged in user.

        GET /user/profile

        Returns:
            Person: The user's profile information
        """
        return self._client.get("/user/profile", response_model=Person)

    def get_profile_by_id(self, person_id: int) -> Person:
        """
        Load the profile data of a specific user.

        GET /user/profile/{personId}

        Args:
            person_id: The ID of the person to retrieve

        Returns:
            Person: The person's profile information
        """
        return self._client.get(f"/user/profile/{person_id}", response_model=Person)

    def login(self, email: str, password: str) -> Session:
        """
        Log in and return a session object.

        POST /login

        Note: This is typically not used with basic auth configuration.

        Args:
            email: User's email
            password: User's password

        Returns:
            Session: Session information
        """
        return self._client.post(
            "/login", json={"email": email, "password": password}, response_model=Session
        )
