from abc import ABC, abstractmethod
from models.creator_metrics import CreatorMetrics


class EarningStrategy(ABC):

    @abstractmethod
    def calculate(self, metrics: CreatorMetrics) -> float:
        pass