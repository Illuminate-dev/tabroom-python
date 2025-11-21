"""Document sharing operations."""

from typing import TYPE_CHECKING, Any

from ..models import Share

if TYPE_CHECKING:
    from ..client import BaseClient


class ShareResource:
    """Document sharing operations."""

    def __init__(self, client: "BaseClient"):
        self._client = client

    def send_share_file(self, data: dict[str, Any]) -> Share:
        """
        Send a document to the docchain email list for a room.

        POST /ext/share/sendShareFile

        Args:
            data: Share file data including room info and document

        Returns:
            Share response
        """
        return self._client.post(
            "/ext/share/sendShareFile", json=data, response_model=Share
        )
