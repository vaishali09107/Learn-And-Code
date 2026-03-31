from abc import ABC, abstractmethod
from datetime import datetime


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass


class FileLogger(Logger):
    def __init__(self, file_path: str = "processing.log"):
        self._file_path = file_path
        self._buffer: list[str] = []

    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._buffer.append(f"[{timestamp}] {message}")

    def flush(self) -> None:
        with open(self._file_path, "w") as f:
            f.write("\n".join(self._buffer) + "\n")
