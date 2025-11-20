"""Tournament tabulation operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import BaseClient


class RoundResource:
    """Operations for a specific round within a tournament."""

    def __init__(self, client: "BaseClient", tourn_id: int, round_id: int):
        self._client = client
        self._tourn_id = tourn_id
        self._round_id = round_id

    def get_dashboard(self) -> dict[str, Any]:
        """
        Get event by event status for the tournament dashboard.

        GET /tab/{tournId}/round/{roundId}/dashboard

        Returns:
            Dashboard data for the round
        """
        return self._client.get(
            f"/tab/{self._tourn_id}/round/{self._round_id}/dashboard"
        )

    def get_attendance(self) -> dict[str, Any]:
        """
        Get room attendance and start status of the round.

        GET /tab/{tournId}/round/{roundId}/attendance

        Returns:
            Attendance data for the round
        """
        return self._client.get(
            f"/tab/{self._tourn_id}/round/{self._round_id}/attendance"
        )

    def mark_attendance(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Mark or unmark a member of a room as present.

        POST /tab/{tournId}/round/{roundId}/attendance

        Args:
            data: Attendance data

        Returns:
            Updated attendance data
        """
        return self._client.post(
            f"/tab/{self._tourn_id}/round/{self._round_id}/attendance", json=data
        )


class TimeslotResource:
    """Operations for a specific timeslot within a tournament."""

    def __init__(self, client: "BaseClient", tourn_id: int, timeslot_id: int):
        self._client = client
        self._tourn_id = tourn_id
        self._timeslot_id = timeslot_id

    def get_dashboard(self) -> dict[str, Any]:
        """
        Get event by event status for the tournament dashboard.

        GET /tab/{tournId}/timeslot/{timeslotId}/dashboard

        Returns:
            Dashboard data for the timeslot
        """
        return self._client.get(
            f"/tab/{self._tourn_id}/timeslot/{self._timeslot_id}/dashboard"
        )

    def get_attendance(self) -> dict[str, Any]:
        """
        Get room attendance and start status of the timeslot.

        GET /tab/{tournId}/timeslot/{timeslotId}/attendance

        Returns:
            Attendance data for the timeslot
        """
        return self._client.get(
            f"/tab/{self._tourn_id}/timeslot/{self._timeslot_id}/attendance"
        )

    def mark_attendance(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Mark or unmark a member of a room as present.

        POST /tab/{tournId}/timeslot/{timeslotId}/attendance

        Args:
            data: Attendance data

        Returns:
            Updated attendance data
        """
        return self._client.post(
            f"/tab/{self._tourn_id}/timeslot/{self._timeslot_id}/attendance", json=data
        )


class TournamentTabResource:
    """Tab operations for a specific tournament."""

    def __init__(self, client: "BaseClient", tourn_id: int):
        self._client = client
        self._tourn_id = tourn_id

    def round(self, round_id: int) -> RoundResource:
        """
        Access operations for a specific round.

        Args:
            round_id: The round ID

        Returns:
            RoundResource for the specified round
        """
        return RoundResource(self._client, self._tourn_id, round_id)

    def timeslot(self, timeslot_id: int) -> TimeslotResource:
        """
        Access operations for a specific timeslot.

        Args:
            timeslot_id: The timeslot ID

        Returns:
            TimeslotResource for the specified timeslot
        """
        return TimeslotResource(self._client, self._tourn_id, timeslot_id)

    def get_dashboard(self) -> dict[str, Any]:
        """
        Get event by event status for the entire tournament dashboard.

        GET /tab/{tournId}/all/dashboard

        Returns:
            Dashboard data for the tournament
        """
        return self._client.get(f"/tab/{self._tourn_id}/all/dashboard")

    def get_attendance(self) -> dict[str, Any]:
        """
        Get room attendance and start status for the tournament.

        GET /tab/{tournId}/all/attendance

        Returns:
            Attendance data for the tournament
        """
        return self._client.get(f"/tab/{self._tourn_id}/all/attendance")

    def mark_attendance(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Mark or unmark a member of a room as present.

        POST /tab/{tournId}/all/attendance

        Args:
            data: Attendance data

        Returns:
            Updated attendance data
        """
        return self._client.post(f"/tab/{self._tourn_id}/all/attendance", json=data)

    def get_category_checkin(self, category_id: int) -> dict[str, Any]:
        """
        Get judge checkin status for a category.

        GET /tab/{tournId}/all/category/{categoryId}/checkin

        Args:
            category_id: The category ID

        Returns:
            Judge checkin data showing who is present or absent
        """
        return self._client.get(
            f"/tab/{self._tourn_id}/all/category/{category_id}/checkin"
        )


class TabResource:
    """Tournament tabulation operations."""

    def __init__(self, client: "BaseClient"):
        self._client = client

    def tournament(self, tourn_id: int) -> TournamentTabResource:
        """
        Access tab operations for a specific tournament.

        Args:
            tourn_id: The tournament ID

        Returns:
            TournamentTabResource for the specified tournament
        """
        return TournamentTabResource(self._client, tourn_id)
