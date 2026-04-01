import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, PROJECT_ROOT)

from models.exceptions import (
    ValidationError,
    DatabaseConnectionError,
    DuplicateUserError,
)
from services.user_service import UserService


def register_user(username, email, scenario="success"):
    service = UserService(scenario=scenario)
 
    try:
        service.validate_user(username, email)
        service.connect_to_database()
        service.save_user(username, email)
    except ValidationError as error:
        print(f"  Bad input: {error}")
    except DatabaseConnectionError as error:
        print(f"  Database problem: {error}")
    except DuplicateUserError as error:
        print(f"  Already exists: {error}")
    else:
        service.send_welcome_email(email)
        print(f"  Done! {username} registered successfully")
    finally:
        service.close_connection()


if __name__ == "__main__":
    print("Case 5: try + except + else + finally (full form)\n")

    print("Scenario A - Success (else + finally run):")
    register_user("alice", "alice@company.com")

    print("\nScenario B - Validation fails (except + finally run):")
    register_user("bob", "bob@invalid", scenario="validation_error")

    print("\nScenario C - Database fails (except + finally run):")
    register_user("charlie", "charlie@company.com", scenario="db_error")

    print("\nScenario D - Duplicate user (except + finally run):")
    register_user("alice", "alice@company.com", scenario="duplicate_error")

