from decimal import Decimal
from datetime import datetime
from typing import Dict
from exceptions import PaymentError
from payment_models import PaymentOutcome, PaymentEntry, PaymentOrder
from payment_services import LogWriter, MessageService

PAYMENT_LIMIT = Decimal("5000")
TIMESTAMP_MULTIPLIER = 1000
INITIAL_ATTEMPT = 0

class PaymentHandler:
    """Payment handler for processing payment transactions."""
    
    MIN_AMOUNT = Decimal("0.01")
    MAX_RETRIES = 2
    PAYMENT_SUCCESS = "Payment successful"
    PAYMENT_FAILED = "Payment failed"

    def __init__(self, logger: LogWriter, notifier: MessageService) -> None:
        """Initialize the payment handler."""
        self.logger = logger
        self.notifier = notifier
        self.history: Dict[str, PaymentEntry] = {}

    def handle_payment(self, request: PaymentOrder) -> PaymentOutcome:
        """Handles a payment request."""
        self._verify_request(request)
        
        attempt = INITIAL_ATTEMPT
        while attempt < self.MAX_RETRIES:
            try:
                self._run_payment(request)
                self._store_record(request)
                self._send_success_notification(request)
                return PaymentOutcome(True, self.PAYMENT_SUCCESS, self._create_transaction_id())
            except PaymentError:
                attempt += 1
                self.logger.write_log(f"Retry attempt: {attempt}")
        
        return PaymentOutcome(False, self.PAYMENT_FAILED, None)

    def _verify_request(self, request: PaymentOrder) -> None:
        """Verifies the payment request."""
        is_customer_id_missing = not request.customer_id
        is_customer_id_empty = not request.customer_id.strip() if request.customer_id else True
        if is_customer_id_missing or is_customer_id_empty:
            raise ValueError("Customer ID required")
        
        is_amount_missing = not request.amount
        is_amount_below_minimum = request.amount < self.MIN_AMOUNT if request.amount else True
        if is_amount_missing or is_amount_below_minimum:
            raise ValueError("Invalid amount")

    def _run_payment(self, request: PaymentOrder) -> None:
        """Runs the payment."""
        self.logger.write_log(f"Executing payment of {request.amount}")
        
        if request.amount > PAYMENT_LIMIT:
            raise PaymentError("Limit exceeded")

    def _store_record(self, request: PaymentOrder) -> None:
        """Stores the payment in history."""
        self.history[self._create_transaction_id()] = PaymentEntry(
            request.customer_id,
            request.amount,
            datetime.now()
        )

    def _send_success_notification(self, request: PaymentOrder) -> None:
        """Sends success notification to customer."""
        self.notifier.dispatch(request.customer_id, f"Payment of {request.amount} processed")

    def _create_transaction_id(self) -> str:
        """Creates a unique transaction ID."""
        return f"TXN-{int(datetime.now().timestamp() * TIMESTAMP_MULTIPLIER)}"
