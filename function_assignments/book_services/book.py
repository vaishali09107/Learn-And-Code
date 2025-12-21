class Book:
    """ Represents a readable book. """

    def __init__(self, title: str, author: str, pages: list[str]):
        self._title = title
        self._author = author
        self._pages = pages
        self._current_page_index = 0

    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self._author

    def get_current_page(self) -> str:
        return self._pages[self._current_page_index]

    def turn_page(self) -> None:
        if self._current_page_index < len(self._pages) - 1:
            self._current_page_index += 1
