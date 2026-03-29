class LogWriter:
    """Log writing service."""
    
    def write_log(self, message: str) -> None:
        """Writes a log message."""
        print(message)

class MessageService:
    """Message service for sending notifications to customers."""
    
    def dispatch(self, customer_id: str, message: str) -> None:
        """Dispatches a notification to a customer."""
        print(f"Notify {customer_id}: {message}")
