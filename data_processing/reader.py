from .record import Record


class CsvRecordReader:
    def read(self, file_path: str) -> tuple[list[Record], list[str]]:
        records: list[Record] = []
        errors: list[str] = []

        with open(file_path, "r") as f:
            lines = f.read().splitlines()

        for line in lines:
            if not line.strip():
                continue

            parts = line.split(",")
            if len(parts) >= 3:
                records.append(self._parse_line(parts))
            else:
                errors.append(f"Invalid line format: {line}")

        return records, errors

    @staticmethod
    def _parse_line(parts: list[str]) -> Record:
        return Record(
            id=parts[0].strip(),
            name=parts[1].strip(),
            value=parts[2].strip(),
            date=parts[3].strip() if len(parts) >= 4 else None,
        )
