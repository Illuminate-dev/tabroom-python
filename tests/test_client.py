"""Basic tests for the Tabroom client."""

import pytest
from tabroom import TabroomClient
from tabroom.exceptions import TabroomError


def test_client_initialization():
    """Test that the client initializes correctly."""
    client = TabroomClient(
        username="test@example.com",
        password="test_password"
    )

    assert client is not None
    assert client._base_client.base_url == "https://api.tabroom.com/v1"
    client.close()


def test_client_custom_base_url():
    """Test client with custom base URL."""
    custom_url = "https://custom.api.com/v1"
    client = TabroomClient(
        base_url=custom_url,
        username="test@example.com",
        password="test_password"
    )

    assert client._base_client.base_url == custom_url
    client.close()


def test_client_context_manager():
    """Test that client works as context manager."""
    with TabroomClient(username="test", password="test") as client:
        assert client is not None


def test_resource_lazy_loading():
    """Test that resources are loaded lazily."""
    client = TabroomClient(username="test", password="test")

    # Resources should be None initially
    assert client._user_resource is None
    assert client._public_resource is None

    # Accessing should create them
    user_resource = client.user
    assert client._user_resource is not None
    assert user_resource is client.user  # Should return same instance

    client.close()


def test_all_resources_accessible():
    """Test that all resource properties are accessible."""
    client = TabroomClient(username="test", password="test")

    # Just test that we can access all resource properties
    assert client.user is not None
    assert client.public is not None
    assert client.tab is not None
    assert client.access is not None
    assert client.caselist is not None
    assert client.nsda is not None
    assert client.share is not None
    assert client.payment is not None
    assert client.system is not None

    client.close()
