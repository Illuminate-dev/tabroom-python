"""Tournament related models."""

from typing import Any

from pydantic import BaseModel, ConfigDict


class Event(BaseModel):
    """Tournament event model."""

    id: int
    name: str | None = None
    # Add other fields as needed


class Round(BaseModel):
    """Tournament round model."""

    id: int
    name: str | None = None
    # Add other fields as needed


class Invite(BaseModel):
    """Tournament invite model.

    Note: API docs say this often contains additional data beyond just 'name'.
    """

    model_config = ConfigDict(extra="allow")  # Allow additional fields not defined in schema

    name: str | None = None


class Ad(BaseModel):
    """Advertisement model."""

    id: int | None = None
    content: str | None = None
    # Add other fields as needed


class Search(BaseModel):
    """Search result model."""

    result: str | None = None
