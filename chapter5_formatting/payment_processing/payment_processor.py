from decimal import Decimal
from datetime import datetime
from typing import Dict
from exceptions import PaymentError
from payment_models import PaymentOutcome, PaymentEntry, PaymentOrder
from payment_services import LogWriter, MessageService
from payment_validator import PaymentRequestValidator

PAYMENT_LIMIT = Decimal("5000")
TIMESTAMP_MULTIPLIER = 1000
INITIAL_ATTEMPT = 0

class PaymentHandler:
    """Payment handler for processing payment transactions."""
    
    MAX_RETRIES = 2
    PAYMENT_SUCCESS = "Payment successful"
    PAYMENT_FAILED = "Payment failed"

    def __init__(self, logger: LogWriter, notifier: MessageService, validator: PaymentRequestValidator = None) -> None:
        """Initialize the payment handler."""
        self.logger = logger
        self.notifier = notifier
        self.validator = validator if validator else PaymentRequestValidator()
        self.history: Dict[str, PaymentEntry] = {}

    def handle_payment(self, request: PaymentOrder) -> PaymentOutcome:
        """Handles a payment request."""
        self.validator.validate(request)
        
        attempt = INITIAL_ATTEMPT
        while attempt < self.MAX_RETRIES:
            try:
                transaction_id = self._create_transaction_id()
                self._run_payment(request)
                self._store_record(request, transaction_id)
                self._send_success_notification(request)
                return PaymentOutcome(True, self.PAYMENT_SUCCESS, transaction_id)
            except PaymentError:
                attempt += 1
                self.logger.write_log(f"Retry attempt: {attempt}")
        
        return PaymentOutcome(False, self.PAYMENT_FAILED, None)

    def _run_payment(self, request: PaymentOrder) -> None:
        """Runs the payment."""
        self.logger.write_log(f"Executing payment of {request.order_amount}")
        
        if request.order_amount > PAYMENT_LIMIT:
            raise PaymentError("Limit exceeded")

    def _store_record(self, request: PaymentOrder, transaction_id: str) -> None:
        """Stores the payment in history."""
        self.history[transaction_id] = PaymentEntry(
            request.customer_id,
            request.order_amount,
            datetime.now()
        )

    def _send_success_notification(self, request: PaymentOrder) -> None:
        """Sends success notification to customer."""
        self.notifier.dispatch(request.customer_id, f"Payment of {request.order_amount} processed")

    def _create_transaction_id(self) -> str:
        """Creates a unique transaction ID."""
        return f"TXN-{int(datetime.now().timestamp() * TIMESTAMP_MULTIPLIER)}"
