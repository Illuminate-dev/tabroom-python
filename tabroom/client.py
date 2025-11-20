"""Base HTTP client for Tabroom API."""

from typing import Any, TypeVar

import httpx
from pydantic import BaseModel, ValidationError

from .auth import BasicAuth
from .exceptions import (
    TabroomAPIError,
    TabroomAuthError,
    TabroomError,
    TabroomNotFoundError,
    TabroomServerError,
    TabroomValidationError,
)
from .models import Err

T = TypeVar("T", bound=BaseModel)


class BaseClient:
    """Base HTTP client with authentication and error handling."""

    def __init__(
        self,
        base_url: str = "https://api.tabroom.com/v1",
        username: str | None = None,
        password: str | None = None,
        timeout: float = 30.0,
    ):
        """
        Initialize the base client.

        Args:
            base_url: Base URL for the API
            username: Username for basic auth
            password: Password for basic auth
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.auth = BasicAuth(username, password) if username and password else None
        self._client = httpx.Client(timeout=timeout)

    def _get_headers(self) -> dict[str, str]:
        """Get headers for requests."""
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if self.auth:
            headers.update(self.auth.get_headers())
        return headers

    def _handle_error(self, response: httpx.Response) -> None:
        """Handle error responses from the API."""
        # Try to parse error message from response
        try:
            error_data = response.json()
            if isinstance(error_data, dict) and "message" in error_data:
                message = error_data["message"]
            else:
                message = response.text or f"HTTP {response.status_code}"
        except Exception:
            message = response.text or f"HTTP {response.status_code}"

        # Raise appropriate exception based on status code
        if response.status_code == 401 or response.status_code == 403:
            raise TabroomAuthError(message, response.status_code)
        elif response.status_code == 404:
            raise TabroomNotFoundError(message, response.status_code)
        elif response.status_code == 422:
            raise TabroomValidationError(message, response.status_code)
        elif response.status_code >= 500:
            raise TabroomServerError(message, response.status_code)
        else:
            raise TabroomAPIError(message, response.status_code)

    def request(
        self,
        method: str,
        path: str,
        response_model: type[T] | None = None,
        **kwargs: Any,
    ) -> T | dict[str, Any] | list[Any] | None:
        """
        Make an HTTP request to the API.

        Args:
            method: HTTP method (GET, POST, etc.)
            path: API endpoint path
            response_model: Pydantic model to parse response into
            **kwargs: Additional arguments to pass to httpx request

        Returns:
            Parsed response data

        Raises:
            TabroomError: On API errors
        """
        url = f"{self.base_url}/{path.lstrip('/')}"
        headers = self._get_headers()

        # Merge custom headers if provided
        if "headers" in kwargs:
            headers.update(kwargs.pop("headers"))

        try:
            response = self._client.request(
                method, url, headers=headers, **kwargs
            )

            # Check for errors
            if not response.is_success:
                self._handle_error(response)

            # Handle empty responses
            if response.status_code == 204 or not response.content:
                return None

            # Parse response
            data = response.json()

            # If response_model provided, validate with Pydantic
            if response_model:
                if isinstance(data, list):
                    return [response_model.model_validate(item) for item in data]
                return response_model.model_validate(data)

            return data

        except httpx.HTTPError as e:
            raise TabroomAPIError(f"HTTP error occurred: {str(e)}")
        except ValidationError as e:
            raise TabroomValidationError(f"Response validation failed: {str(e)}")

    def get(
        self, path: str, response_model: type[T] | None = None, **kwargs: Any
    ) -> T | dict[str, Any] | list[Any] | None:
        """Make a GET request."""
        return self.request("GET", path, response_model=response_model, **kwargs)

    def post(
        self, path: str, response_model: type[T] | None = None, **kwargs: Any
    ) -> T | dict[str, Any] | list[Any] | None:
        """Make a POST request."""
        return self.request("POST", path, response_model=response_model, **kwargs)

    def put(
        self, path: str, response_model: type[T] | None = None, **kwargs: Any
    ) -> T | dict[str, Any] | list[Any] | None:
        """Make a PUT request."""
        return self.request("PUT", path, response_model=response_model, **kwargs)

    def delete(
        self, path: str, response_model: type[T] | None = None, **kwargs: Any
    ) -> T | dict[str, Any] | list[Any] | None:
        """Make a DELETE request."""
        return self.request("DELETE", path, response_model=response_model, **kwargs)

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
