"""Access control and permissions operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import BaseClient


class EventAccessResource:
    """Access control for a specific event."""

    def __init__(self, client: "BaseClient", tourn_id: int, event_id: int):
        self._client = client
        self._tourn_id = tourn_id
        self._event_id = event_id

    def grant(self, person_id: int, permissions: dict[str, Any]) -> dict[str, Any]:
        """
        Grant or modify event access permissions for a user.

        POST /tab/{tournId}/event/{eventId}/access/{personId}

        Args:
            person_id: The person to grant access to
            permissions: Permission settings

        Returns:
            Updated permissions
        """
        return self._client.post(
            f"/tab/{self._tourn_id}/event/{self._event_id}/access/{person_id}",
            json=permissions,
        )

    def revoke(self, person_id: int) -> None:
        """
        Revoke event access permissions for a user.

        DELETE /tab/{tournId}/event/{eventId}/access/{personId}

        Args:
            person_id: The person to revoke access from
        """
        self._client.delete(
            f"/tab/{self._tourn_id}/event/{self._event_id}/access/{person_id}"
        )


class CategoryAccessResource:
    """Access control for a specific category."""

    def __init__(self, client: "BaseClient", tourn_id: int, category_id: int):
        self._client = client
        self._tourn_id = tourn_id
        self._category_id = category_id

    def grant(self, person_id: int, permissions: dict[str, Any]) -> dict[str, Any]:
        """
        Grant or modify category access permissions for a user.

        POST /tab/{tournId}/category/{categoryId}/access/{personId}

        Args:
            person_id: The person to grant access to
            permissions: Permission settings

        Returns:
            Updated permissions
        """
        return self._client.post(
            f"/tab/{self._tourn_id}/category/{self._category_id}/access/{person_id}",
            json=permissions,
        )

    def revoke(self, person_id: int) -> None:
        """
        Revoke category access permissions for a user.

        DELETE /tab/{tournId}/category/{categoryId}/access/{personId}

        Args:
            person_id: The person to revoke access from
        """
        self._client.delete(
            f"/tab/{self._tourn_id}/category/{self._category_id}/access/{person_id}"
        )


class TournamentAccessResource:
    """Access control for a specific tournament."""

    def __init__(self, client: "BaseClient", tourn_id: int):
        self._client = client
        self._tourn_id = tourn_id

    def grant(self, person_id: int, permissions: dict[str, Any]) -> dict[str, Any]:
        """
        Grant or modify tournament access permissions for a user.

        POST /tab/{tournId}/access/{personId}

        Args:
            person_id: The person to grant access to
            permissions: Permission settings

        Returns:
            Updated permissions
        """
        return self._client.post(
            f"/tab/{self._tourn_id}/access/{person_id}", json=permissions
        )

    def revoke(self, person_id: int) -> None:
        """
        Revoke tournament access permissions for a user.

        DELETE /tab/{tournId}/access/{personId}

        Args:
            person_id: The person to revoke access from
        """
        self._client.delete(f"/tab/{self._tourn_id}/access/{person_id}")

    def event(self, event_id: int) -> EventAccessResource:
        """
        Access event-level permissions.

        Args:
            event_id: The event ID

        Returns:
            EventAccessResource for the specified event
        """
        return EventAccessResource(self._client, self._tourn_id, event_id)

    def category(self, category_id: int) -> CategoryAccessResource:
        """
        Access category-level permissions.

        Args:
            category_id: The category ID

        Returns:
            CategoryAccessResource for the specified category
        """
        return CategoryAccessResource(self._client, self._tourn_id, category_id)


class AccessResource:
    """Access control and permissions operations."""

    def __init__(self, client: "BaseClient"):
        self._client = client

    def tournament(self, tourn_id: int) -> TournamentAccessResource:
        """
        Access permissions for a specific tournament.

        Args:
            tourn_id: The tournament ID

        Returns:
            TournamentAccessResource for the specified tournament
        """
        return TournamentAccessResource(self._client, tourn_id)
