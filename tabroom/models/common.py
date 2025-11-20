"""Common models shared across the API."""

from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field, field_validator


class Err(BaseModel):
    """Error response from the API."""

    message: str


class TabroomDateTime(BaseModel):
    """Helper for parsing Tabroom's datetime format: YYYY-MM-DD HH:MM:SS"""

    @classmethod
    def parse_tabroom_datetime(cls, value: str | None) -> datetime | None:
        """Parse Tabroom's datetime format."""
        if value is None or value == "":
            return None

        # Tabroom format: YYYY-MM-DD HH:MM:SS or YYYY-MM-DD
        try:
            if " " in value:
                return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            else:
                return datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            return None
