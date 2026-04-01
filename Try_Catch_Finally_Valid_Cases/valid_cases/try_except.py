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


if __name__ == "__main__":
    print("Case 1: try + except\n")

    print("Scenario A - Success:")
    register_user("alice", "alice@company.com")

    print("\nScenario B - Validation fails:")
    register_user("bob", "bob@invalid", scenario="validation_error")

    print("\nScenario C - Database fails:")
    register_user("charlie", "charlie@company.com", scenario="db_error")

