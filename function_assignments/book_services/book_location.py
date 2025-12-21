class LibraryLocation:
    """ Represents a physical location of a book in a library. """

    def __init__(self, room_number: str, shelf_number: str):
        self.room_number = room_number
        self.shelf_number = shelf_number

    def get_location(self) -> str:
        return f"Room {self.room_number}, Shelf {self.shelf_number}"
