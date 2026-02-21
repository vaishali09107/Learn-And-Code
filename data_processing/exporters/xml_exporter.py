from dataclasses import fields

from ..record import Record
from .base import Exporter


class XmlExporter(Exporter):
    def export(self, records: list[Record], file_path: str) -> None:
        xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>', "<records>"]

        for record in records:
            xml_lines.append("  <record>")
            for field in fields(record):
                value = getattr(record, field.name)
                if value is not None:
                    xml_lines.append(
                        f"    <{field.name}>{value}</{field.name}>"
                    )
            xml_lines.append("  </record>")

        xml_lines.append("</records>")

        with open(file_path, "w") as f:
            f.write("\n".join(xml_lines))
