from datetime import datetime

from .record import Record

INPUT_DATE_FORMAT = "%Y-%m-%d"


class RecordTransformer:
    def __init__(self, output_date_format: str = INPUT_DATE_FORMAT):
        self._output_date_format = output_date_format

    def transform(self, records: list[Record]) -> list[Record]:
        return [self._transform_record(record) for record in records]

    def _transform_record(self, record: Record) -> Record:
        record.name = record.name.upper()
        self._format_date(record)
        self._calculate_derived_values(record)
        return record

    def _format_date(self, record: Record) -> None:
        if record.date is None:
            return
        try:
            parsed_date = datetime.strptime(record.date, INPUT_DATE_FORMAT)
            record.date = parsed_date.strftime(self._output_date_format)
        except ValueError:
            pass

    @staticmethod
    def _calculate_derived_values(record: Record) -> None:
        value = float(record.value)
        record.doubled_value = value * 2
        record.squared_value = value * value
