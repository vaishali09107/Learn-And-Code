from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional

@dataclass
class PaymentOrder:
    """Represents a payment order."""
    customer_id: str
    order_amount: Decimal

@dataclass
class PaymentOutcome:
    """Represents the outcome of a payment operation."""
    success: bool
    message: str
    transaction_id: Optional[str]

@dataclass
class PaymentEntry:
    """Represents an entry of a completed payment."""
    customer_id: str
    order_amount: Decimal
    timestamp: datetime
