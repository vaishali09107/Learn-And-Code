from models.exceptions import (
    ValidationError,
    DatabaseConnectionError,
    DuplicateUserError,
)


class UserService:

    def __init__(self, scenario="success"):
        self._scenario = scenario
        self._connection_open = False

    def validate_user(self, username, email):
        if self._scenario == "validation_error":
            raise ValidationError(f"Invalid email: {email}")
        print(f"  Validated user {username} ({email})")

    def connect_to_database(self):
        if self._scenario == "db_error":
            raise DatabaseConnectionError("Could not connect to database")
        self._connection_open = True
        print("  Connected to database")

    def save_user(self, username, email):
        if self._scenario == "duplicate_error":
            raise DuplicateUserError(f"User {username} already exists")
        print(f"  Saved {username} to database")

    def close_connection(self):
        if self._connection_open:
            self._connection_open = False
            print("  Closed database connection")
        else:
            print("  No connection to close")

    def send_welcome_email(self, email):
        print(f"  Sent welcome email to {email}")
