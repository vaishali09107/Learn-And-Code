from .config import ProcessingConfig
from .exporters.factory import ExporterFactory
from .logger import Logger
from .reader import CsvRecordReader
from .record import Record
from .statistics_calculator import StatisticsCalculator
from .transformer import RecordTransformer
from .validator import RecordValidator


class DataProcessor:
    """Orchestrates the data processing pipeline."""

    def __init__(
        self,
        reader: CsvRecordReader,
        validator: RecordValidator,
        transformer: RecordTransformer,
        statistics_calculator: StatisticsCalculator,
        logger: Logger,
        config: ProcessingConfig,
    ):
        self._reader = reader
        self._validator = validator
        self._transformer = transformer
        self._statistics_calculator = statistics_calculator
        self._logger = logger
        self._config = config

        self._records: list[Record] = []
        self._error_messages: list[str] = []
        self._statistics: dict[str, int] = {}

    def process(self, input_path: str, output_path: str) -> None:
        self._logger.log("Starting data processing")

        try:
            self._read_data(input_path)
            self._validate_records()
            self._transform_records()
            self._compute_statistics()
            self._write_output(output_path)
            self._logger.flush()
            self._print_summary()
        except Exception as ex:
            self._handle_fatal_error(ex)

    def export(self, file_path: str, format_type: str) -> None:
        self._logger.log(f"Exporting to {format_type.upper()}: {file_path}")
        exporter = ExporterFactory.create(format_type)
        exporter.export(self._records, file_path)
        self._logger.log(f"{format_type.upper()} export complete")

    def filter_by_value(self, min_value: float) -> list[Record]:
        filtered = [
            r for r in self._records if float(r.value) >= min_value
        ]
        self._logger.log(
            f"Filtered {len(filtered)} records with value >= {min_value}"
        )
        return filtered

    def display_statistics(self) -> None:
        print("\n=== Processing Statistics ===")
        for key, value in self._statistics.items():
            print(f"{key}: {value}")

        if self._error_messages:
            print("\n=== Errors ===")
            for error in self._error_messages:
                print(f"- {error}")

    @property
    def records(self) -> list[Record]:
        return list(self._records)

    @property
    def error_messages(self) -> list[str]:
        return list(self._error_messages)

    @property
    def statistics(self) -> dict[str, int]:
        return dict(self._statistics)

    def _read_data(self, input_path: str) -> None:
        self._logger.log(f"Reading input file: {input_path}")
        self._records, read_errors = self._reader.read(input_path)
        self._error_messages.extend(read_errors)
        self._logger.log(f"Parsed {len(self._records)} records")

    def _validate_records(self) -> None:
        if not self._config.should_validate:
            return
        self._logger.log("Validating data...")
        self._records, validation_errors = self._validator.validate(
            self._records
        )
        self._error_messages.extend(validation_errors)
        self._logger.log(
            f"Validation complete. {len(self._records)} valid records"
        )

    def _transform_records(self) -> None:
        if not self._config.should_transform:
            return
        self._logger.log("Transforming data...")
        self._records = self._transformer.transform(self._records)
        self._logger.log("Transformation complete")

    def _compute_statistics(self) -> None:
        self._logger.log("Calculating statistics...")
        self._statistics = self._statistics_calculator.calculate(
            self._records, len(self._error_messages)
        )
        self._logger.log(
            f"Statistics calculated: {len(self._statistics)} metrics"
        )

    def _write_output(self, output_path: str) -> None:
        self._logger.log(f"Writing output to: {output_path}")
        exporter = ExporterFactory.create("csv")
        exporter.export(self._records, output_path)
        self._logger.log(
            f"Output written. {len(self._records)} records processed"
        )

    def _print_summary(self) -> None:
        print("Processing complete!")
        print(f"Records processed: {len(self._records)}")
        print(f"Errors: {len(self._error_messages)}")

    def _handle_fatal_error(self, ex: Exception) -> None:
        self._error_messages.append(f"Fatal error: {ex}")
        self._logger.log(f"FATAL ERROR: {ex}")
        self._logger.flush()
        print(f"Processing failed: {ex}")
