from dataclasses import dataclass


@dataclass
class ProcessingConfig:
    date_format: str = "%Y-%m-%d"
    batch_size: int = 100
    should_validate: bool = True
    should_transform: bool = True
