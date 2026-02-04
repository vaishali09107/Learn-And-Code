from domain.wallet import Wallet

class Customer:
    """Customer entity that controls its own payment behavior."""

    def __init__(self, first_name: str, last_name: str, wallet: Wallet) -> None:
        """Initialize the customer with a first name, last name, and wallet."""
        self._first_name = first_name
        self._last_name = last_name
        self._wallet = wallet

    @property
    def first_name(self) -> str:
        """Get the first name of the customer."""
        return self._first_name

    @property
    def last_name(self) -> str:
        """Get the last name of the customer."""
        return self._last_name

    def pay(self, amount: float) -> bool:
        """Attempt to pay the requested amount.

        Returns True if payment succeeds, otherwise False.
        """
        if self._can_afford(amount):
            self._wallet.debit(amount)
            return True
        return False

    def _can_afford(self, amount: float) -> bool:
        """Internal check for sufficient funds.

        Kept private to avoid exposing wallet details.
        """
        return self._wallet.balance >= amount
