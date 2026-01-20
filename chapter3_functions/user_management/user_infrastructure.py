class DatabaseConnector:
    """Connector for database operations."""

    def add_record(self, table, record):
        """Adds a record into a table."""
        pass


def get_database_connector():
    """Factory function to get a database connector instance."""
    return DatabaseConnector()


def save_to_file(file_path, content):
    """Saves content to a file."""
    pass


def get_file_saver():
    """Factory function to get the file saver function."""
    return save_to_file
