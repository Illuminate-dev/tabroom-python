"""Base HTTP client for Tabroom API."""

from typing import Any, TypeVar

import requests
from pydantic import BaseModel, ValidationError

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

COOKIE_NAME = "TabroomToken"


class BaseClient:
    """Base HTTP client with cookie-based authentication and error handling."""

    def __init__(
        self,
        api_base_url: str = "https://api.tabroom.com/v1",
        site_base_url: str = "https://www.tabroom.com",
        username: str | None = None,
        password: str | None = None,
        token: str | None = None,
        timeout: float = 30.0,
        auto_login: bool = True,
    ):
        """
        Initialize the base client.

        Args:
            api_base_url: Base URL for API endpoints
            site_base_url: Base URL for the main site
            username: Username for login
            password: Password for login
            token: Optional existing TabroomToken (skips login if provided)
            timeout: Request timeout in seconds
            auto_login: Automatically login if username/password provided
        """
        self.api_base_url = api_base_url.rstrip("/")
        self.site_base_url = site_base_url.rstrip("/")
        self.timeout = timeout
        self.username = username
        self.password = password

        # Session automatically handles cookies
        self._client = requests.Session()

        # Set token if provided
        if token:
            self._client.cookies.set(COOKIE_NAME, token, domain=".tabroom.com")

        # Auto-login if credentials provided and no token
        if auto_login and username and password and not token:
            self.login(username, password)

    def login(self, username: str, password: str) -> None:
        """
        Log in to Tabroom and obtain authentication cookie.

        Args:
            username: Username
            password: Password

        Raises:
            TabroomAuthError: If login fails
        """
        login_url = f"{self.site_base_url}/user/login/login_save.mhtml"

        try:
            response = self._client.post(
                login_url,
                data={"username": username, "password": password},
            )

            # Session automatically stores the cookie - just verify it exists
            if COOKIE_NAME not in self._client.cookies:
                raise TabroomAuthError(
                    "Login failed: No authentication cookie received",
                    response.status_code,
                )

            self.username = username
            self.password = password

        except requests.RequestException as e:
            raise TabroomAuthError(f"Login request failed: {str(e)}")

    def logout(self) -> None:
        """Clear authentication token from session."""
        if COOKIE_NAME in self._client.cookies:
            del self._client.cookies[COOKIE_NAME]

    def is_authenticated(self) -> bool:
        """Check if client has authentication token."""
        return COOKIE_NAME in self._client.cookies

    @property
    def token(self) -> str | None:
        """Get the current authentication token."""
        return self._client.cookies.get(COOKIE_NAME)

    def _get_headers(self) -> dict[str, str]:
        """Get headers for requests."""
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def _handle_error(self, response: requests.Response) -> None:
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
            **kwargs: Additional arguments to pass to requests

        Returns:
            Parsed response data

        Raises:
            TabroomError: On API errors
        """
        url = f"{self.api_base_url}/{path.lstrip('/')}"
        headers = self._get_headers()

        # Merge custom headers if provided
        if "headers" in kwargs:
            headers.update(kwargs.pop("headers"))

        # Set timeout if not provided
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout

        try:
            # Session automatically includes cookies
            response = self._client.request(method, url, headers=headers, **kwargs)

            # Check for errors
            if not response.ok:
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

        except requests.RequestException as e:
            raise TabroomAPIError(f"HTTP error occurred: {str(e)}")
        except ValidationError as e:
            raise TabroomValidationError(f"Response validation failed: {str(e)}")

    def request_html(self, path: str, method: str, **kwargs: Any) -> str | None:
        """Returns html content of a webpath"""
        url = f"{self.site_base_url}/{path.lstrip('/')}"
        headers = self._get_headers()

        if "headers" in kwargs:
            kwargs.update(kwargs.pop("headers"))

        try:
            response = self._client.request(method, url, headers=headers, **kwargs)

            if not response.ok:
                self._handle_error(response)

            if response.status_code == 204 or not response.content:
                return None

            return str(response.content)
        except requests.RequestException as e:
            raise TabroomAPIError(f"HTTP error occured: {str(e)}")

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
