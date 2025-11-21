"""User profile operations."""

from typing import TYPE_CHECKING

from ..models import Person

if TYPE_CHECKING:
    from ..client import BaseClient


class UserResource:
    """User profile operations."""

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
