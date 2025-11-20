"""Document sharing related models."""

from pydantic import BaseModel


class Share(BaseModel):
    """Document share model."""

    id: int | None = None
    # Add other fields as needed
