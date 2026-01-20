from user_infrastructure import get_database_connector, save_to_file

EMPTY_STRING = ""
DEFAULT_BACKUP_DIRECTORY = "/backup/users"

def is_user_valid(user):
    """Checks if the user is valid."""
    has_name = user.name != EMPTY_STRING
    has_email = user.email != EMPTY_STRING
    return has_name and has_email

def store_user_in_database(user, database_connector=None):
    """Stores the user in the database."""
    if database_connector is None:
        database_connector = get_database_connector()
    database_connector.add_record("Users", user)

def create_user_backup(user, backup_directory=DEFAULT_BACKUP_DIRECTORY):
    """Creates a backup of the user to a file."""
    file_path = f"{backup_directory}/{user.id}.txt"
    save_to_file(file_path, user)

def persist_user(user, database_connector=None, backup_directory=DEFAULT_BACKUP_DIRECTORY):
    """Persists the user to the database with backup."""
    if not is_user_valid(user):
        raise ValueError("Invalid user data")

    store_user_in_database(user, database_connector)
    create_user_backup(user, backup_directory)

