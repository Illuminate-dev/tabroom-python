"""Collection of extra operations not in API spec"""

from typing import TYPE_CHECKING, Any, Dict, List

from bs4 import BeautifulSoup

from tabroom.types import DebateEvent

if TYPE_CHECKING:
    from ..client import BaseClient


class ExtraResource:
    """System status operations."""

    def __init__(self, client: "BaseClient"):
        self._client = client

    def get_bids(self, event: DebateEvent, year: str = "2025") -> List[Dict[str, Any]]:
        """
        Get list of entrys with bids in a specific event.

        Scrapes HTML of https://www.tabroom.com/index/results/toc_bids.mhtml.

        Args:
            event: the event to get bids for
            year: the school year starting to get bids for

        Returns:
            List of bids
        """

        form_data = {"code": event.value.id, "year": year}

        html = self._client.request_html(
            "/index/results/toc_bids.mhtml", "POST", data=form_data
        )

        if html is None:
            return []

        soup = BeautifulSoup(html, "html.parser")

        table = soup.find(id=str(event.value.id))
        policy_teams = []

        for row in table.tbody.find_all("tr"):
            school = (
                row.contents[1].get_text().replace("\\t", "").replace("\\n", "").strip()
            )
            state = (
                row.contents[3].get_text().replace("\\t", "").replace("\\n", "").strip()
            )
            entry = (
                row.contents[5].get_text().replace("\\t", "").replace("\\n", "").strip()
            )
            bids = (
                row.contents[7].get_text().replace("\\t", "").replace("\\n", "").strip()
            )
            policy_teams.append(
                {"school": school, "state": state, "entry": entry, "bids": bids}
            )

        return policy_teams
