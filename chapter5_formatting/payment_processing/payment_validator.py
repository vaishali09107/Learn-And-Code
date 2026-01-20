from decimal import Decimal

MIN_AMOUNT = Decimal("0.01")


class PaymentRequestValidator:
    """Validator for payment requests."""

    def validate(self, request) -> None:
        """Validates the payment request."""
        self._validate_customer_id(request)
        self._validate_order_amount(request)

    def _validate_customer_id(self, request) -> None:
        """Validates the customer ID."""
        is_customer_id_missing = not request.customer_id
        is_customer_id_empty = not request.customer_id.strip() if request.customer_id else True
        if is_customer_id_missing or is_customer_id_empty:
            raise ValueError("Customer ID required")

    def _validate_order_amount(self, request) -> None:
        """Validates the order amount."""
        is_order_amount_missing = not request.order_amount
        is_order_amount_below_minimum = request.order_amount < MIN_AMOUNT if request.order_amount else True
        if is_order_amount_missing or is_order_amount_below_minimum:
            raise ValueError("Invalid amount")
