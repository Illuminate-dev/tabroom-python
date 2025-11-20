"""User and person related models."""

from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .common import TabroomDateTime


class Person(BaseModel):
    """Person model representing a user."""

    model_config = ConfigDict(populate_by_name=True)  # Allow both 'pass_timestamp' and 'pass_timstamp'

    id: int
    email: str | None = None
    first: str | None = None
    middle: str | None = None
    last: str | None = None
    street: str | None = None
    city: str | None = None
    state: str | None = None
    zip: str | None = None
    postal: str | None = None
    country: str | None = None
    tz: str | None = None
    nsda: int | None = None
    phone: int | None = None
    gender: str | None = None
    pronoun: str | None = None
    password: str
    no_email: bool = False
    site_admin: bool | None = None
    accesess: int | None = None  # Note: typo in API schema
    last_access: datetime | None = None
    pass_timestamp: Annotated[
        datetime | None, Field(alias="pass_timstamp")
    ] = None  # Note: typo in API schema
    timestamp: datetime | None = None

    @field_validator("last_access", "pass_timestamp", "timestamp", mode="before")
    @classmethod
    def parse_datetime(cls, value: str | None) -> datetime | None:
        """Parse Tabroom datetime format."""
        return TabroomDateTime.parse_tabroom_datetime(value)
