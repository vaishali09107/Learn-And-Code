from abc import ABC, abstractmethod

class Printer(ABC):
    """ Printer abstraction. """

    @abstractmethod
    def print_page(self, page_content: str) -> None:
        pass

class PlainTextPrinter(Printer):
    def print_page(self, page_content: str) -> None:
        print(page_content)

class HtmlPrinter(Printer):
    def print_page(self, page_content: str) -> None:
        print(f'<div class="single-page">{page_content}</div>')
