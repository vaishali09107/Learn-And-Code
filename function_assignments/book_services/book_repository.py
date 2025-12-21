import pickle
from pathlib import Path

class BookRepository:
    """ Handles saving and loading books. """

    def save(self, book: Book) -> None:
        filename = f"{book.get_title()} - {book.get_author()}.book"
        file_path = Path("documents") / filename

        with open(file_path, "wb") as file:
            pickle.dump(book, file)
