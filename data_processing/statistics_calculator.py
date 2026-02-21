from .record import Record


class StatisticsCalculator:
    def calculate(
        self, records: list[Record], error_count: int
    ) -> dict[str, int]:
        total_value = sum(float(r.value) for r in records)
        record_count = len(records)

        return {
            "total_records": record_count,
            "error_count": error_count,
            "total_value": int(total_value),
            "average_value": (
                int(total_value / record_count) if record_count > 0 else 0
            ),
        }
