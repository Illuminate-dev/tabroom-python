"""
Tabroom API Client

A Python client library for the Tabroom.com API with type-safe models and organized resources.
"""

from .client import BaseClient
from .exceptions import (
    TabroomAPIError,
    TabroomAuthError,
    TabroomError,
    TabroomNotFoundError,
    TabroomServerError,
    TabroomValidationError,
)
from .models import (
    Ad,
    CaselistLink,
    Chapter,
    Err,
    Event,
    Invite,
    LoginRequest,
    Person,
    Round,
    School,
    SchoolSetting,
    Search,
    Session,
    Share,
    Student,
)
from .resources import (
    AccessResource,
    CaselistResource,
    NsdaResource,
    PaymentResource,
    PublicResource,
    ShareResource,
    SystemResource,
    TabResource,
    UserResource,
)


class TabroomClient:
    """
    Main client for interacting with the Tabroom API.

    Example:
        >>> client = TabroomClient(username="user@example.com", password="password")
        >>> profile = client.user.get_profile()
        >>> tournaments = client.public.search_tournaments("future", "TOC")
        >>> dashboard = client.tab.tournament(123).get_dashboard()
    """

    def __init__(
        self,
        base_url: str = "https://api.tabroom.com/v1",
        username: str | None = None,
        password: str | None = None,
        timeout: float = 30.0,
    ):
        """
        Initialize the Tabroom API client.

        Args:
            base_url: Base URL for the API (default: https://api.tabroom.com/v1)
            username: Username for basic HTTP authentication
            password: Password for basic HTTP authentication
            timeout: Request timeout in seconds (default: 30.0)
        """
        self._base_client = BaseClient(
            base_url=base_url,
            username=username,
            password=password,
            timeout=timeout,
        )

        # Initialize resources lazily
        self._user_resource: UserResource | None = None
        self._public_resource: PublicResource | None = None
        self._tab_resource: TabResource | None = None
        self._access_resource: AccessResource | None = None
        self._caselist_resource: CaselistResource | None = None
        self._nsda_resource: NsdaResource | None = None
        self._share_resource: ShareResource | None = None
        self._payment_resource: PaymentResource | None = None
        self._system_resource: SystemResource | None = None

    @property
    def user(self) -> UserResource:
        """Access user profile operations."""
        if self._user_resource is None:
            self._user_resource = UserResource(self._base_client)
        return self._user_resource

    @property
    def public(self) -> PublicResource:
        """Access public tournament search and listing operations."""
        if self._public_resource is None:
            self._public_resource = PublicResource(self._base_client)
        return self._public_resource

    @property
    def tab(self) -> TabResource:
        """Access tournament tabulation operations."""
        if self._tab_resource is None:
            self._tab_resource = TabResource(self._base_client)
        return self._tab_resource

    @property
    def access(self) -> AccessResource:
        """Access permission and access control operations."""
        if self._access_resource is None:
            self._access_resource = AccessResource(self._base_client)
        return self._access_resource

    @property
    def caselist(self) -> CaselistResource:
        """Access caselist integration operations."""
        if self._caselist_resource is None:
            self._caselist_resource = CaselistResource(self._base_client)
        return self._caselist_resource

    @property
    def nsda(self) -> NsdaResource:
        """Access NSDA integration operations."""
        if self._nsda_resource is None:
            self._nsda_resource = NsdaResource(self._base_client)
        return self._nsda_resource

    @property
    def share(self) -> ShareResource:
        """Access document sharing operations."""
        if self._share_resource is None:
            self._share_resource = ShareResource(self._base_client)
        return self._share_resource

    @property
    def payment(self) -> PaymentResource:
        """Access payment processing operations."""
        if self._payment_resource is None:
            self._payment_resource = PaymentResource(self._base_client)
        return self._payment_resource

    @property
    def system(self) -> SystemResource:
        """Access system status operations."""
        if self._system_resource is None:
            self._system_resource = SystemResource(self._base_client)
        return self._system_resource

    def close(self) -> None:
        """Close the HTTP client connection."""
        self._base_client.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


__version__ = "0.1.0"

__all__ = [
    # Main client
    "TabroomClient",
    # Exceptions
    "TabroomError",
    "TabroomAuthError",
    "TabroomNotFoundError",
    "TabroomValidationError",
    "TabroomServerError",
    "TabroomAPIError",
    # Models
    "Person",
    "Session",
    "LoginRequest",
    "School",
    "SchoolSetting",
    "Chapter",
    "Event",
    "Round",
    "Invite",
    "Ad",
    "Search",
    "Student",
    "CaselistLink",
    "Share",
    "Err",
    # Resources (for advanced usage)
    "UserResource",
    "PublicResource",
    "TabResource",
    "AccessResource",
    "CaselistResource",
    "NsdaResource",
    "ShareResource",
    "PaymentResource",
    "SystemResource",
]
