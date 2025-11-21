"""NSDA integration operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import BaseClient


class NsdaResource:
    """NSDA integration operations."""

    def __init__(self, client: "BaseClient"):
        self._client = client

    def get_history(self, nsda_id: int) -> dict[str, Any]:
        """
        Load history for a NSDA membership ID.

        GET /ext/nsda/history

        Args:
            nsda_id: NSDA membership ID

        Returns:
            NSDA history data
        """
        return self._client.get("/ext/nsda/history", params={"nsda_id": nsda_id})
