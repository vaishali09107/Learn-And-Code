import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, PROJECT_ROOT)

from services.user_service import UserService


def register_user(username, email, scenario="success"):
    service = UserService(scenario=scenario)

    try:
        service.validate_user(username, email)
        service.connect_to_database()
        service.save_user(username, email)
    finally:
        service.close_connection()


if __name__ == "__main__":
    print("Case 6: try + finally (no except)\n")

    print("Scenario A - Success (finally runs normally):")
    register_user("alice", "alice@company.com")

    print("\nScenario B - Failure (finally runs, error goes to caller):")
    try:
        register_user("bob", "bob@invalid", scenario="validation_error")
    except Exception as error:
        print(f"  Caller caught the error: {error}")

