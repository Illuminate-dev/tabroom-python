"""Payment processing operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import BaseClient


class PaymentResource:
    """Payment processing operations."""

    def __init__(self, client: "BaseClient"):
        self._client = client

    def process_paypal(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Record a payment from PayPal.

        POST /user/enter/paypal

        Args:
            data: PayPal payment data

        Returns:
            Payment confirmation
        """
        return self._client.post("/user/enter/paypal", json=data)

    def process_authorize(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Process a payment through Authorize.

        POST /user/enter/authorize

        Args:
            data: Authorize payment data

        Returns:
            Payment confirmation
        """
        return self._client.post("/user/enter/authorize", json=data)
