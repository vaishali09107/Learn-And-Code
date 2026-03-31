from data_processing import (
    CsvRecordReader,
    DataProcessor,
    FileLogger,
    ProcessingConfig,
    RecordTransformer,
    RecordValidator,
    SampleDataGenerator,
    StatisticsCalculator,
)


def main():
    SampleDataGenerator.generate("input.csv", 50)

    config = ProcessingConfig(
        date_format="%m/%d/%Y",
        batch_size=50,
        should_validate=True,
        should_transform=True,
    )

    processor = DataProcessor(
        reader=CsvRecordReader(),
        validator=RecordValidator(),
        transformer=RecordTransformer(output_date_format=config.date_format),
        statistics_calculator=StatisticsCalculator(),
        logger=FileLogger(),
        config=config,
    )

    processor.process("input.csv", "output.csv")
    processor.display_statistics()

    processor.export("output.json", "json")
    processor.export("output.xml", "xml")

    try:
        processor.export("output_test.json", "json")
        processor.export("output_test.xml", "xml")
    except ValueError as ex:
        print(f"Export error: {ex}")

    filtered = processor.filter_by_value(100)
    print(f"\nFiltered records: {len(filtered)}")

    print(f"\nRecords processed: {len(processor.records)}")
    print(f"Errors: {len(processor.error_messages)}")


if __name__ == "__main__":
    main()
