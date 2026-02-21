from .base import Exporter
from .csv_exporter import CsvExporter
from .json_exporter import JsonExporter
from .xml_exporter import XmlExporter


class ExporterFactory:
    """Creates Exporter instances by format name. New formats can be
    registered at runtime via `register()` without modifying existing code."""

    _registry: dict[str, type[Exporter]] = {
        "csv": CsvExporter,
        "json": JsonExporter,
        "xml": XmlExporter,
    }

    @classmethod
    def create(cls, format_type: str) -> Exporter:
        exporter_class = cls._registry.get(format_type.lower())
        if exporter_class is None:
            raise ValueError(f"Unsupported export format: {format_type}")
        return exporter_class()

    @classmethod
    def register(cls, format_type: str, exporter_class: type[Exporter]) -> None:
        cls._registry[format_type.lower()] = exporter_class
