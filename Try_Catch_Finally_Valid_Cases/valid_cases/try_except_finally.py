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
    finally:
        service.close_connection()


if __name__ == "__main__":
    print("Case 4: try + except + finally\n")

    print("Scenario A - Success (finally still runs):")
    register_user("alice", "alice@company.com")

    print("\nScenario B - Failure (finally still runs):")
    register_user("bob", "bob@invalid", scenario="db_error")

