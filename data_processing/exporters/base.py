from abc import ABC, abstractmethod

from ..record import Record


class Exporter(ABC):
    """Base class for all export formats."""

    @abstractmethod
    def export(self, records: list[Record], file_path: str) -> None:
        pass
