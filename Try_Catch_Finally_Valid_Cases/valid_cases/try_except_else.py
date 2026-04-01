import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, PROJECT_ROOT)

from models.exceptions import ValidationError, DatabaseConnectionError
from services.user_service import UserService


def register_user(username, email, scenario="success"):
    service = UserService(scenario=scenario)

    try:
        service.validate_user(username, email)
        service.connect_to_database()
        service.save_user(username, email)
    except (ValidationError, DatabaseConnectionError) as error:
        print(f"  Registration failed: {error}")
    else:
        service.send_welcome_email(email)
        print(f"  Done! {username} registered successfully")


if __name__ == "__main__":
    print("Case 3: try + except + else\n")

    print("Scenario A - Success (else runs):")
    register_user("alice", "alice@company.com")

    print("\nScenario B - Failure (else skipped):")
    register_user("bob", "bob@invalid", scenario="validation_error")

