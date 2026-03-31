from ..record import Record
from .base import Exporter


class CsvExporter(Exporter):
    def export(self, records: list[Record], file_path: str) -> None:
        header = "ID,NAME,VALUE,DATE,DOUBLED_VALUE,SQUARED_VALUE"
        lines = [header]

        for record in records:
            lines.append(
                f"{record.id},{record.name},{record.value},"
                f"{record.date},{record.doubled_value},{record.squared_value}"
            )

        with open(file_path, "w") as f:
            f.write("\n".join(lines))
