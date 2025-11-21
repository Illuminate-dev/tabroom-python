"""Caselist related models."""

from pydantic import BaseModel


class Student(BaseModel):
    """Student model."""

    id: int
    name: str | None = None
    # Add other fields as needed


class CaselistLink(BaseModel):
    """Link to a caselist page."""

    url: str | None = None
    # Add other fields as needed
