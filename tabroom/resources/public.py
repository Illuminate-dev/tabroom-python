"""Public tournament search and listing operations."""

from typing import TYPE_CHECKING, Any

from ..models import Ad, Invite, Search

if TYPE_CHECKING:
    from ..client import BaseClient


class PublicResource:
    """Public tournament search and listing operations."""

    def __init__(self, client: "BaseClient"):
        self._client = client

    def search_tournaments(
        self, time: str, search_string: str, circuit_id: int | None = None
    ) -> list[Search]:
        """
        Search for non-hidden tournaments by name.

        GET /public/search/{time}/{searchString}/circuit/{circuitId}
        GET /public/search/{time}/{searchString}

        Args:
            time: Time filter - 'past', 'future', or 'both'
            search_string: Search query
            circuit_id: Optional circuit ID to filter by

        Returns:
            List of search results
        """
        if circuit_id:
            path = f"/public/search/{time}/{search_string}/circuit/{circuit_id}"
        else:
            path = f"/public/search/{time}/{search_string}"

        return self._client.get(path, response_model=Search)

    def get_upcoming_tournaments(self, circuit: int | None = None) -> list[Invite]:
        """
        Get the public listing of upcoming tournaments.

        GET /public/invite/upcoming/{circuit}
        GET /public/invite/upcoming

        Args:
            circuit: Optional circuit ID to filter by

        Returns:
            List of tournament invites
        """
        if circuit:
            path = f"/public/invite/upcoming/{circuit}"
        else:
            path = "/public/invite/upcoming"

        return self._client.get(path, response_model=Invite)

    def get_ads(self) -> list[Ad]:
        """
        Get list of ads to display on front page.

        GET /public/ads

        Returns:
            List of advertisements
        """
        return self._client.get("/public/ads", response_model=Ad)

    def get_tournament_by_id(self, tourn_id: int) -> Invite:
        """
        Get the public pages for a tournament by ID.

        GET /public/invite/tourn/{tourn_id}

        Args:
            tourn_id: Tournament ID

        Returns:
            Tournament invite information
        """
        return self._client.get(f"/public/invite/tourn/{tourn_id}", response_model=Invite)

    def get_tournament_by_webname(self, webname: str) -> Invite:
        """
        Get the public pages for a tournament by webname.

        GET /public/invite/{webname}

        Args:
            webname: Tournament webname/slug

        Returns:
            Tournament invite information
        """
        return self._client.get(f"/public/invite/{webname}", response_model=Invite)
