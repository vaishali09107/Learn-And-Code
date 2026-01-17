from user_infrastructure import db, save_to_file

EMPTY_STRING = ""

def is_user_valid(user):
    """Checks if the user is valid."""
    has_name = user.name != EMPTY_STRING
    has_email = user.email != EMPTY_STRING
    return has_name and has_email

def store_user_in_database(user):
    """Stores the user in the database."""
    db.add_record("Users", user)

def create_user_backup(user):
    """Creates a backup of the user to a file."""
    file_path = f"/backup/users/{user.id}.txt"
    save_to_file(file_path, user)

def persist_user(user):
    """Persists the user to the database with backup."""
    if not is_user_valid(user):
        print("Invalid user data")
        return

    store_user_in_database(user)
    create_user_backup(user)
