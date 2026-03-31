from dataclasses import fields

from ..record import Record
from .base import Exporter


class JsonExporter(Exporter):
    def export(self, records: list[Record], file_path: str) -> None:
        json_lines = ["["]

        for i, record in enumerate(records):
            properties = self._build_properties(record)
            json_obj = "  {" + ", ".join(properties) + "}"
            if i < len(records) - 1:
                json_obj += ","
            json_lines.append(json_obj)

        json_lines.append("]")

        with open(file_path, "w") as f:
            f.write("\n".join(json_lines))

    @staticmethod
    def _build_properties(record: Record) -> list[str]:
        return [
            f'"{field.name}": "{getattr(record, field.name)}"'
            for field in fields(record)
            if getattr(record, field.name) is not None
        ]
