"""System status operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import BaseClient


class SystemResource:
    """System status operations."""

    def __init__(self, client: "BaseClient"):
        self._client = client

    def get_status(self) -> dict[str, Any]:
        """
        Check system status.

        GET /status

        Returns:
            System status data with 200 status code if up
        """
        return self._client.get("/status")

    def post_status(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Check system status via POST.

        POST /status

        Args:
            data: Optional data to send

        Returns:
            System status data with 200 status code if up
        """
        return self._client.post("/status", json=data or {})
