from dataclasses import dataclass
from typing import Optional


@dataclass
class Record:
    """Represents a single data record parsed from input."""

    id: str
    name: str
    value: str
    date: Optional[str] = None
    doubled_value: Optional[float] = None
    squared_value: Optional[float] = None
