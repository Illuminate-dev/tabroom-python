"""Caselist integration operations."""

from typing import TYPE_CHECKING, Any

from ..models import CaselistLink, Chapter, Student

if TYPE_CHECKING:
    from ..client import BaseClient


class CaselistResource:
    """Caselist integration operations."""

    def __init__(self, client: "BaseClient"):
        self._client = client

    def get_students(self, person_id: int) -> list[Student]:
        """
        Load students for a person ID.

        GET /ext/caselist/students

        Args:
            person_id: The person ID

        Returns:
            List of students
        """
        return self._client.get(
            "/ext/caselist/students",
            params={"person_id": person_id},
            response_model=Student,
        )

    def get_rounds(self, person_id: int) -> list[dict[str, Any]]:
        """
        Load rounds for a person ID.

        GET /ext/caselist/rounds

        Args:
            person_id: The person ID

        Returns:
            List of rounds
        """
        return self._client.get(
            "/ext/caselist/rounds", params={"person_id": person_id}
        )

    def create_link(self, data: dict[str, Any]) -> CaselistLink:
        """
        Create a link to a caselist page.

        POST /ext/caselist/link

        Args:
            data: Link data

        Returns:
            Created caselist link
        """
        return self._client.post(
            "/ext/caselist/link", json=data, response_model=CaselistLink
        )

    def get_chapters(self, person_id: int) -> list[Chapter]:
        """
        Load chapters for a person ID.

        GET /ext/caselist/chapters

        Args:
            person_id: The person ID

        Returns:
            List of chapters
        """
        return self._client.get(
            "/ext/caselist/chapters",
            params={"person_id": person_id},
            response_model=Chapter,
        )
