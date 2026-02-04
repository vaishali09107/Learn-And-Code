class Wallet:
    """Data structure representing a simple wallet balance."""

    def __init__(self, balance: float = 0.0) -> None:
        """Initialize the wallet with a given balance."""
        self._balance = balance

    @property
    def balance(self) -> float:
        """Get the current balance of the wallet."""
        return self._balance

    def debit(self, amount: float) -> None:
        """Decrease the balance by a given amount."""
        self._balance -= amount


