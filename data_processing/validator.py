from .record import Record


class RecordValidator:
    def validate(self, records: list[Record]) -> tuple[list[Record], list[str]]:
        valid_records: list[Record] = []
        errors: list[str] = []

        for record in records:
            record_errors = self._validate_record(record)
            if record_errors:
                errors.extend(record_errors)
            else:
                valid_records.append(record)

        return valid_records, errors

    @staticmethod
    def _validate_record(record: Record) -> list[str]:
        errors: list[str] = []

        if not record.id:
            errors.append("Record missing ID")

        if not record.name:
            errors.append(f"Record {record.id} missing name")

        if not _is_numeric(record.value):
            errors.append(f"Record {record.id} has invalid value")

        return errors


def _is_numeric(value: str) -> bool:
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
