class APIClientError(Exception):
    """Custom exception for API client errors."""
    
    def __init__(self, error_type: APIErrorType, message: str, status_code: int = None):
        self.error_type = error_type
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
    
    def to_dict(self) -> Dict:
        """Convert exception to dictionary response."""
        return {
            "success": False,
            "error_type": self.error_type.value,
            "message": self.message
        }