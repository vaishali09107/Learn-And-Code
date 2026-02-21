import random
from datetime import datetime, timedelta


class SampleDataGenerator:
    @staticmethod
    def generate(file_path: str, record_count: int) -> None:
        lines: list[str] = []

        for i in range(1, record_count + 1):
            record_id = f"ID{i:04d}"
            name = f"Item{i}"
            value = random.randint(10, 999)
            date = datetime.now() - timedelta(days=random.randint(0, 364))
            lines.append(
                f"{record_id},{name},{value},{date.strftime('%Y-%m-%d')}"
            )

        with open(file_path, "w") as f:
            f.write("\n".join(lines))

        print(f"Generated {record_count} sample records in {file_path}")
