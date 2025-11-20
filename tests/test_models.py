"""Tests for Pydantic models."""

from datetime import datetime
from tabroom.models import Person, Session, Invite, Search, Err


def test_session_model():
    """Test Session model validation."""
    session = Session(person_id=123, name="John Doe")
    assert session.person_id == 123
    assert session.name == "John Doe"


def test_err_model():
    """Test Err model validation."""
    error = Err(message="Something went wrong")
    assert error.message == "Something went wrong"


def test_invite_model_extra_fields():
    """Test that Invite model allows extra fields."""
    invite = Invite(
        name="Tournament Name",
        extra_field="This should be allowed"
    )
    assert invite.name == "Tournament Name"


def test_search_model():
    """Test Search model validation."""
    search = Search(result="Tournament 1")
    assert search.result == "Tournament 1"


def test_person_model():
    """Test Person model with nullable fields."""
    # Minimal person (only required field is password)
    person = Person(id=1, password="secret")
    assert person.id == 1
    assert person.email is None
    assert person.first is None

    # Full person
    person_full = Person(
        id=1,
        email="test@example.com",
        first="John",
        last="Doe",
        password="secret",
        no_email=False,
        site_admin=True
    )
    assert person_full.email == "test@example.com"
    assert person_full.first == "John"
    assert person_full.site_admin is True


def test_person_datetime_parsing():
    """Test that Person model parses datetime strings correctly."""
    person = Person(
        id=1,
        password="secret",
        last_access="2024-01-15 10:30:00",
        timestamp="2024-01-20 15:45:30"
    )

    assert isinstance(person.last_access, datetime)
    assert person.last_access.year == 2024
    assert person.last_access.month == 1
    assert person.last_access.day == 15
