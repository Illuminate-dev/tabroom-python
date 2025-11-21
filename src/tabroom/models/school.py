"""School and chapter related models."""

from pydantic import BaseModel


class School(BaseModel):
    """School model."""

    id: int
    name: str | None = None
    # Add other fields as needed based on API responses


class SchoolSetting(BaseModel):
    """School settings model."""

    id: int
    # Add fields as needed based on API responses


class Chapter(BaseModel):
    """Chapter model."""

    id: int
    name: str | None = None
    # Add other fields as needed based on API responses
