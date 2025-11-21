"""Authentication related models."""

from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    """Request body for login endpoint (not used with basic auth)."""

    email: str
    password: str


class Session(BaseModel):
    """Session object returned from login."""

    person_id: int
    name: str
